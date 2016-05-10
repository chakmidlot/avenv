#!/usr/bin/env python3

import glob
import os
import re

from global_config import get_activation_path

def get_idea_config():
    dirname = os.getcwd()

    while dirname != '/':
        path = os.path.join(dirname, '.idea/misc.xml')
        if glob.glob(path):
            return path

        dirname = os.path.dirname(dirname)


def parse_config(filepath):
    row = open(filepath).read()
    venv_name = re.compile(r'project-jdk-name="([^"]*)"')
    match = venv_name.search(row)
    if not match and not match.groups(0):
        return None

    return get_activation_path(match.groups()[0])


def main():
    config = get_idea_config()
    print(parse_config(config))


if __name__ == '__main__':

    main()