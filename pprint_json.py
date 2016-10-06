# -*- coding: utf-8 -*-
import argparse
import json
import os
import sys


def load_win_unicode_console():
    if sys.platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()


def get_named_argument(arg_name: str) -> str:
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser()
        parser.add_argument('--' + arg_name)
        return getattr(parser.parse_args(sys.argv[1:]), arg_name)
    else:
        print('Введите параметр в формате --%s Значение' % arg_name)
        exit(1)


def load_data(filepath: str):
    if os.path.isfile(filepath):
        try:
            with open(filepath, mode='r', encoding="utf-8") as file:
                return json.load(file)
        except PermissionError:
            print('У вас нет прав доступа к файлу')
            exit(1)
    else:
        print('Файл не найден')
        exit(1)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':

    load_win_unicode_console()
    file_path = get_named_argument('json')
    data = load_data(file_path)
    pretty_print_json(data)
