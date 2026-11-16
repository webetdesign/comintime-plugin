# Contrat d’intégration recommandé

Ce contrat décrit des actions métier de haut niveau à exposer à un agent par MCP, par une application ChatGPT ou par une couche d’API équivalente. Les noms sont indicatifs. L’adaptateur peut réutiliser les API ComInTime existantes. Les décisions d’autorisation et de statut restent côté serveur.

## Principes

- Authentifier chaque appel avec l’identité réelle de l’utilisateur.
- Limiter toutes les lectures et mutations aux dossiers auxquels il a accès.
- Fournir un contexte agrégé pour éviter une succession de requêtes et un tunnel conversationnel.
- Rendre les actions idempotentes lorsque leur répétition pourrait créer des doublons.
- Retourner le statut réellement obtenu, jamais seulement le statut demandé.
- Faire respecter par ComInTime les droits, contraintes réseau et transitions de statut.

## Actions de lecture

### `list_communication_folders`

Retourne les dossiers accessibles avec `id`, `name` et, si possible, un indicateur permettant d’identifier le dossier actif ou récent. À utiliser uniquement lorsque le dossier ne peut pas être déduit du contexte de session.

### `get_publication_context`

Entrée recommandée :

```json
{
  "folder_id": "string",
  "intended_date": "date-time optionnelle",
  "requested_media_id": "string optionnelle",
  "recent_limit": 20
}
```

Réponse recommandée :

```json
{
  "company": {},
  "goals": [],
  "targets": [],
  "messages": [],
  "themes": [],
  "media": [],
  "monthly_activity": {
    "published": [],
    "planned": [],
    "scheduled": [],
    "coverage": {}
  },
  "permissions": {},
  "timezone": "Europe/Paris"
}
```

Chaque média doit indiquer sa ligne éditoriale, ses formats, son rythme, sa priorité, ses limites de contenu, sa page ou son compte de diffusion et l’état de la connexion. Les objectifs, cibles, médias, thématiques et sous-thématiques doivent exposer leur identifiant stable et leur ordre de priorité.

`coverage` peut être calculé par ComInTime afin de refléter exactement sa logique mensuelle. Il doit inclure les contenus publiés, planifiés et programmés.

### `suggest_next_publication`

Entrée : `folder_id`, `from` (date optionnelle). À partir de la stratégie configurée
(rythme de chaque média, rotation des cibles / objectifs / sous-thématiques, contenus
déjà planifiés), retourne le **prochain créneau** à couvrir : `date`, `support`, `target`,
`goal`, `subject` (sous-thématique). **Ne rédige aucun contenu** — la rédaction du titre et
du texte revient au modèle client, qui appelle ensuite `save_publication` avec ces
identifiants. Les champs `target`, `goal` ou `subject` peuvent être absents si la stratégie
n’en impose pas : le modèle choisit alors librement en restant cohérent.

### `get_publication_status`

Retourne l’état courant d’une publication, sa date, sa destination, les validations restantes et les éventuelles erreurs de diffusion.

## Actions d’écriture

### `save_publication`

Crée ou met à jour une publication caractérisée.

Entrée minimale recommandée :

```json
{
  "idempotency_key": "string",
  "subject_id": "string optionnelle",
  "folder_id": "string",
  "title": "string",
  "content": "string",
  "summary": "string optionnelle",
  "instructions": "string optionnelle",
  "media_id": "string optionnelle",
  "format_id": "string optionnelle",
  "goal_id": "string optionnelle",
  "target_id": "string optionnelle",
  "message_id": "string optionnelle",
  "theme_ids": [],
  "intended_date": "date-time optionnelle",
  "requested_maturity": "idea|qualified"
}
```

Le serveur choisit le statut autorisé correspondant à la maturité demandée et retourne les champs effectivement enregistrés.

### `submit_publication_for_validation`

Soumet une publication existante au circuit de validation. Retourne le statut réel et le rôle ou groupe attendu, sans divulguer d’informations personnelles inutiles.

### `validate_publication`

Valide une publication si l’utilisateur en a le droit. Refuse explicitement sinon. La présence de cet outil ne constitue jamais une autorisation implicite.

### `schedule_publication`

Entrée recommandée :

```json
{
  "idempotency_key": "string",
  "subject_id": "string",
  "media_id": "string",
  "publish_at": "date-time",
  "confirm_content_version": "string optionnelle"
}
```

ComInTime vérifie les droits, la validation, les champs requis, les limites du réseau, la connexion et la date. La réponse distingue au minimum `scheduled`, `ready_for_manual_publication`, `validation_required` et `blocked`, avec le statut ComInTime et une raison exploitable.

Pour un site web ou un média sans diffusion automatique, cette action ne simule pas une publication. Elle retourne `ready_for_manual_publication` et place le contenu dans l’état approprié.

## Données à ne pas exposer au modèle

Ne jamais retourner les jetons OAuth, secrets, clés d’API, identifiants techniques de session ou données personnelles sans utilité éditoriale. Exposer seulement un état de connexion et, si nécessaire, le nom public de la page ou du compte.

## Correspondance avec l’existant ComInTime

L’adaptateur peut s’appuyer sur les entités `Subject`, `Goal`, `Target`, `Message`, `Support`, `Theme` et sur les services de suggestion, de génération, de validation et de publication existants. Il doit centraliser les règles déjà présentes dans ComInTime au lieu de les réimplémenter dans le prompt.

## Sémantique métier de `messages`

`messages` désigne les éléments configurés de la stratégie, pas des textes générés ou des échanges de conversation. Chaque élément doit conserver son identifiant, son texte et ses rattachements objectif/cible. Dans `get-communication-audit-context`, ces champs sont `id`, `text`, `goalId` et `targetId`. Cette lecture peut compléter le contexte de publication lorsqu’il ne fournit pas les messages. Une absence de champ ne prouve pas une absence de configuration. L’association d’une publication à un message doit être confirmée par les données retournées, jamais déduite du seul contenu rédigé.

## Association persistée au message

`get-post-context.messages` expose les messages renseignés dont l’objectif et la cible sont visibles dans le dossier. `create-post` et `update-post` acceptent `messageId` ; le serveur vérifie son appartenance au dossier et l’égalité de son objectif/cible avec le couple final du post. `update-post` conserve le message si le paramètre est omis ; `clear: ["message"]` retire explicitement l’association. Une incohérence est refusée avant mutation. La réponse `post.message` contient `id`, `text`, `goalId`, `targetId`, ou `null`. Aucun message stratégique n’est créé par ces outils.
## Champs de ligne éditoriale du support

`get-post-context` et `list-supports` exposent `do`, `dont`, `postSize`, `tones`, `personalPronoun`, `tvDistinction` et `signature`. `tvDistinction` vaut `TU` (tutoiement), `VOS` (vouvoiement) ou `null` ; il est distinct du pronom de l’émetteur. Ces champs doivent être utilisés à la création comme à la modification du texte. Voir [strategie-et-redaction.md](strategie-et-redaction.md) pour leur interprétation et la relecture finale. La vérification éditoriale relève du LLM ; les outils d’enregistrement ne certifient pas le respect sémantique de ces règles.
