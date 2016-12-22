#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import os
from pprint import PrettyPrinter
from sys import argv, exit


def load_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError("No such file: {}".format(filepath))
    if not filepath.endswith(".json"):
        raise FileNotFoundError("Not a json file")
    with open(filepath, "r") as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    pp = PrettyPrinter(indent=4)
    pp.pprint(data)


if __name__ == '__main__':
    if len(argv) != 2:
        print("Ввидите имя загружаемого json-файла после 'python3 {}'".format(__file__))
        exit()
    if argv[1] == "--help":
        print("Поместите в текущую директорию файл в формате json.")
        print("Наберите python3 {} <имя файла> и нажмите enter.".format(__file__))
        exit()

    filename = argv[1]
    json_data = load_data(filename)
    pretty_print_json(json_data)
