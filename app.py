import logging

from utils.create_files import create_files
from data import config
from data.models import ProgramActions
from functions.add_to_manifest import add_to_manifest
from functions.exclude_from_manifest import exclude_from_manifest
from functions.find import find
from functions.get_mafile_dict import get_mafile_dicts
from functions.name_as_logins import name_as_logins
from functions.name_as_steamid64s import name_as_steamid64s

if __name__ == '__main__':
    create_files()
    login_dict, _ = get_mafile_dicts()
    if login_dict:
        while True:
            action = None
            print('''  Select the action:
1) Find maFiles by account logins and/or SteamID64s;
2) Name maFiles as logins;
3) Name maFiles as SteamID64s;
4) Add maFiles to the manifest;
5) Exclude non-existent maFiles from the manifest;
6) Exit.''')

            try:
                action = int(input('> '))
                print()
                if action == ProgramActions.Find.Selection:
                    find()

                elif action == ProgramActions.NameAsLogins.Selection:
                    name_as_logins()

                elif action == ProgramActions.NameAsSteamID64s.Selection:
                    name_as_steamid64s()

                elif action == ProgramActions.AddToManifest.Selection:
                    add_to_manifest()

                elif action == ProgramActions.ExcludeFromManifest.Selection:
                    exclude_from_manifest()

                else:
                    break

            except KeyboardInterrupt:
                print()

            except ValueError:
                print(f"\n{config.RED}[X] You didn't enter a number!{config.RESET_ALL}")

            except BaseException as e:
                logging.exception('main')
                print(f'\n{config.RED}[X] Something went wrong: {e}{config.RESET_ALL}\n')

            if action:
                break

    else:
        print(f'\n{config.RED}[X] The maFiles folder is empty, fill it up!{config.RESET_ALL}')

    input(f'\nPress {config.LIGHTGREEN_EX}Enter{config.RESET_ALL} to exit.\n')
