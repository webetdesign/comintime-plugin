---
description: "Affiche le profil de la structure (entreprise, association…) d'un dossier ComInTime."
argument-hint: "<dossier>"
---

Dossier : **$ARGUMENTS**

Si le dossier est absent ou ambigu, appelle `mcp__plugin_comintime-mcp_comintime__list-folders` et
demande lequel utiliser.

Appelle `mcp__plugin_comintime-mcp_comintime__get-folder-profile` pour ce dossier, puis présente :

1. **Identité** : nom, type de structure, secteur, effectif, site web, zone de
   chalandise, clientèle.
2. **Présentation** : description, activités, histoire.
3. **Positionnement** : valeurs, vision, avantages, certifications, projets, équipe.

Signale les rubriques vides (« non renseigné »). Ce profil sert de base pour
rédiger des contenus fidèles au ton et au positionnement de la structure.
