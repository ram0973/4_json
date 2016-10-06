# -*- coding: utf-8 -*-
import json
from sys import platform

JSON_FILE = 'Бары.json'


def load_data(filepath):
    with open(filepath, mode='r', encoding="utf-8") as file:
        return json.load(file)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':

    if platform == 'win32':
        import win_unicode_console
        win_unicode_console.enable()
    data = load_data(JSON_FILE)
    pretty_print_json(data)
