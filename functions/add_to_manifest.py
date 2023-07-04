import os

from pretty_utils.miscellaneous.files import read_json

from data import config
from functions.get_mafile_dict import get_mafile_dicts
from functions.save_manifest import save_manifest
from utils.print_to_log import print_to_log


def add_to_manifest():
    if os.path.exists(config.MANIFEST_FILE):
        manifest = read_json(path=config.MANIFEST_FILE)

    else:
        manifest = {
            'encrypted': False,
            'first_run': False,
            'entries': [],
            'periodic_checking': False,
            'periodic_checking_interval': 10,
            'periodic_checking_checkall': False,
            'auto_confirm_market_transactions': False,
            'auto_confirm_trades': False
        }

    imported = [str(entry['steamid']) for entry in manifest['entries']]
    added = 0
    _, s64_dict = get_mafile_dicts()
    for s64, mafile_path in s64_dict.items():
        try:
            if s64 not in imported:
                manifest['entries'].append({
                    'encryption_iv': None,
                    'encryption_salt': None,
                    'filename': f'{s64}.maFile',
                    'steamid': int(s64)
                })
                added += 1
                print_to_log(text=f'Account was added to the manifest.', status='[V]', login_or_s64=s64)

            else:
                print_to_log(text=f'Account already on the manifest.', status='[V]', login_or_s64=s64)

            new_path = os.path.join(config.PROCESSED_DIR, f'{s64}.maFile')
            os.rename(mafile_path, new_path)

        except BaseException as e:
            print_to_log(
                text=f'Failed to add the {mafile_path} maFile to the manifest: {e}', status='[X]', login_or_s64=s64
            )

    print_to_log(text=f'{added}/{len(s64_dict)} missing maFiles were added to the manifest.', status='[V]')
    save_manifest(manifest=manifest)
