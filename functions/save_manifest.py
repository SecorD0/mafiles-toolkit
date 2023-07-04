import json
from typing import Dict, Any

from data import config


def save_manifest(manifest: Dict[str, Any]):
    with open(file=config.PROCESSED_MANIFEST_FILE, mode='w') as f:
        json.dump(manifest, f, ensure_ascii=False, separators=(',', ':'))
