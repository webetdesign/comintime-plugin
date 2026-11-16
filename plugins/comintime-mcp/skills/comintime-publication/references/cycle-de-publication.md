# Cycle de publication

## Intention et statut cible

Le niveau de maturité du contenu et la demande de l’utilisateur déterminent le statut visé. Les noms fonctionnels correspondent au cycle ComInTime :

| Situation | Statut visé |
|---|---|
| L’utilisateur conserve une idée sommaire | Idée lancée (`STATUS_NEW`) |
| Le contenu est déjà rédigé ou qualifié | À traiter (`STATUS_TO_TREAT`) |
| Le contenu doit être examiné par le responsable | À valider (`STATUS_TO_VALIDATE`) |
| Le contenu est validé mais sa diffusion n’est pas complètement définie | À planifier (`STATUS_VALIDATED`) |
| Le contenu est prêt mais ne peut pas être programmé automatiquement | À publier (`STATUS_PLANNED`) |
| Le contenu doit être diffusé automatiquement et toutes les conditions sont remplies | Programmée (`STATUS_SCHEDULED`) |

Une publication rédigée et caractérisée par l’agent est normalement au moins « À traiter ». Une demande de publication vise le résultat « Programmée », mais l’intégration doit appliquer les transitions, validations et contrôles réels de ComInTime.

## Contrôle avant action

Pour un texte rédigé ou modifié par l’agent, effectuer la vérification éditoriale décrite dans [strategie-et-redaction.md](strategie-et-redaction.md) avant enregistrement. Une modification limitée aux métadonnées ne justifie pas une réécriture du contenu.

Avant d’enregistrer, vérifier que le dossier et l’auteur sont identifiés. Avant de soumettre ou valider, vérifier les droits par une action ComInTime : ne pas les déduire du langage de l’utilisateur.

Avant de programmer, contrôler par ComInTime :

- que le média est configuré dans le dossier ;
- que le contenu respecte les contraintes de la plateforme ;
- que les champs obligatoires, dont l’objectif et la cible lorsque ComInTime les exige, sont renseignés ;
- que la date et l’heure sont définies et admissibles ;
- que le compte ou la page de diffusion est connecté et que son autorisation est valide ;
- que la validation requise a été obtenue ;
- que l’utilisateur possède les droits nécessaires.

Si la date manque dans une demande de programmation, proposer une date cohérente avec le planning et demander une confirmation courte. Ne pas ouvrir un questionnaire complet.

## Médias et diffusion

- Un média absent du dossier ne peut pas être choisi comme destination de publication.
- Un média configuré peut servir à la rédaction même si son compte n’est pas connecté.
- Facebook, Instagram, LinkedIn, Google Business Profile et tout autre réseau pris en charge ne peuvent être programmés automatiquement que si la connexion nécessaire est valide.
- Le site web peut servir de média éditorial et recevoir un contenu préparé, mais ComInTime ne le met pas directement en ligne. Conserver alors la publication dans l’état adapté à une diffusion manuelle.

La capacité du moteur de génération interne de ComInTime ne limite pas les médias que l’agent peut rédiger. Seules la configuration du dossier, les contraintes éditoriales et la capacité réelle de diffusion déterminent les actions disponibles.

## Confirmation et résultat

La demande explicite « publie », « programme » ou équivalent peut valoir intention d’agir. Montrer néanmoins le texte, la destination et la date avant l’engagement final lorsqu’ils n’ont pas déjà été confirmés ensemble dans la demande courante.

Après chaque action, annoncer le résultat retourné par ComInTime : identifiant ou lien si disponible, statut réel, média, date, prochaine validation éventuelle et raison précise d’un échec. Ne pas annoncer « programmée » lorsque le serveur a seulement enregistré « À publier ».

En cas d’échec partiel, conserver le brouillon si l’action le permet et proposer uniquement la correction nécessaire : connexion du compte, validation, date, champ manquant ou contenu trop long.
