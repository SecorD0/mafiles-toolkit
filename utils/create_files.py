from pretty_utils.miscellaneous.files import touch

from data import config


def create_files():
    touch(path=config.FILES_DIR)
    touch(path=config.MAFILES_DIR)
    touch(path=config.PROCESSED_DIR)
    touch(path=config.FIND_IT_FILE, file=True)


create_files()
