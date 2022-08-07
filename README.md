<h1><p align="center">maFiles Toolkit</p></h1>


<p align="center"><img src="images/icon.ico" width="400"></p>

<h1><p align="center">Content</p></h1>

- [Short description](#Short-description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Source code](#Source-code)
- [Functions](#Functions)
    - [Find maFiles by account logins and/or SteamID64s](#Find-maFiles-by-account-logins-and-or-SteamID64s)
    - [Name maFiles as logins](#Name-maFiles-as-logins)
    - [Name maFiles as SteamID64s](#Name-maFiles-as-SteamID64s)
    - [Add maFiles to the manifest](#Add-maFiles-to-the-manifest)
    - [Exclude non-existent maFiles from the manifest](#Exclude-non-existent-maFiles-from-the-manifest)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)

<h1><p align="center">Short description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀This toolkit is designed to enhance your interaction with maFiles.

⠀Functions:
1. Find maFiles by account logins and/or SteamID64s;
2. Name maFiles as logins;
3. Name maFiles as SteamID64s;
4. Add maFiles to the manifest;
5. Exclude non-existent maFiles from the manifest.

<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[maFiles Toolkit](https://github.com/SecorD0/mafiles-toolkit)

⠀[SDA official repository](https://github.com/Jessecar96/SteamDesktopAuthenticator)

<h1><p align="center">File structure</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The program use the following files and directories:
- `maFiles` — a directory with maFiles for interaction;
- `processed` — a directory with maFiles processed by the program;
- `find_it.txt` — a text file with logins and/or SteamID64 to be found;
- `maFiles Toolkit.exe` / `app.py` — an executable file that runs the program.

<h1><p align="center">How to run</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

<h2><p align="center">Windows</p></h2>

1. Download an EXE file from the [releases page](https://github.com/SecorD0/mafiles-toolkit/releases);
2. Create a folder and put the EXE file in it;
3. Run the program the first time to create necessary files;
```
[V] A folder for maFiles was created, put the necessary files in it!

Press Enter to exit
```
4. Copy maFiles for interaction to the `maFiles` directory;
5. Run the program and select a function;
6. Open the `processed` directory to view the result;
7. Do whatever you want with the processed maFiles.

<h2><p align="center">Source code</p></h2>

1. Install [Python](https://www.python.org/downloads/);
2. Clone the repository:
```sh
git clone https://github.com/SecorD0/mafiles-toolkit
```
3. Set up an environment;
4. Install requirements:
```sh
pip install -r requirements.txt
```
5. Run the `app.py` the first time to create necessary files:
```
[V] A folder for maFiles was created, put the necessary files in it!

Press Enter to exit
```
6. Copy maFiles for interaction to the `maFiles` directory;
7. Run the `app.py` and select a function;
8. Open the `processed` directory to view the result;
9. Do whatever you want with the processed maFiles.

⠀If you want to build the EXE file by yourself, use the command:
```sh
pyinstaller app.py -F -n "maFiles Toolkit" -i "images/icon.ico"
```

<h1><p align="center">Functions</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

<h2><p align="center">Find maFiles by account logins and/or SteamID64s</p></h2>

⠀It extracts from a variety of maFiles only the ones you need by logins and/or SteamID64s. It renames file to specified login or SteamID64.

⠀Before execution you need to fill the `find_it.txt` file with logins and/or SteamID64s, e.g.:
```
Wilman_33
76561198018854190
onroeni
https://steamcommunity.com/profiles/76561198007602847
```

⠀Example output:
```
Select a function:
(1) Find maFiles by account logins and/or SteamID64s
(2) Name maFiles as logins
(3) Name maFiles as SteamID64s
(4) Add maFiles to the manifest
(5) Exclude non-existent maFiles from the manifest
> 1
[V] Wilman_33 was found: C:\Users\Me\Desktop\maFiles Toolkit\processed\wilman_33.maFile
[V] 76561198018854190 was found: C:\Users\Me\Desktop\maFiles Toolkit\processed\76561198018854190.maFile
[V] onroeni was found: C:\Users\Me\Desktop\maFiles Toolkit\processed\onroeni.maFile
[V] 76561198007602847 was found: C:\Users\Me\Desktop\maFiles Toolkit\processed\76561198007602847.maFile

Press Enter to exit
```

<h2><p align="center">Name maFiles as logins</p></h2>

⠀It names all maFiles as logins.

⠀Example output:
```
Select a function:
(1) Find maFiles by account logins and/or SteamID64s
(2) Name maFiles as logins
(3) Name maFiles as SteamID64s
(4) Add maFiles to the manifest
(5) Exclude non-existent maFiles from the manifest
> 2
[V] C:\Users\Me\Desktop\maFiles Toolkit\processed\wilman_33.maFile -> C:\Users\Me\Desktop\maFiles Toolkit\processed\wilman_33.maFile
[V] C:\Users\Me\Desktop\maFiles Toolkit\processed\76561198018854190.maFile -> C:\Users\Me\Desktop\maFiles Toolkit\processed\ymanjiv.maFile
[V] C:\Users\Me\Desktop\maFiles Toolkit\processed\onroeni.maFile -> C:\Users\Me\Desktop\maFiles Toolkit\processed\onroeni.maFile
[V] C:\Users\Me\Desktop\maFiles Toolkit\processed\76561198007602847.maFile -> C:\Users\Me\Desktop\maFiles Toolkit\processed\o40dysi.maFile

Press Enter to exit
```

<h2><p align="center">Name maFiles as SteamID64s</p></h2>

⠀It names all maFiles as SteamID64s.

⠀Example output:
```
Select a function:
(1) Find maFiles by account logins and/or SteamID64s
(2) Name maFiles as logins
(3) Name maFiles as SteamID64s
(4) Add maFiles to the manifest
(5) Exclude non-existent maFiles from the manifest
> 3
[V] C:\Users\Me\Desktop\maFiles Toolkit\processed\wilman_33.maFile -> C:\Users\Me\Desktop\maFiles Toolkit\processed\76561198081830472.maFile
[V] C:\Users\Me\Desktop\maFiles Toolkit\processed\76561198018854190.maFile -> C:\Users\Me\Desktop\maFiles Toolkit\processed\76561198018854190.maFile
[V] C:\Users\Me\Desktop\maFiles Toolkit\processed\onroeni.maFile -> C:\Users\Me\Desktop\maFiles Toolkit\processed\76561197997019522.maFile
[V] C:\Users\Me\Desktop\maFiles Toolkit\processed\76561198007602847.maFile -> C:\Users\Me\Desktop\maFiles Toolkit\processed\76561198007602847.maFile

Press Enter to exit
```

<h2><p align="center">Add maFiles to the manifest</p></h2>

⠀It takes all maFiles and adds them to the manifest, if not already added.

⠀Example output:
```
(1) Find maFiles by account logins and/or SteamID64s
(2) Name maFiles as logins
(3) Name maFiles as SteamID64s
(4) Add maFiles to the manifest
(5) Exclude non-existent maFiles from the manifest
> 4
[V] 76561198018854190 was added to the manifest
[V] 76561197997019522 was added to the manifest

Press Enter to exit
```

<h2><p align="center">Exclude non-existent maFiles from the manifest</p></h2>

⠀It extracts all maFiles that are contained in the manifest and deletes from it those that couldn't be found.

⠀Example output:
```
(1) Find maFiles by account logins and/or SteamID64s
(2) Name maFiles as logins
(3) Name maFiles as SteamID64s
(4) Add maFiles to the manifest
(5) Exclude non-existent maFiles from the manifest
> 5
[V] 76561198081830472 was deleted from the manifest

[V] There are 3 accounts left on the manifest

Press Enter to exit
```

<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/mafiles-toolkit/issues/new/choose), select the template, fill it out and submit it.

<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!
- Ethereum-like address (Ethereum, BSC, Moonbeam, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`