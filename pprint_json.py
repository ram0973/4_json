# -*- coding: utf-8 -*-
import argparse
import json
import sys
from colorama import Style, Fore


def load_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    и раскрашивание символов
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()
        from colorama import init
        init()  # colorama


def get_json_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json', help='Введите путь к файлу .json')
    if parser.parse_args().json:
        return parser.parse_args().json
    else:
        parser.print_help()
        exit(1)


def load_json_data(file_path: str):
    try:
        with open(file_path, mode='r', encoding="utf-8") as file:
                return json.load(file)
    except OSError as error:
        print(Fore.RED+Style.BRIGHT, 'Ошибка: ', error.strerror, ' в файле: ',
              error.filename)
        exit(1)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':

    load_win_unicode_console()
    json_file_path = get_json_argument()
    json_data = load_json_data(json_file_path)
    pretty_print_json(json_data)
