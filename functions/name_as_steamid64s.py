import os

from data import config
from functions.get_mafile_dict import get_mafile_dicts
from utils.print_to_log import print_to_log


def name_as_steamid64s():
    _, s64_dict = get_mafile_dicts()
    for s64, mafile_path in s64_dict.items():
        try:
            new_path = os.path.join(config.PROCESSED_DIR, f'{s64}.maFile')
            os.rename(mafile_path, new_path)
            print_to_log(text=f'maFile was renamed: {mafile_path} -> {new_path}', status='[V]', login_or_s64=s64)

        except BaseException as e:
            print_to_log(text=f'Failed to rename {mafile_path} maFile: {e}', status='[X]', login_or_s64=s64)

    print_to_log(text=f'{len(s64_dict)} maFiles were renamed.', status='[V]')
