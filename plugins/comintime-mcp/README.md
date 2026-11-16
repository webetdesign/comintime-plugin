# ComInTime pour Claude et ChatGPT

Connectez votre assistant IA à [ComInTime](https://www.comintime.com/fr/) pour
consulter votre agenda éditorial, rédiger des brouillons cohérents avec votre
stratégie, ajouter des visuels, programmer vos publications et analyser votre
communication, directement depuis la conversation.

Le plugin agit **toujours au nom de l'utilisateur connecté** (OAuth 2.1) et selon
ses rôles sur chaque dossier. Aucune publication n'est déclenchée sans
confirmation explicite.

## Prérequis

- Un compte ComInTime actif.
- Claude Code / Claude Desktop, ou ChatGPT / Codex.

## Installation

### Claude

Depuis l'annuaire de plugins Claude, recherchez **ComInTime**, ou ajoutez le
marketplace manuellement :

```bash
/plugin marketplace add webetdesign/comintime-plugin
/plugin install comintime-mcp@comintime
```

Lancez ensuite `/mcp` et connectez-vous avec votre compte ComInTime. Testez avec
`/comintime:folders`.

### ChatGPT et Codex

Installez l'app **ComInTime** depuis l'annuaire ChatGPT, puis terminez la
connexion OAuth demandée. Dans Codex, vous pouvez aussi ajouter le marketplace :

```bash
codex plugin marketplace add webetdesign/comintime-plugin
```

## Fonctionnalités

| Élément | Description |
|---|---|
| `/comintime:folders` | Liste vos dossiers et votre rôle sur chacun. |
| `/comintime:company <dossier>` | Profil de la structure du dossier (identité, description, valeurs…). |
| `/comintime:agenda [période]` | Agenda éditorial sur une période en langage naturel. |
| `/comintime:next [dossier]` | Prochaine publication à venir. |
| `/comintime:draft <dossier> : <brief>` | Rédige un brouillon cohérent avec le contexte du dossier (ne publie pas). |
| `/comintime:visual <id> [· remove <idMédia>]` | Ajoute ou retire un visuel sur un post. |
| `/comintime:publish <id> [· now\|date]` | Programme ou publie un post, avec simulation obligatoire avant confirmation. |
| Skill `comintime-publication` | Guide la rédaction et la programmation d'une publication. |
| Skill `comintime-analyse-communication` | Diagnostic de stratégie, d'activité et de performances sociales. |
| Sous-agent `community-manager` | Planifie, rédige et prépare les publications. Ne publie jamais sans validation. |

Les commandes slash et le sous-agent sont disponibles dans Claude Code. Les
skills et les outils MCP sont disponibles partout.

### Outils MCP

- **Dossier** : `list-folders`, `get-folder-profile`.
- **Contexte éditorial** : `get-post-context`, `list-targets`, `list-goals`,
  `list-supports`, `list-themes`, `list-folder-media`.
- **Agenda** : `next-publication`, `last-publication`, `publications-in-period`.
- **Rédaction** : `create-post`, `update-post`, `attach-media`, `remove-media`.
- **Publication** : `publish-post`.
- **Analyse** : `get-communication-audit-context`,
  `get-communication-activity-statistics`,
  `list-publications-for-communication-analysis`,
  `get-communication-social-statistics`.

## Sécurité et données

- `create-post` et `update-post` ne produisent que des **brouillons**.
- `publish-post` est le **seul outil sortant** : simulation par défaut,
  `confirm: true` requis, refus si le post n'est pas conforme au réseau, rôle
  « responsable » exigé.
- Le jeton OAuth ne donne accès qu'aux données de l'utilisateur qui l'a autorisé.

Politique de confidentialité :
<https://www.comintime.com/fr/politique-de-confidentialite>
Conditions générales d'utilisation :
<https://www.comintime.com/fr/conditions-generales-d-utilisation>

## Support

Web et Design — <contact@webetdesign.com>

## Licence

Logiciel propriétaire © Web et Design. Voir [LICENSE](./LICENSE).
