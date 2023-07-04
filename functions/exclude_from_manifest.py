import os

from pretty_utils.miscellaneous.files import read_json

from data import config
from functions.get_mafile_dict import get_mafile_dicts
from functions.save_manifest import save_manifest
from utils.print_to_log import print_to_log


def exclude_from_manifest():
    if os.path.exists(config.MANIFEST_FILE):
        manifest = read_json(path=config.MANIFEST_FILE)

    else:
        print(
            f'\n{config.RED}[X] There is no the {config.MANIFEST_FILE} in the '
            f'{config.MAFILES_DIR} directory!{config.RESET_ALL}'
        )
        return

    imported = {str(entry['steamid']): entry for entry in manifest['entries']}
    _, s64_dict = get_mafile_dicts()
    for s64, entry in imported.items():
        try:
            if s64 in s64_dict:
                new_path = os.path.join(config.PROCESSED_DIR, f'{s64}.maFile')
                os.rename(s64_dict[s64], new_path)
                print_to_log(text=f'Account on the manifest.', status='[V]', login_or_s64=s64)

            else:
                manifest['entries'].remove(entry)
                print_to_log(text=f'Account was excluded from the manifest.', status='[V]', login_or_s64=s64)

        except BaseException as e:
            print_to_log(
                text=f'Failed to exclude the {s64} maFile from the manifest: {e}', status='[X]', login_or_s64=s64
            )

    print_to_log(text=f'{len(manifest["entries"])}/{len(imported)} maFiles left on the manifest.', status='[V]')
    save_manifest(manifest=manifest)
