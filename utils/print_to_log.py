from typing import Optional, Any

from pretty_utils.miscellaneous.time_and_date import unix_to_strtime

from data import config


def print_to_log(text: Any, status: Optional[str] = '', i: Optional[int] = None, total: Optional[int] = None,
                 login_or_s64: Optional[str] = None) -> None:
    printable_text = f'{unix_to_strtime()}'
    color = ''
    if status:
        printable_text += f' | {status}'
        if status == '[V]':
            color = config.LIGHTGREEN_EX

        elif status == '[!]':
            color = config.LIGHTYELLOW_EX

        elif status == '[X]':
            color = config.RED

    if login_or_s64:
        printable_text += f' | {login_or_s64}'
        if i is not None and total is not None:
            printable_text += f' ({i + 1}/{total})'

    printable_text += f' | {text}'
    print(color + printable_text + config.RESET_ALL)
    try:
        with open(file=config.LOG_FILE, mode='a', encoding='utf-8') as file:
            file.write(printable_text + '\n')

    except:
        pass
