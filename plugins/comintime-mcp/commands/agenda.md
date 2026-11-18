---
description: Affiche l'agenda éditorial ComInTime pour une période donnée.
argument-hint: [période en langage naturel] [· dossier]
---

Période demandée : **$ARGUMENTS**
(si vide, laisse l'outil appliquer sa valeur par défaut : les 30 prochains jours.)

1. Interprète `$ARGUMENTS`. Ce qui ressemble à une période (« ce weekend »,
   « semaine prochaine », « ce mois-ci », « du 15 au 30 septembre »…) va dans le
   paramètre `period` ; un nom ou un id de dossier va dans `folder`.
2. Appelle `mcp__plugin_comintime-mcp_comintime__publications-in-period` avec ces paramètres.
3. Rends un agenda trié par date : **Date**, **Titre**, **Dossier**, **Support**,
   **Statut**. Regroupe par jour si la période dépasse une semaine.
4. Termine par un compte par statut (À publier / Programmée / Publiée…).

En cas de doute sur le dossier, appelle d'abord `mcp__plugin_comintime-mcp_comintime__list-folders`.
