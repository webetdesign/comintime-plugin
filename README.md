# ComInTime — plugins pour assistants IA

Ce dépôt contient le plugin officiel [ComInTime](https://www.comintime.com/fr/)
pour Claude (Claude Code, Claude Desktop) et OpenAI (ChatGPT, Codex).

- Plugin : [`plugins/comintime-mcp`](./plugins/comintime-mcp) — documentation et installation.
- Marketplace Claude : [`.claude-plugin/marketplace.json`](./.claude-plugin/marketplace.json)
- Marketplace OpenAI : [`.agents/plugins/marketplace.json`](./.agents/plugins/marketplace.json)

Installation rapide dans Claude Code :

```bash
/plugin marketplace add webetdesign/comintime-plugin
/plugin install comintime-mcp@comintime
```

## Soumission à l'annuaire OpenAI

La fiche Codex du dépôt (`.codex-plugin/plugin.json`) est en français : c'est
elle qui s'affiche quand on installe le plugin depuis ce marketplace. L'annuaire
OpenAI exige une fiche de base en anglais ; les textes anglais sont dans
[`openai/listing.en.json`](./openai/listing.en.json). Pour générer le ZIP à
déposer sur platform.openai.com/plugins :

```bash
python3 scripts/build-openai-zip.py
```

Le script produit `dist/comintime-<version>.zip` : fiche de base en anglais, et
version française reprise du manifeste dans la traduction `fr-FR`. Toute
modification des textes de la fiche se fait donc aux deux endroits.

Licence propriétaire © Web et Design — voir [LICENSE](./LICENSE).
