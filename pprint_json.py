# -*- coding: utf-8 -*-
import argparse
import json
import sys

TAB_INDENT_SIZE = 4


def load_win_unicode_console():
    """
    Включаем правильное отображение unicode в консоли под MS Windows
    """
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def load_json_data(file_path: str):
    with open(file_path, mode='r', encoding="utf-8") as file:
        return json.load(file)


def pretty_print_json(data):
    print(json.dumps(data,
                     sort_keys=True,
                     indent=TAB_INDENT_SIZE,
                     ensure_ascii=False))


if __name__ == '__main__':

    load_win_unicode_console()

    parser = argparse.ArgumentParser()
    parser.add_argument('--json', help='Введите путь к файлу .json')

    json_file_path = parser.parse_args().json

    if not json_file_path:
        parser.print_help()
        exit(1)

    try:
        json_data = load_json_data(json_file_path)
    except OSError as error:
        print('Ошибка: %s в файле: %s' % (error.strerror, error.filename))
        exit(1)
    pretty_print_json(json_data)
