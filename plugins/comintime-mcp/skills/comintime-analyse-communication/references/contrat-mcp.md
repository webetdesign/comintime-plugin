# Contrat MCP recommandé

> **État : implémenté.** Les quatre outils décrits ci-dessous existent dans le
> serveur MCP ComInTime :
> `get-communication-audit-context`, `get-communication-activity-statistics`,
> `list-publications-for-communication-analysis`, `get-communication-social-statistics`. Ils sont en lecture seule,
> agissent au nom de l'utilisateur du jeton et excluent les éléments cachés par
> défaut. Les périodes par défaut valent 3 mois glissants. La section « Repli avec
> les outils actuels » ne sert que si ces outils sont indisponibles.

## Choisir les lectures selon la demande

- **Avis sur la stratégie** : `get-communication-audit-context`, complété si nécessaire par les lectures du profil et des fondamentaux. Aucun appel aux statistiques ou aux publications ; aucune période d’activité nécessaire.
- **Avis sur la communication mise en œuvre** : contexte stratégique + `get-communication-activity-statistics`, puis listing ciblé pour les preuves. Les performances sociales, si disponibles, complètent l’alignement avec les objectifs.
- **Audit complet explicite** : les deux diagnostics, séparés dans la restitution.

Cette sélection s’applique aussi aux solutions de repli : `publications-in-period` n’est pas un repli pour l’analyse de la stratégie seule.

## Surface actuelle réutilisable

La version actuelle du plugin permet déjà de résoudre le dossier et de récupérer une partie du contexte avec `list-folders`, `get-folder-profile`, `get-post-context`, `list-goals`, `list-targets`, `list-supports`, `list-themes` et `publications-in-period`. `suggest-next-post` peut compléter les recommandations éditoriales, mais ne remplace pas l’analyse statistique.

Ces outils ne suffisent pas à un audit complet si leurs réponses omettent les messages, positions, états cachés, dates d’effet et associations détaillées des publications.

## Outils de haut niveau

Utiliser le contexte stratégique, les agrégats d’activité et les statistiques sociales, puis le listing seulement pour les exemples nécessaires.

Une définition structurée des entrées est fournie dans [mcp-outils-proposes.json](mcp-outils-proposes.json) pour faciliter l’implémentation.

### `get-communication-audit-context`

Objectif : fournir en une lecture tout le contexte nécessaire à l’analyse de cohérence.

Entrée :

```json
{
  "folder": "identifiant ou nom",
  "asOf": "2026-09-04",
  "includeHidden": false
}
```

Sortie minimale :

```json
{
  "folder": {"id": 1, "name": "…", "timezone": "Europe/Paris"},
  "companyProfile": {},
  "strategyEffectiveFrom": "date optionnelle",
  "goals": [{"id": 1, "title": "…", "position": 1}],
  "targets": [{"id": 2, "title": "…", "position": 1, "supportIds": []}],
  "supports": [{
    "id": 3,
    "title": "…",
    "type": "linkedin",
    "position": 1,
    "number": 2,
    "frequency": "month",
    "active": true,
    "connectionStatus": "connected",
    "targetIds": [],
    "themeItemIds": [],
    "editorialRules": {}
  }],
  "messages": [{"id": 4, "goalId": 1, "targetId": 2, "text": "…"}],
  "themes": [{"id": 5, "title": "…", "items": [{"id": 6, "title": "…", "supportIds": []}]}],
  "excluded": {"hiddenGoals": 0, "hiddenTargets": 0, "hiddenSupports": 0, "hiddenMessages": 0, "hiddenThemeItems": 0}
}
```

Le serveur filtre les éléments cachés par défaut. `includeHidden` est réservé à un audit explicite de la configuration et ne doit jamais faire entrer ces éléments dans les attendus d’activité.

### `get-communication-activity-statistics`

Objectif : utiliser le moteur statistique ComInTime et éviter au modèle de recompter les publications.

Entrée :

```json
{
  "folder": "identifiant ou nom",
  "from": "2026-06-04",
  "to": "2026-09-04",
  "statuses": ["STATUS_SUCCESS_PUBLICATION"],
  "includeMonthlyBreakdown": true,
  "includeFutureOutlook": true
}
```

Sortie minimale :

```json
{
  "period": {"from": "…", "to": "…"},
  "totals": {"published": 0, "planned": 0, "scheduled": 0},
  "dataQuality": {
    "withoutSupport": 0,
    "withoutGoal": 0,
    "withoutTarget": 0,
    "withoutMessage": 0,
    "withoutThemeItem": 0
  },
  "bySupport": [],
  "byGoal": [],
  "byTarget": [],
  "byMessage": [],
  "byTheme": [],
  "byThemeItem": [],
  "byMonth": [],
  "futureOutlook": {}
}
```

Chaque ligne agrégée devrait fournir l’identifiant, le titre, la position, le nombre observé, la part observée, le nombre attendu lorsqu’il est défini par la cadence, la date de dernière utilisation et la ventilation mensuelle. Le serveur doit exclure les éléments cachés avant calcul et utiliser l’historique de configuration s’il existe.

### `list-publications-for-communication-analysis`

Objectif : obtenir un échantillon ou un sous-ensemble paginé pour expliquer un écart et vérifier l’alignement sémantique des messages.

Entrée :

```json
{
  "folder": "identifiant ou nom",
  "from": "2026-06-04",
  "to": "2026-09-04",
  "status": "STATUS_SUCCESS_PUBLICATION",
  "supportIds": [],
  "goalIds": [],
  "targetIds": [],
  "messageIds": [],
  "themeItemIds": [],
  "limit": 50,
  "cursor": null,
  "includeContent": true
}
```

Chaque publication retourne : identifiant, date, titre, contenu ou extrait, support, objectif, cible, message, thème et sous-thème. Limiter et paginer la réponse ; ne charger le contenu complet que lorsque l’analyse sémantique le nécessite.

## Pourquoi ces outils

- Le serveur calcule les agrégats à proximité des données et réutilise l’outil statistique existant.
- Le modèle reçoit peu de données, mais suffisamment structurées pour raisonner correctement.
- Les éléments cachés sont exclus de manière déterministe.
- Les rangs, cadences et associations restent ceux de ComInTime.
- L’analyse sémantique coûteuse n’est déclenchée que pour les messages ou exemples nécessaires.

## Règles techniques

- Outils en lecture seule, idempotents et `openWorldHint: false`.
- Authentification OAuth au nom de l’utilisateur ; ne pas accepter `userEmail` dans un appel OAuth normal.
- Dates ISO et fuseau du dossier dans toutes les réponses.
- Identifiants stables et mêmes libellés que dans ComInTime.
- Ne jamais exposer de jeton de réseau social, secret ou donnée personnelle inutile.
- Retourner les dénominateurs et les catégories non caractérisées, pas seulement des pourcentages.
- Versionner le schéma ou annoncer les champs indisponibles plutôt que de renvoyer silencieusement zéro.
- N’exposer à cette compétence que des outils de lecture pour la stratégie. La modification des fondamentaux reste réservée à l’application web ComInTime.

## Repli avec les outils actuels

Si ces outils sont indisponibles :

1. appeler `get-folder-profile` et `get-post-context` ;
2. compléter avec `list-goals`, `list-targets`, `list-supports` et `list-themes` si leurs réponses sont plus riches ;
3. uniquement pour la communication mise en œuvre, appeler `publications-in-period` sur la période demandée ou les trois derniers mois par défaut ;
4. produire uniquement les constats supportés par les champs reçus ;
5. déclarer « non mesurable » toute dimension dont les priorités, éléments cachés, messages ou associations manquent.

Ne pas utiliser `create-post`, `update-post` ou `publish-post` pendant un diagnostic. Ne jamais utiliser depuis ChatGPT un éventuel outil de création, modification, masquage, réactivation, réordonnancement ou suppression de la stratégie.

## Sémantique métier de « message »

Un message est un objet de la stratégie ComInTime, identifié et rattaché à un objectif et une cible. `messages`, `messageIds` et les agrégats par message se réfèrent à ces objets configurés. La proximité sémantique entre un texte publié et un message ne constitue pas une association enregistrée. Une analyse de fidélité du texte peut compléter les associations réelles mais ne doit pas les remplacer dans les décomptes.
## `get-communication-social-statistics`

Entrées : `folder` obligatoire ; `from`, `to` facultatifs (trois mois par défaut), `userEmail` réservé au contexte autorisé du serveur. Lecture seule, aucune collecte réseau.

Retour : `schemaVersion`, `folderId`, `period`, `source`, `semantics`, `pages`, `excludedPublications`. Chaque page fournit ses supports visibles, son réseau, son instantané de page, ses métriques avec couverture et dates, sa ventilation par mois de publication et les limites de collecte. Les supports cachés et les publications sans correspondance entre page et support visible sont exclus.

Voir [performances-sociales.md](performances-sociales.md) pour les définitions et les limites, notamment Google My Business sans collecte et la portée cumulée des compteurs.
