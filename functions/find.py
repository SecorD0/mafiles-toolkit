import os

from pretty_utils.miscellaneous.files import read_lines

from data import config
from functions.get_mafile_dict import get_mafile_dicts
from utils.print_to_log import print_to_log


def find():
    accounts = read_lines(path=config.FIND_IT_FILE, skip_empty_rows=True)
    accounts = list(set([account.replace('https://steamcommunity.com/profiles/', '').lower() for account in accounts]))
    if not accounts:
        print(
            f'\n{config.RED}[X] The {config.FIND_IT_FILE} file is empty, '
            f'specify logins and/or SteamID64s!{config.RESET_ALL}'
        )
        return

    found = 0
    login_dict, s64_dict = get_mafile_dicts()
    for account in accounts:
        try:
            new_path = os.path.join(config.PROCESSED_DIR, f'{account}.maFile')
            if account in login_dict or account in s64_dict:
                if account in login_dict:
                    os.rename(login_dict[account], new_path)

                else:
                    os.rename(s64_dict[account], new_path)

                found += 1
                print_to_log(text=f'maFile was found: {new_path}', status='[V]', login_or_s64=account)

            else:
                print_to_log(text="maFile wasn't found!", status='[!]', login_or_s64=account)

        except BaseException as e:
            print_to_log(text=f'Something went wrong: {e}', status='[X]', login_or_s64=account)

    print_to_log(text=f'{found}/{len(accounts)} maFiles were found.', status='[V]')
