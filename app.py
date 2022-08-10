import glob
import json
import logging
import os

from functions.files import absolute_path, touch


def main():
    try:
        touch(processed)
        touch(find_it, True)

        if touch(maFiles):
            print('[V] A folder for maFiles was created, put the necessary files in it!')
            return

        manifest_path = absolute_path(maFiles, 'manifest.json')
        mafiles = glob.glob(absolute_path(maFiles, '*.maFile'))
        if not mafiles:
            print('[!] The maFiles folder is empty, fill it up!')
            return

        text = '''Select a function:
(1) Find maFiles by account logins and/or SteamID64s
(2) Name maFiles as logins
(3) Name maFiles as SteamID64s
(4) Add maFiles to the manifest
(5) Exclude non-existent maFiles from the manifest
> '''
        s = int(input(text))
        if s == 1:
            with open(find_it) as f:
                lines = f.readlines()
                accounts = {line.rstrip().replace('https://steamcommunity.com/profiles/', '').lower(): '' for line in
                            lines}

            if not accounts:
                print(f'[!] The {find_it} is empty, specify logins and/or SteamID64s!')
                return

            for mafile in mafiles:
                try:
                    content = json.load(open(mafile))
                    if 'account_name' in content and content['account_name'] in accounts:
                        login = content['account_name']
                        new_path = absolute_path(processed, f'{login}.maFile')
                        os.rename(mafile, new_path)
                        accounts[login] = new_path

                    elif 'Session' in content and 'SteamID' in content['Session'] and str(
                            content['Session']['SteamID']) in accounts:
                        SteamID64 = str(content["Session"]["SteamID"])
                        new_path = absolute_path(processed, f'{SteamID64}.maFile')
                        os.rename(mafile, new_path)
                        accounts[SteamID64] = new_path
                except:
                    pass

            for account in accounts:
                mafile = accounts[account]
                if mafile:
                    print(f'[V] {account} was found: {mafile}')

                else:
                    print(f"[X] {account} wasn't found")

        elif s == 2:
            for mafile in mafiles:
                content = json.load(open(mafile))
                if 'account_name' in content:
                    login = content['account_name']
                    new_path = absolute_path(processed, f'{login}.maFile')
                    os.rename(mafile, new_path)
                    print(f'[V] {mafile} -> {new_path}')

        elif s == 3:
            for mafile in mafiles:
                content = json.load(open(mafile))
                if 'Session' in content and 'SteamID' in content['Session']:
                    SteamID64 = content["Session"]["SteamID"]
                    new_path = absolute_path(processed, f'{SteamID64}.maFile')
                    os.rename(mafile, new_path)
                    print(f'[V] {mafile} -> {new_path}')

        elif s == 4:
            if os.path.exists(manifest_path):
                manifest = json.load(open(manifest_path))

            else:
                manifest = {
                    "encrypted": False,
                    "first_run": False,
                    "entries": [],
                    "periodic_checking": False,
                    "periodic_checking_interval": 20,
                    "periodic_checking_checkall": False,
                    "auto_confirm_market_transactions": False,
                    "auto_confirm_trades": False
                }

            imported = [entry['steamid'] for entry in manifest['entries']]
            for mafile in mafiles:
                try:
                    content = json.load(open(mafile))
                    if 'Session' in content and 'SteamID' in content['Session']:
                        SteamID64 = content["Session"]["SteamID"]
                        if not SteamID64 in imported:
                            print(f'[V] {SteamID64} was added to the manifest')
                            manifest['entries'].append({
                                'encryption_iv': None,
                                'encryption_salt': None,
                                'filename': f'{SteamID64}.maFile',
                                'steamid': SteamID64
                            })
                        os.rename(mafile, absolute_path(processed, f'{SteamID64}.maFile'))
                except:
                    pass

            with open(absolute_path(processed, 'manifest.json'), 'w') as f:
                json.dump(manifest, f, ensure_ascii=False, separators=(',', ':'))

        elif s == 5:
            if not os.path.exists(manifest_path):
                print('[!] There is no the manifest.json file in the maFiles directory!')
                return

            manifest = json.load(open(manifest_path))
            imported = {entry['steamid']: entry for entry in manifest['entries']}
            existing = []
            for mafile in mafiles:
                try:
                    content = json.load(open(mafile))
                    if 'Session' in content and 'SteamID' in content['Session']:
                        SteamID64 = content["Session"]["SteamID"]
                        existing.append(SteamID64)
                        if SteamID64 in imported:
                            os.rename(mafile, absolute_path(processed, f'{SteamID64}.maFile'))

                        else:
                            print(f'[V] {SteamID64} was deleted from the manifest')
                            manifest['entries'].remove(imported[SteamID64])
                except:
                    pass

            entries = manifest['entries'].copy()
            for entry in manifest['entries']:
                SteamID64 = entry['steamid']
                if SteamID64 not in existing:
                    print(f'[V] {SteamID64} was deleted from the manifest')
                    entries.remove(entry)

            manifest['entries'] = entries.copy()
            print(f'\n[V] There are {len(entries)} accounts left on the manifest')
            with open(absolute_path(processed, 'manifest.json'), 'w') as f:
                json.dump(manifest, f, ensure_ascii=False, separators=(',', ':'))

        else:
            print('[!] There is no such function!')

    except ValueError:
        logging.exception('hi')
        print("[!] The entered text isn't a number!")

    except:
        logging.exception('[!] Something went wrong!')


processed = 'processed'
find_it = 'find_it.txt'
maFiles = 'maFiles'

if __name__ == '__main__':
    main()
    input('\nPress Enter to exit')
