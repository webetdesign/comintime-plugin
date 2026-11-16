# Stratégie et rédaction

## Modèle stratégique

ComInTime formalise la communication d’une entreprise autour de six ensembles utiles à la rédaction :

- le contexte de l’entreprise : présentation, activités, valeurs, avantages, projets, équipe, histoire, certifications et autres éléments distinctifs ;
- les objectifs de communication, ordonnés par priorité ;
- les cibles, également ordonnées par priorité et éventuellement décrites comme des personas ;
- les médias et leur ligne éditoriale : rythme, formats, ton, longueur, tutoiement ou vouvoiement, pronom, signature, consignes à suivre et à éviter ;
- les messages, qui correspondent au croisement d’un objectif et d’une cible ;
- les thématiques et sous-thématiques que l’entreprise peut aborder.

Le **message ComInTime** est un élément configuré de la stratégie, rattaché à un objectif et une cible. Son texte définit ce que la structure souhaite faire comprendre à cette cible pour atteindre cet objectif. L’idée du post et son angle rédactionnel sont distincts de cet élément.

Le texte de la publication peut exprimer cette intention avec une formulation adaptée au média, sans recopier le texte stratégique. Cette reformulation ne crée ni ne modifie le message configuré ; son identité et ses rattachements restent ceux retournés par ComInTime.

Pour « quel message utiliser ? », rechercher les messages configurés correspondant à l’objectif et à la cible, puis présenter le message retenu avec ces rattachements. Pour « rédige une publication à partir de ce message », identifier le message configuré avant de rédiger le contenu. Ne pas répondre à ces demandes par un slogan inventé présenté comme un message ComInTime.

## Priorité donnée à l’utilisateur

Traiter les éléments explicitement demandés comme des contraintes. Si l’utilisateur demande un post Instagram sur un sujet précis, ne pas remplacer Instagram ou le sujet pour optimiser la stratégie. Utiliser les autres dimensions stratégiques afin de rendre ce post plus cohérent.

Lorsque la demande est ouverte, utiliser ComInTime pour proposer l’orientation la plus pertinente. Lorsque la demande est précise, utiliser ComInTime pour enrichir le texte et compléter sa caractérisation.

## Analyse mensuelle de la diversité

Raisonner sur le mois de la date de publication envisagée et sur le média choisi. Inclure dans l’analyse les publications déjà publiées, planifiées et programmées afin de ne pas créer artificiellement une surreprésentation future.

Pour départager plusieurs orientations compatibles avec l’idée :

1. respecter le rythme et la priorité du média ;
2. favoriser les objectifs prioritaires encore insuffisamment couverts sur ce média pendant le mois ;
3. favoriser les cibles prioritaires encore insuffisamment sollicitées ;
4. rechercher le message configuré pour le couple objectif–cible ;
5. diversifier les thématiques et sous-thématiques sans choisir un sujet artificiel ;
6. vérifier la cohérence globale avec la présentation de l’entreprise et la ligne éditoriale du média.

Les priorités et quotas servent au classement des possibilités, pas à l’interdiction d’un contenu. Si l’orientation la mieux classée dénature l’idée, choisir la possibilité compatible suivante. Si aucune ne convient, respecter l’idée et signaler sobrement l’écart éventuel.

## Déduction sans tunnel

Déduire automatiquement les dimensions dont la confiance est suffisante :

- confiance forte : renseigner directement la valeur ;
- confiance moyenne sans incidence forte sur le contenu : choisir la meilleure valeur et la montrer comme modifiable ;
- ambiguïté qui modifierait substantiellement le texte ou empêcherait la publication : poser une seule question ciblée.

Si les données confirment qu’aucun message n’est configuré pour l’objectif et la cible retenus, une demande de rédaction libre peut être satisfaite à partir de ces deux éléments : indiquer « aucun message ComInTime configuré pour ce couple » sans baptiser l’idée produite « message ». Si l’utilisateur demande précisément d’utiliser un message existant non identifié, le résoudre avant de rédiger à partir de lui.

Si les messages ne sont pas retournés par le contexte de publication, compléter avec `get-communication-audit-context` lorsqu’il est disponible : sa liste `messages` fournit `id`, `text`, `goalId` et `targetId`. Si cette lecture est impossible, dire que le message configuré n’est pas accessible, pas qu’il n’existe pas. Ne pas supposer qu’un couple objectif–cible possède un message unique sans examiner les données.

L’enregistrement du texte d’une publication et son association au message configuré sont deux opérations distinctes. Ne pas inventer un paramètre d’outil ni annoncer un rattachement que la réponse ComInTime ne confirme pas.

## Rédaction

Produire un contenu naturel, autonome et adapté au média. Appliquer les contraintes éditoriales du support et utiliser le contexte de l’entreprise uniquement lorsqu’il est pertinent pour le sujet. Ne jamais mentionner littéralement le nom du persona ni ses informations personnelles dans le post : adapter plutôt le vocabulaire, l’angle, les bénéfices et le niveau de détail à cette cible.

Éviter les affirmations non présentes dans le contexte ou dans la demande. Lorsque le média social n’accepte pas de mise en forme HTML, livrer du texte brut adapté à la plateforme.

## Ligne éditoriale : contraintes de rédaction et de modification

Avant de rédiger ou de retoucher un texte, identifier le support retenu dans `get-post-context` ou `list-supports` et lire ses règles. Réutiliser le contexte déjà chargé lorsqu’il correspond au même dossier et au même support ; le recharger si le média change ou si une modification de configuration est signalée. Ne pas prendre les règles d’un autre média ni le texte existant comme référence à la place de la configuration.

| Champ MCP | Application dans le texte |
|---|---|
| `do` | Appliquer chaque consigne pertinente : vocabulaire, structure, angle, éléments attendus. Ne pas inventer un fait pour satisfaire une consigne. |
| `dont` | Écarter les formulations, promesses, sujets ou procédés interdits. Ne pas les réintroduire dans l’accroche, les hashtags, la signature ou l’appel à l’action. |
| `postSize` | Respecter la taille et l’unité indiquées. Pour une borne numérique, mesurer le texte final, signature et hashtags inclus sauf périmètre explicitement différent. Une indication qualitative (« court ») n’autorise pas à inventer une limite chiffrée. |
| `tones` | Conserver les tons configurés, y compris lors d’une demande de reformulation plus attractive. |
| `tvDistinction` | `TU` signifie tutoiement ; `VOS` signifie vouvoiement. Appliquer ce choix aux adresses au lecteur et aux appels à l’action. |
| `personalPronoun` | Respecter le pronom configuré. « Je », « Nous » ou « On » déterminent la voix de l’émetteur ; ils ne déterminent pas le tutoiement/vouvoiement de l’audience. Les valeurs « Tu » ou « Vous » existent aussi : les interpréter avec `tvDistinction` et les autres consignes, sans inventer une voix de marque. |
| `signature` | Inclure la signature configurée dans le texte final, sans doublon, sauf condition d’application définie dans la configuration ou dérogation explicite de l’utilisateur. La préserver lors des retouches et l’intégrer à la vérification de longueur ; ne pas la supprimer silencieusement pour raccourcir le post. |

Ces règles éditoriales sont des contraintes de composition, pas de simples critères de classement comme les priorités et quotas. Une demande vague telle que « rends-le plus percutant » ne constitue pas une dérogation aux `dont`, au ton, à la taille ou aux pronoms.

Une dérogation explicitement demandée par l’utilisateur reste prioritaire pour le texte concerné : signaler brièvement l’écart utile, sans modifier la configuration du média ni redemander une autorisation déjà donnée. Si des consignes se contredisent et que l’intention ne permet pas de trancher, poser une question ciblée seulement si cela empêche de rédiger correctement.

Un champ vide n’impose aucune règle. Un champ absent de la réponse n’est pas la preuve que rien n’est configuré : tenter la lecture complémentaire disponible si nécessaire, puis signaler la limite utile sans inventer la règle. Une clé technique de traduction dans `postSize` n’est pas une limite numérique exploitable. Ne pas annoncer une conformité de longueur mesurée sans avoir effectué le comptage.

### Vérification avant livraison

Relire la version finale contre les `do` et `dont`, la taille, le ton, l’adresse au lecteur, le pronom et la signature. Corriger les écarts avant de présenter le texte ou de l’envoyer à `create-post` / `update-post`. Cette vérification porte aussi sur les retouches, raccourcissements et adaptations à un autre média ; elle ne nécessite pas d’afficher une checklist à l’utilisateur.

Respecter le périmètre de l’édition : si la demande porte uniquement sur une date, un statut ou l’enregistrement mot pour mot d’un texte, ne pas réécrire le contenu silencieusement. Signaler un écart éditorial pertinent sans transformer cette action en refonte du texte. La relecture du LLM ne remplace pas les contrôles techniques de publication et n’est pas une validation automatique du serveur.

## Caractérisation compacte

Après le contenu, présenter seulement les éléments utiles, par exemple :

> Instagram · Objectif : développer la notoriété · Cible : futurs clients · Thématique : vie de l’entreprise / événements

Ajouter le message, la date ou le statut uniquement lorsqu’ils facilitent la vérification ou l’action suivante. L’utilisateur doit pouvoir corriger un choix en une phrase.

## Associer le message à la publication enregistrée

Après avoir arrêté l’objectif et la cible, lire `messages` dans `get-post-context`. Filtrer sur les deux identifiants, puis évaluer la pertinence du texte stratégique pour le post. Choisir un message adapté parmi ce couple uniquement ; ne pas choisir automatiquement le premier ni forcer un message sans rapport parce qu’il est le seul disponible.

Transmettre le `messageId` retenu à `create-post` ou `update-post`. Vérifier dans `post.message` de la réponse l’association effectivement enregistrée et la restituer avec l’objectif et la cible. Une mention du message dans le texte ou la caractérisation conversationnelle ne suffit pas à le sauvegarder.

Si aucun message du couple ne convient, enregistrer sans message lorsque l’enregistrement est demandé et expliquer : « Aucun message configuré ne correspond suffisamment à ce post pour cet objectif et cette cible. Je vous recommande d’en ajouter un dans l’application web ComInTime. » Proposer alors une formulation stratégique, identifiée comme **proposition non enregistrée**, avec l’objectif et la cible concernés. Ne pas créer ou modifier la stratégie depuis le MCP ; ne pas inventer de lien vers l’application. Une collecte de contexte en échec ne permet pas d’affirmer qu’aucun message pertinent n’existe.

Lors d’une modification du contenu, réévaluer la pertinence du message. Si l’objectif ou la cible change, reconsulter les messages du couple final ; remplacer l’association via `messageId`, ou utiliser `clear: ["message"]` si aucun ne convient, puis fournir la recommandation ci-dessus. Le serveur refuse une association incompatible ; il ne choisit pas la pertinence sémantique à la place du LLM. Pour une modification de métadonnées seulement, conserver le message existant si le couple reste inchangé.
