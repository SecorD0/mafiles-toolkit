import glob
import os
from typing import Dict, Tuple

from pretty_utils.miscellaneous.files import read_json

from data import config


def get_mafile_dicts() -> Tuple[Dict[str, str], Dict[str, str]]:
    login_dict = {}
    s64_dict = {}
    mafiles = glob.glob(os.path.join(config.MAFILES_DIR, '*.maFile'))
    for mafile_path in mafiles:
        content = read_json(path=mafile_path)
        if 'account_name' in content:
            login = content['account_name']
            login_dict[login] = mafile_path

        if 'Session' in content and 'SteamID' in content['Session']:
            s64_dict[str(content['Session']['SteamID'])] = mafile_path

    return login_dict, s64_dict
