import os
import platform
import sys
from pathlib import Path

from colorama import Fore, Style

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()

else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

if platform.system() == 'Windows':
    GREEN = ''
    LIGHTGREEN_EX = ''
    RED = ''
    LIGHTYELLOW_EX = ''
    RESET_ALL = ''

else:
    GREEN = Fore.GREEN
    LIGHTGREEN_EX = Fore.LIGHTGREEN_EX
    RED = Fore.RED
    LIGHTYELLOW_EX = Fore.LIGHTYELLOW_EX
    RESET_ALL = Style.RESET_ALL

FILES_DIR = os.path.join(ROOT_DIR, 'files')
MAFILES_DIR = os.path.join(FILES_DIR, 'maFiles')
PROCESSED_DIR = os.path.join(FILES_DIR, 'processed')

LOG_FILE = os.path.join(FILES_DIR, 'log.log')
ERRORS_FILE = os.path.join(FILES_DIR, 'errors.log')

FIND_IT_FILE = os.path.join(FILES_DIR, 'find_it.txt')
MANIFEST_FILE = os.path.join(MAFILES_DIR, 'manifest.json')
PROCESSED_MANIFEST_FILE = os.path.join(PROCESSED_DIR, 'manifest.json')
