---
name: comintime-publication
description: Rédiger, modifier, caractériser, enregistrer, faire valider ou programmer une publication avec le contexte d’entreprise, la stratégie éditoriale et l’historique mensuel de ComInTime. Utiliser pour transformer une idée en contenu destiné à un média configuré dans ComInTime, sans imposer à l’utilisateur un tunnel stratégique.
---

# Publication ComInTime

## Finalité

Aider l’utilisateur à publier simplement. Exploiter la stratégie ComInTime en arrière-plan pour améliorer la pertinence et la diversité du contenu, sans transformer la conversation en formulaire. L’intention explicite de l’utilisateur reste prioritaire.

Ce skill définit la méthode conversationnelle et l'expérience utilisateur. Il
ne déclare aucune connexion MCP et ne porte pas l'authentification technique.

Lire [references/strategie-et-redaction.md](references/strategie-et-redaction.md) avant de choisir l’orientation et de rédiger. Lire [references/cycle-de-publication.md](references/cycle-de-publication.md) dès que la demande implique un enregistrement, une validation, une planification ou une publication. Le document [references/contrat-integration.md](references/contrat-integration.md) décrit les actions que l’intégration ComInTime doit exposer ; il est destiné à l’implémentation du plugin ou de l’agent.

## Sens du terme « message »

Dans le contexte ComInTime, **« message » désigne le message configuré dans la stratégie**, rattaché à la combinaison d’un objectif et d’une cible : ce que la structure souhaite faire comprendre à cette cible pour atteindre cet objectif. Cette définition s’applique aussi lorsque l’utilisateur dit « ce message », « quel message ? » ou « nos messages ».

Ne pas remplacer cet objet stratégique par l’idée du post, son angle, son texte ou le sens que le LLM déduit du contenu. Employer « idée », « angle », « texte de la publication » ou « promesse perçue » pour ces notions. Une référence explicitement extérieure à la stratégie, telle qu’un message d’erreur ou un message privé, conserve naturellement son sens explicite.

Résoudre le message à partir des données ComInTime : identifiant, texte configuré, objectif et cible associés. Ne jamais inventer un identifiant ni déclarer qu’un message est configuré ou associé à une publication sur la seule base d’une ressemblance sémantique. Si plusieurs messages correspondent et que le contexte ne permet pas de choisir, poser une question ciblée ; s’il manque des données, distinguer message non accessible et absence de message confirmée.

## Principes d’expérience utilisateur

- Commencer par répondre à l’idée ou à la demande de publication, pas par expliquer la stratégie.
- Déduire silencieusement le média, l’objectif, la cible, le message et les thématiques quand le contexte le permet.
- Interpréter le mot « message », lorsqu’il désigne un élément stratégique ou de caractérisation, comme le message configuré dans ComInTime pour le couple objectif–cible, et non comme l’idée, le sujet ou le sens général du contenu. Ne retenir un autre sens que si l’utilisateur le précise explicitement.
- Ne poser qu’une question courte lorsqu’une information manque réellement pour produire le contenu ou exécuter l’action demandée.
- Ne jamais demander à l’utilisateur de reconstituer des informations déjà présentes dans ComInTime.
- Présenter la caractérisation sous une forme compacte et facilement corrigeable.
- Accepter toute correction ou préférence explicite de l’utilisateur, même si une autre orientation serait mieux classée par la stratégie.
- Signaler une recommandation stratégique comme un conseil, jamais comme un obstacle à la rédaction.

## Déroulement

1. Identifier l’intention : proposer un texte, enregistrer une idée, enregistrer une publication avancée, soumettre, valider, planifier ou publier.
2. Identifier le dossier ComInTime. Si plusieurs dossiers sont possibles et qu’aucun ne peut être déduit, demander lequel utiliser.
3. Charger en une fois le contexte utile : présentation de l’entreprise, stratégie, médias configurés, lignes éditoriales, connexions, droits et activité du mois concerné.
4. Respecter les éléments imposés par l’utilisateur. Pour les éléments libres, choisir une combinaison cohérente et diversifiante selon `strategie-et-redaction.md`.
5. Après choix de l’objectif et de la cible, examiner les messages configurés pour ce couple et retenir celui qui convient au post. Lors de l’enregistrement, transmettre son `messageId` et vérifier `post.message` dans la réponse. Si aucun ne convient, le signaler et proposer un message à ajouter dans l’application web, sans le créer ni forcer une association.
6. Rédiger ou modifier pour le média retenu en respectant ses `do` et `dont`, sa taille (`postSize`), ses tons (`tones`), son tutoiement/vouvoiement (`tvDistinction`), son pronom (`personalPronoun`) et sa signature. Appliquer la vérification éditoriale de `strategie-et-redaction.md` avant de montrer ou d’enregistrer le texte final. Une simple reformulation ou un changement de média nécessite aussi cette vérification.
7. Afficher le texte puis une caractérisation compacte : média, objectif, cible, message, thématique et sous-thématique, date et statut envisagés quand ils sont pertinents.
8. Si l’utilisateur demande seulement un texte, s’arrêter là. Ne pas enregistrer ni programmer sans demande ou confirmation explicite.
9. Si une action ComInTime est demandée, appliquer `cycle-de-publication.md`, laisser ComInTime contrôler les droits et restituer clairement le résultat réel.

## Garde-fous

- Ne pas inventer de configuration, de connexion, de droit, d’objectif, de cible, de message ou de thématique ComInTime.
- Ne pas confondre le message ComInTime avec le texte de la publication, l’idée de l’utilisateur ou l’intention générale de son discours.
- Ne pas promettre une publication automatique avant le contrôle du média, du compte, du contenu, de la date, des droits et de la validation.
- Ne pas contourner les transitions de statut ni les validations imposées par ComInTime.
- Ne pas publier vers un média absent du dossier.
- Ne pas recopier mécaniquement le message de référence : préserver son intention tout en adaptant la formulation.
- Ne pas forcer un rapprochement stratégique qui dénature le sujet de l’utilisateur.
- Demander une confirmation juste avant la programmation ou la publication si elle n’a pas déjà été donnée sans ambiguïté dans la demande courante.

## Forme de la réponse

Livrer d’abord le contenu utile. Ajouter ensuite, sans jargon interne, les choix déduits et l’état de l’action. En cas de blocage, expliquer uniquement l’élément manquant et proposer l’étape la plus simple pour continuer.
