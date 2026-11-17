---
description: Liste les dossiers ComInTime de l'utilisateur connecté et son rôle sur chacun.
allowed-tools: mcp__plugin_comintime-mcp_comintime__list-folders
---

Appelle l'outil `mcp__plugin_comintime-mcp_comintime__list-folders` puis présente le résultat sous forme
de tableau : **Dossier**, **Id**, **Rôle**. Termine par le nombre total de dossiers.

Si l'appel renvoie une erreur d'authentification, rappelle à l'utilisateur de lancer
`/mcp` pour se connecter au serveur ComInTime.
