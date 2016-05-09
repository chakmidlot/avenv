#!/usr/bin/env python3

import glob
import os
import re


def get_idea_config():
    dirname = os.getcwd()

    while dirname != '/':
        path = os.path.join(dirname, '.idea/misc.xml')
        if glob.glob(path):
            return path

        dirname = os.path.dirname(dirname)


def parse_config(filepath):
    row = open(filepath).read()
    venv_name = re.compile(r'project-jdk-name="Python [\w.]+( virtualenv at)? ([^"]*)')
    match = venv_name.search(row)
    if not match and not match.groups(0):
        return None

    venv = match.groups()[1]

    if venv.startswith('('):
        venv = venv[1:-1]
    venv = os.path.expanduser(venv)

    return '{}/bin/activate'.format(venv)


def main():
    config = get_idea_config()
    print(parse_config(config))


if __name__ == '__main__':

    main()