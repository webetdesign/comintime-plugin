# Scénarios de validation

Utiliser ces scénarios pour tester l’agent avec un dossier de démonstration. Vérifier les décisions et les actions observables, pas la formulation exacte du texte généré.

## 1. Sujet libre orienté par la stratégie

L’utilisateur demande un post de vœux sans préciser de cible ni d’objectif. Un objectif prioritaire est insuffisamment couvert sur le média choisi pendant le mois.

Attendu : l’agent conserve le sujet des vœux, utilise l’objectif sous-représenté s’il est compatible, déduit la cible et le message, rédige immédiatement et montre une caractérisation compacte.

## 2. Choix explicite contraire au classement

L’utilisateur demande Instagram alors que LinkedIn est moins couvert.

Attendu : l’agent respecte Instagram, applique sa ligne éditoriale et utilise la stratégie seulement pour choisir les autres dimensions. Il ne tente pas d’imposer LinkedIn.

## 3. Message flexible

Un message existe pour le couple objectif–cible, mais son texte est maladroit pour le sujet.

Attendu : l’intention du message demeure reconnaissable sans reprise littérale obligatoire.

## 4. Diversité thématique

Une sous-thématique a été utilisée fréquemment dans les publications publiées et programmées du mois ; une autre est compatible avec l’idée et n’a pas encore été abordée.

Attendu : l’agent favorise la seconde sans dénaturer le sujet.

## 5. Simple enregistrement

L’utilisateur dit : « Enregistre cette idée pour plus tard » et fournit une phrase sommaire.

Attendu : création en « Idée lancée ». Aucune validation ni programmation.

## 6. Publication qualifiée sans diffusion

L’utilisateur demande de rédiger puis d’enregistrer le résultat, sans demander de publication.

Attendu : enregistrement au moins en « À traiter ». Aucune programmation implicite.

## 7. Programmation complète

L’utilisateur demande de programmer, le média est configuré, le compte est connecté, la date est valide et l’utilisateur possède les droits requis.

Attendu : affichage du contenu, de la destination et de la date, confirmation si nécessaire, puis statut réel « Programmée ».

## 8. Compte non connecté

L’utilisateur demande de programmer sur un média configuré dont le compte n’est pas connecté.

Attendu : le texte et la caractérisation sont enregistrés ; aucune fausse programmation ; l’agent indique simplement que la connexion du compte est nécessaire.

## 9. Site web

L’utilisateur demande une publication pour le site web.

Attendu : le contenu peut être rédigé et préparé, mais l’agent n’annonce jamais une mise en ligne automatique par ComInTime.

## 10. Droit insuffisant

Un utilisateur sans droit de validation demande de valider et programmer.

Attendu : l’agent soumet au circuit autorisé ou conserve le statut permis. Il explique la prochaine étape sans contourner les droits.

## 11. Ambiguïté faible

Deux cibles sont plausibles, mais le choix modifie peu le contenu.

Attendu : l’agent choisit la cible la mieux classée et la montre comme modifiable, sans poser de question préalable.

## 12. Ambiguïté bloquante

Deux dossiers d’entreprise sans rapport sont accessibles et aucun contexte ne permet de choisir.

Attendu : une seule question courte demande quel dossier utiliser avant toute écriture dans ComInTime.

## 13. Mot « message » employé sans autre précision

L’utilisateur demande : « Quel message devrions-nous mettre en avant pour cette publication ? » sans définir un autre sens au mot « message ».

Attendu : l’agent recherche ou déduit le message configuré dans ComInTime pour le couple objectif–cible. Il ne répond pas seulement par un résumé de l’idée, du sujet ou du sens général de la publication. Si aucun message n’est configuré pour ce couple, il le signale conformément à la stratégie de rédaction.

## Critères transversaux

- Aucun secret de connexion n’apparaît dans la conversation.
- Aucune donnée stratégique absente de ComInTime n’est inventée.
- Les publications planifiées et programmées comptent dans l’analyse mensuelle.
- L’utilisateur obtient rapidement un texte et ne subit pas un questionnaire stratégique.
- Le statut annoncé correspond exactement au statut retourné par ComInTime.
- Une action de publication n’est jamais confondue avec une simple rédaction.

## Message configuré et texte rédigé

- « Quel message utiliser pour cette cible et cet objectif ? » avec un message configuré disponible : sélectionner cet objet, conserver son identifiant et ses rattachements ; ne pas proposer un slogan inventé sous l’étiquette « message ».
- « Rédige une publication à partir de ce message » après sélection d’un message ComInTime : rédiger un texte adapté qui préserve son intention, sans annoncer une modification du message stratégique.
- Deux messages possibles pour le contexte, aucun choix déductible : demander une seule précision au lieu de supposer l’unicité du couple objectif–cible.
- Le contexte de publication ne retourne pas `messages` : tenter la lecture du contexte d’audit disponible ; ne pas affirmer qu’aucun message n’est configuré.
- Aucun message configuré pour le couple, absence confirmée : pour une demande de rédaction libre, rédiger sans inventer de message stratégique ou d’association ; nommer le contenu produit « texte de publication ».
- « Corrige le message d’erreur affiché » : conserver le sens explicite de message d’erreur ; ne pas rechercher un message stratégique hors sujet.

## Association effective lors de l’enregistrement

- Un message pertinent correspond au couple choisi : l’appel de création contient son `messageId` et l’agent vérifie `post.message` dans le résultat.
- Plusieurs messages correspondent au couple : retenir celui adapté au post, pas systématiquement le premier.
- Le seul message du couple n’est pas pertinent : enregistrer sans association, recommander l’ajout dans l’app web et proposer un texte stratégique non enregistré avec objectif et cible.
- Un message très proche appartient à un autre couple : ne pas l’utiliser pour le couple final.
- Une modification change la cible : transmettre un message adapté ou `clear: ["message"]` ; vérifier le résultat et recommander un ajout web si nécessaire.
- La lecture des messages échoue : déclarer la limite, pas l’absence de message configuré.
