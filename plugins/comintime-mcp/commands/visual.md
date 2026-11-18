---
description: Ajoute ou retire un visuel sur un post ComInTime, puis recalcule sa conformité réseau.
argument-hint: <id du post> [· remove <id média>]
---

Demande : **$ARGUMENTS**

Identifie l'id du post. Deux cas :

## Ajouter un visuel

- **Si l'utilisateur a joint une image au message** : appelle
  `mcp__plugin_comintime-mcp_comintime__attach-media` avec `subjectId`, `imageBase64` (le contenu de
  l'image encodé en base64) et `mimeType` (`image/png`, `image/jpeg`…).
- **Si l'utilisateur a donné une URL** (ou un data URI) : appelle
  `mcp__plugin_comintime-mcp_comintime__attach-media` avec `subjectId` et `imageUrl`.

Contraintes : image valide, 10 Mo max. Un post Instagram exige au moins un visuel.

## Retirer un visuel

Si la demande contient `remove <id média>`, appelle
`mcp__plugin_comintime-mcp_comintime__remove-media` avec `subjectId` et `mediaId`.

## Rendu

Après l'action, présente la liste des médias du post (id, nom de fichier) et
l'état `viability` renvoyé : s'il reste des avertissements, explique lesquels et
ce qu'il manque avant de pouvoir publier.
