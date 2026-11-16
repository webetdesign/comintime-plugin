---
description: Rédige un brouillon de post ComInTime (sans le publier) à partir d'un brief.
argument-hint: <dossier> : <brief de rédaction>
allowed-tools: mcp__comintime__list-folders, mcp__comintime__get-post-context, mcp__comintime__create-post, mcp__comintime__attach-media
---

Brief : **$ARGUMENTS**

Découpe `$ARGUMENTS` en `<dossier>` (avant le `:`) et `<brief>` (après). Si le
dossier est absent ou ambigu, appelle `mcp__comintime__list-folders` et demande
lequel utiliser avant de continuer.

1. Appelle `mcp__comintime__get-post-context` pour ce dossier afin de récupérer
   les supports, cibles, objectifs, formats, thèmes et langues disponibles.
2. Propose à l'utilisateur : support + format + cible + objectif + thèmes + langue
   les plus cohérents avec le brief, en listant les ids retenus. **Attends sa
   validation.**
3. Rédige le texte final du post (titre + contenu + accroche courte) dans la
   langue choisie, en respectant le brief.
4. Appelle `mcp__comintime__create-post` avec le contenu rédigé et les ids validés.
   Ne renseigne PAS de date de publication et n'appelle jamais `publish-post` :
   cette commande produit un brouillon.
5. Si l'utilisateur a **joint une image** au message, ajoute-la au post créé avec
   `mcp__comintime__attach-media` (`imageBase64` + `mimeType`).
6. Renvoie l'id du post créé et un lien/rappel pour le relire dans ComInTime.

Pour ajouter un visuel plus tard : `/comintime:visual <id>`. Pour programmer ou
publier : `/comintime:publish <id>`.
