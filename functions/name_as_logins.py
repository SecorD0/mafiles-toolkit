import os

from data import config
from functions.get_mafile_dict import get_mafile_dicts
from utils.print_to_log import print_to_log


def name_as_logins():
    login_dict, _ = get_mafile_dicts()
    for login, mafile_path in login_dict.items():
        try:
            new_path = os.path.join(config.PROCESSED_DIR, f'{login}.maFile')
            os.rename(mafile_path, new_path)
            print_to_log(text=f'maFile was renamed: {mafile_path} -> {new_path}', status='[V]', login_or_s64=login)

        except BaseException as e:
            print_to_log(text=f'Failed to rename {mafile_path} maFile: {e}', status='[X]', login_or_s64=login)

    print_to_log(text=f'{len(login_dict)} maFiles were renamed.', status='[V]')
