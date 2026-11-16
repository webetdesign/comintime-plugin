# Performances sociales dans le diagnostic

Appeler `get-communication-social-statistics` avec `folder`, `from` et `to`. Il lit les statistiques enregistrées pour les pages liées aux supports visibles ; il ne déclenche aucune collecte. L’outil applique les droits du dossier. Facebook, Instagram, LinkedIn et Google My Business sont identifiés séparément.

## Interpréter la réponse

- `period` sélectionne les dates de publication. Les métriques sont les **compteurs cumulés** de ces publications à la date de leur stockage, pas les interactions survenues pendant cette période. `byPublicationMonth` compare des cohortes de publications d’âges différents, pas une évolution mensuelle de l’audience.
- `pageSnapshot` décrit le dernier instantané disponible. Sa période est inconnue : ne pas le présenter comme une mesure historique ou calculer une croissance d’abonnés.
- Pour chaque métrique, rapprocher `measuredPublications` de `publicationCount`. `null` signifie non disponible ; un zéro stocké peut provenir d’un repli du collecteur historique. Examiner `collectionLimitation` et les dates de stockage, y compris les observations non datées. Ne pas affirmer qu’une collecte a réussi à partir de `updatedAt`.
- Respecter `visibilityDefinition` : le champ historique regroupe selon le réseau portée, impressions ou vues, parfois sans conserver le choix exact. Ne pas additionner les réseaux, présenter une audience unique totale ou classer les réseaux à partir de ces chiffres hétérogènes.
- Aucun taux global n’est fourni : les dénominateurs et définitions d’engagement ne sont pas harmonisés. Ne pas additionner ni moyenner les taux historiques.
- Google My Business : la collecte actuelle ne remonte pas ses performances. Appels, demandes d’itinéraire et clics vers le site sont **non mesurables**, jamais nuls par défaut. Les abonnés ne sont pas un substitut aux actions locales.

## Relier les résultats à la stratégie

Distinguer la régularité éditoriale, les résultats observés et l’atteinte des objectifs. Une cadence respectée ne prouve pas l’efficacité ; une interaction ne prouve pas une vente. Pour la visibilité, examiner le compteur propre au réseau ; pour l’engagement, les interactions couvertes ; pour le trafic, les clics disponibles. Sans attribution ou conversion mesurée, présenter l’impact commercial comme inconnu.

Restituer les résultats sociaux utiles avec réseau, période, couverture et limite, puis des recommandations reliées aux objectifs du dossier. Séparer constats et hypothèses ; privilégier les essais éditoriaux vérifiables. Si les données manquent, poursuivre le diagnostic stratégique et éditorial possible en nommant précisément les performances non mesurables. Ne pas modifier la stratégie pendant l’analyse.
