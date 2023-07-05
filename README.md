<h1><p align="center">mafiles-toolkit</p></h1>

<p align="center"><img src="images/icons/app.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [DISCLAIMER](#DISCLAIMER)
- [Description](#Description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Docker (image)](#Docker-image)
    - [Docker (building)](#Docker-building)
    - [Source code](#Source-code)
- [Functions](#Functions)
    - [Find maFiles by account logins and/or SteamID64s](#Find-maFiles-by-account-logins-andor-SteamID64s)
    - [Name maFiles as logins](#Name-maFiles-as-logins)
    - [Name maFiles as SteamID64s](#Name-maFiles-as-SteamID64s)
    - [Add maFiles to the manifest](#Add-maFiles-to-the-manifest)
    - [Exclude non-existent maFiles from the manifest](#Exclude-non-existent-maFiles-from-the-manifest)
- [Updating](#Updating)
  - [Windows](#Windows-1)
  - [GitHub image](#GitHub-image)
  - [Self-built image](#Self-built-image)
  - [Source code](#Source-code-1)
- [Useful commands](#Useful-commands)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">DISCLAIMER</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program has no injections — you can make the code review to make sure. Any cases of third parties gaining access to your accounts aren't the fault of the developer, but of you or another person. Keep your sensitive data in a safe place.

⠀By using this program you have agreed to the above and have no and won't have claims against its developer.



<h1><p align="center">Description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The toolkit is designed to enhance your interaction with maFiles.

⠀Functions:
1. Find maFiles by account logins and/or SteamID64s;
2. Name maFiles as logins;
3. Name maFiles as SteamID64s;
4. Add maFiles to the manifest;
5. Exclude non-existent maFiles from the manifest.



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[mafiles-toolkit](https://github.com/SecorD0/mafiles-toolkit)

⠀[SDA official repository](https://github.com/Jessecar96/SteamDesktopAuthenticator)



<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `files` — a user files directory:
  - `maFiles` — a directory with maFiles for interaction;
  - `processed` — a directory with maFiles processed by the program;
  - `find_it.txt` — a text file with logins and/or SteamID64 to be found;
- `maFiles-toolkit.exe` / `app.py` — an executable file that runs the program.



<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/mafiles-toolkit/releases).
2. Create a folder and put the EXE file in it.
3. Run the program the first time to create necessary files.
4. Copy maFiles for interaction to the `maFiles` directory.
5. Fill in the `find_it.txt` file if you're going to find maFiles of specified accounts.
6. Run the program again, select a function, wait for it to finish and close it.
7. Open the `processed` directory to view the result.


<h2><p align="center">Docker (image)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/mafiles-toolkit/files:/program/files --name mafiles-toolkit ghcr.io/secord0/mafiles-toolkit:main
```
3. Copy maFiles for interaction to the `maFiles` directory.
4. Fill in the `find_it.txt` file if you're going to find maFiles of specified accounts.
5. Run the program again, select a function, wait for it to finish and close it:
```sh
docker run -it --rm -v $HOME/mafiles-toolkit/files:/program/files --name mafiles-toolkit ghcr.io/secord0/mafiles-toolkit:main
```
6. Open the `processed` directory to view the result.


<h2><p align="center">Docker (building)</p></h2>

1. Install Docker, in Ubuntu you can use the command:
```sh
. <(wget -qO- https://raw.githubusercontent.com/SecorD0/utils/main/installers/docker.sh)
```
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/mafiles-toolkit
```
3. Go to the repository:
```sh
cd mafiles-toolkit
```
4. Build an image:
```sh
docker build -t mafiles-toolkit .
```
5. Run the program the first time to create necessary files:
```sh
docker run -it --rm -v $HOME/mafiles-toolkit/:/program --name mafiles-toolkit mafiles-toolkit
```
6. Copy maFiles for interaction to the `maFiles` directory.
7. Fill in the `find_it.txt` file if you're going to find maFiles of specified accounts.
8. Run the program again, select a function, wait for it to finish and close it:
```sh
docker run -it --rm -v $HOME/mafiles-toolkit/:/program --name mafiles-toolkit mafiles-toolkit
```
9. Open the `processed` directory to view the result.


<h2><p align="center">Source code</p></h2>

1. Install [Python 3.8](https://www.python.org/downloads/).
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/mafiles-toolkit
```
3. Go to the repository:
```sh
cd mafiles-toolkit
```
4. Set up an environment.
5. Install requirements:
```sh
pip install -r requirements.txt
```
6. Run the `app.py` the first time to create necessary files.
7. Copy maFiles for interaction to the `maFiles` directory.
8. Fill in the `find_it.txt` file if you're going to find maFiles of specified accounts.
9. Run the `app.py` again, select a function, wait for it to finish and close it.
10. Open the `processed` directory to view the result.


⠀If you want to build the EXE file by yourself:
- Install `pyinstaller`:
```sh
pip install pyinstaller
```
- Build the EXE file:
```sh
pyinstaller app.py -Fn mafiles-toolkit -i images/icons/app.ico --add-binary "images/icons;images/icons"
```



<h1><p align="center">Functions</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Find maFiles by account logins and/or SteamID64s</p></h2>

⠀It extracts from a variety of maFiles only the ones you need by logins and/or SteamID64s. It renames file to specified login or SteamID64.

⠀Before execution you need to fill the `find_it.txt` file with logins and/or SteamID64s, e.g.:
```
Wilman_33
76561198018854190
76561198018490012
ONROENI
https://steamcommunity.com/profiles/76561198007602847
```

⠀Example output:
```
  Select the action:
1) Find maFiles by account logins and/or SteamID64s;
2) Name maFiles as logins;
3) Name maFiles as SteamID64s;
4) Add maFiles to the manifest;
5) Exclude non-existent maFiles from the manifest;
6) Exit.
> 1

04.07.2023 21:24:49 | [V] | wilman_33 | maFile was found: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\wilman_33.maFile
04.07.2023 21:24:49 | [V] | 76561198018854190 | maFile was found: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561198018854190.maFile
04.07.2023 21:24:49 | [!] | 76561198018490012 | maFile wasn't found!
04.07.2023 21:24:49 | [V] | onroeni | maFile was found: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\onroeni.maFile
04.07.2023 21:24:49 | [V] | 76561198007602847 | maFile was found: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561198007602847.maFile
04.07.2023 21:24:49 | [V] | 4/5 maFiles were found.

Press Enter to exit.

```


<h2><p align="center">Name maFiles as logins</p></h2>

⠀It names all maFiles as logins.

⠀Example output:
```
  Select the action:
1) Find maFiles by account logins and/or SteamID64s;
2) Name maFiles as logins;
3) Name maFiles as SteamID64s;
4) Add maFiles to the manifest;
5) Exclude non-existent maFiles from the manifest;
6) Exit.
> 2

04.07.2023 21:26:13 | [V] | wilman_33 | maFile was renamed: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\wilman_33.maFile -> C:\Users\Me\Desktop\mafiles-toolkit\files\processed\wilman_33.maFile
04.07.2023 21:26:13 | [V] | ymanjiv | maFile was renamed: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561198018854190.maFile -> C:\Users\Me\Desktop\mafiles-toolkit\files\processed\ymanjiv.maFile
04.07.2023 21:26:13 | [V] | onroeni | maFile was renamed: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\ONROENI.maFile -> C:\Users\Me\Desktop\mafiles-toolkit\files\processed\onroeni.maFile
04.07.2023 21:26:13 | [V] | o40dysi | maFile was renamed: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561198007602847.maFile -> C:\Users\Me\Desktop\mafiles-toolkit\files\processed\o40dysi.maFile
04.07.2023 21:26:13 | [V] | 4 maFiles were renamed.

Press Enter to exit.

```


<h2><p align="center">Name maFiles as SteamID64s</p></h2>

⠀It names all maFiles as SteamID64s.

⠀Example output:
```
  Select the action:
1) Find maFiles by account logins and/or SteamID64s;
2) Name maFiles as logins;
3) Name maFiles as SteamID64s;
4) Add maFiles to the manifest;
5) Exclude non-existent maFiles from the manifest;
6) Exit.
> 3

04.07.2023 21:27:32 | [V] | 76561198081830472 | maFile was renamed: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\wilman_33.maFile -> C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561198081830472.maFile
04.07.2023 21:27:32 | [V] | 76561198018854190 | maFile was renamed: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561198018854190.maFile -> C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561198018854190.maFile
04.07.2023 21:27:32 | [V] | 76561197997019522 | maFile was renamed: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\ONROENI.maFile -> C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561197997019522.maFile
04.07.2023 21:27:32 | [V] | 76561198007602847 | maFile was renamed: C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561198007602847.maFile -> C:\Users\Me\Desktop\mafiles-toolkit\files\processed\76561198007602847.maFile
04.07.2023 21:27:32 | [V] | 4 maFiles were renamed.

Press Enter to exit.

```


<h2><p align="center">Add maFiles to the manifest</p></h2>

⠀It takes all maFiles and adds them to the manifest, if not already added. It creates the `manifest.json` file automatically if there is no source one in the maFiles folder.

⠀Example output:
```
  Select the action:
1) Find maFiles by account logins and/or SteamID64s;
2) Name maFiles as logins;
3) Name maFiles as SteamID64s;
4) Add maFiles to the manifest;
5) Exclude non-existent maFiles from the manifest;
6) Exit.
> 4

04.07.2023 21:29:05 | [V] | 76561198081830472 | Account already on the manifest.
04.07.2023 21:29:05 | [V] | 76561198018854190 | Account was added to the manifest.
04.07.2023 21:29:05 | [V] | 76561197997019522 | Account was added to the manifest.
04.07.2023 21:29:05 | [V] | 76561198007602847 | Account already on the manifest.
04.07.2023 21:29:05 | [V] | 2/4 missing maFiles were added to the manifest.

Press Enter to exit.

```


<h2><p align="center">Exclude non-existent maFiles from the manifest</p></h2>

⠀It extracts all maFiles that are contained in the manifest and excludes from it those that couldn't be found.

⠀Example output:
```
  Select the action:
1) Find maFiles by account logins and/or SteamID64s;
2) Name maFiles as logins;
3) Name maFiles as SteamID64s;
4) Add maFiles to the manifest;
5) Exclude non-existent maFiles from the manifest;
6) Exit.
> 5

04.07.2023 21:32:18 | [V] | 76561198081830472 | Account was excluded from the manifest.
04.07.2023 21:32:18 | [V] | 76561198018854190 | Account on the manifest.
04.07.2023 21:32:18 | [V] | 76561197997019522 | Account on the manifest.
04.07.2023 21:32:18 | [V] | 76561198007602847 | Account on the manifest.
04.07.2023 21:32:18 | [V] | 3/4 maFiles left on the manifest.

Press Enter to exit.

```



<h1><p align="center">Updating</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">Windows</p></h2>

1. Download an EXE file of the new version from the [releases page](https://github.com/SecorD0/mafiles-toolkit/releases) and replace the old one with it.


<h2><p align="center">GitHub image</p></h2>

1. Stop the container:
```sh
docker stop mafiles-toolkit
```
2. Remove the container:
```sh
docker rm mafiles-toolkit
```
3. Update the image:
```sh
docker pull ghcr.io/secord0/mafiles-toolkit:main
```


<h2><p align="center">Self-built image</p></h2>

1. Stop the container:
```sh
docker stop mafiles-toolkit
```
2. Remove the container:
```sh
docker rm mafiles-toolkit
```
3. Go to the repository:
```sh
cd mafiles-toolkit
```
4. Update the local files:
```sh
git pull
```
5. Rebuild the image:
```sh
docker build -t mafiles-toolkit .
```


<h2><p align="center">Source code</p></h2>

1. Go to the repository:
```sh
cd mafiles-toolkit
```
2. Update the local files:
```sh
git pull
```



<h1><p align="center">Useful commands</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀To run the program (GitHub image):
```sh
docker run -it --rm -v $HOME/mafiles-toolkit/files:/program/files --name mafiles-toolkit ghcr.io/secord0/mafiles-toolkit:main
```

⠀To run the program (self-built image):
```sh
docker run -it --rm -v $HOME/mafiles-toolkit/:/program --name mafiles-toolkit mafiles-toolkit
```

⠀To remove the container:
```sh
docker stop mafiles-toolkit; docker rm mafiles-toolkit
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/mafiles-toolkit/issues/new/choose), select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Address of EVM networks (Ethereum, Polygon, BSC, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`
