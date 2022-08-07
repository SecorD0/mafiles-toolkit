import os
import pathlib


def absolute_path(*args):
    """
    Returns an absolute path to a file starting from the program directory.

    :param args: parts of the path to joining
    :return: the absolute path
    """
    return os.path.join(str(pathlib.Path().absolute()), *args)


def touch(path: str, file: bool = False) -> bool:
    """
    Create object (file or directory) if it doesn't exists.

    :param str path: path to an object
    :param bool file: is it a file?
    :return bool: True if the object was created
    """
    if file:
        if not os.path.exists(path):
            with open(path, 'w') as f:
                f.write('')
            return True
        return False

    if not os.path.isdir(path):
        os.mkdir(path)
        return True
    return False
