#!/usr/bin/env python3
"""Génère le ZIP de soumission à l'annuaire OpenAI (ChatGPT / Codex).

Le dépôt garde la fiche Codex en français, pour les installations via le
marketplace. L'annuaire OpenAI exige une fiche de base en anglais : ce script
copie le plugin, remplace les champs de fiche par ceux de openai/listing.en.json
et place la version française dans
extensions.com.openai.publication.translations.fr-FR.

Le dépôt référence aussi l'app ChatGPT de l'espace W&D (.app.json) pour que le
plugin fonctionne sur ChatGPT web via le marketplace d'organisation. L'annuaire
refuse un ZIP qui référence une app : le script retire .app.json et déclare à la
place le serveur MCP de .mcp.json. Il ajoute enfin les cas de test de revue
(openai/review.json), refusés par l'import en marketplace d'organisation tant
que le manifeste ne déclare pas exactement un serveur MCP.

Usage : python3 scripts/build-openai-zip.py  ->  dist/comintime-<version>.zip
"""
import json
import pathlib
import shutil
import sys
import tempfile
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "comintime-mcp"
LISTING_EN = ROOT / "openai" / "listing.en.json"
REVIEW = ROOT / "openai" / "review.json"
SUBTITLE_MAX = 30
DESCRIPTION_MAX = 4000


def main() -> int:
    manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text())
    english = json.loads(LISTING_EN.read_text())
    interface = manifest["interface"]

    subtitle_fr = interface["shortDescription"]
    description_fr = interface["longDescription"]
    for label, text, limit in (
        ("sous-titre FR", subtitle_fr, SUBTITLE_MAX),
        ("sous-titre EN", english["interface"]["shortDescription"], SUBTITLE_MAX),
        ("description FR", description_fr, DESCRIPTION_MAX),
        ("description EN", english["interface"]["longDescription"], DESCRIPTION_MAX),
    ):
        if len(text) > limit:
            print(f"{label} trop long : {len(text)} > {limit} caractères", file=sys.stderr)
            return 1

    review = json.loads(REVIEW.read_text())["review"]
    manifest.setdefault("extensions", {}).setdefault("com.openai", {})["review"] = review
    manifest.pop("apps", None)
    manifest["mcpServers"] = "./.mcp.json"
    manifest["description"] = english["description"]
    interface.update(english["interface"])
    publication = manifest["extensions"]["com.openai"]["publication"]
    publication["translations"] = {
        "fr-FR": {"subtitle": subtitle_fr, "description": description_fr},
    }

    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    target = dist / f"comintime-{manifest['version']}.zip"

    with tempfile.TemporaryDirectory() as tmp:
        staging = pathlib.Path(tmp) / "comintime-mcp"
        shutil.copytree(PLUGIN, staging, ignore=shutil.ignore_patterns(".DS_Store", ".app.json"))
        (staging / ".codex-plugin" / "plugin.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
        )
        with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(staging.rglob("*")):
                archive.write(path, path.relative_to(staging).as_posix())

    print(target.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
