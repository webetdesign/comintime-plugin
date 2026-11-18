---
description: "Programme ou publie un post ComInTime existant, avec dry-run obligatoire."
argument-hint: "<id du post> [· \"now\" | date ISO]"
---

Demande : **$ARGUMENTS**

1. Identifie l'id du post et le mode voulu : `now` (immédiat) ou `schedule` avec
   une date ISO future (`YYYY-MM-DDTHH:MM`).
2. Appelle `mcp__plugin_comintime-mcp_comintime__publish-post` **en dry-run** (`confirm` = false / non
   fourni) pour obtenir le récapitulatif : `channel` (type + compte), date
   effective, `contentPreview`, `mediaCount`, `viability` (avertissements réseau)
   et `blockers`.
3. Si `blockers` n'est pas vide, l'outil refusera : explique les raisons.
   - Si un blocage porte sur un **visuel manquant** (Instagram), demande une image
     à l'utilisateur et ajoute-la avec `/comintime:visual` avant de réessayer.
   - Si le contenu est trop long, corrige-le avec `/comintime:draft` ou
     `update-post` puis relance le dry-run.
4. Affiche le récapitulatif à l'utilisateur et demande une confirmation explicite.
5. Seulement après un « oui » clair, rappelle `mcp__plugin_comintime-mcp_comintime__publish-post` avec
   `confirm: true` et les mêmes paramètres.
6. Confirme le résultat (statut final + date programmée/publiée + `messengerId`).

N'appelle jamais `publish-post` avec `confirm: true` sans avoir montré le dry-run
et obtenu l'accord dans ce même échange.
