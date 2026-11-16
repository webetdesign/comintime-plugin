---
description: Montre la ou les prochaines publications ComInTime à venir.
argument-hint: [dossier] [· statut]
allowed-tools: mcp__comintime__next-publication, mcp__comintime__list-folders
---

Cible : **$ARGUMENTS** (dossier et/ou statut ; peut être vide).

Appelle `mcp__comintime__next-publication` en passant le dossier dans `folder` et,
si l'utilisateur a précisé un statut, dans `status`. Présente la prochaine
publication avec sa date, son titre, son support, son statut et le dossier.
Indique le temps restant avant la date prévue.
