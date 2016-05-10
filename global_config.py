import glob
import os
import re


re_patterns_order = [re.compile(x) for x in [
        r'.PyCharm\d{2}$',
        r'.PyCharm\d{4}\.\d$'
    ]
]

config_path = '/config/options/jdk.table.xml'

venv_name_pattern = '<name value="{}" />'

re_venv_path = re.compile(r'<homePath value="(.+)" />')

replacements = [
    ['$USER_HOME$', os.path.expanduser('~')]
]


def get_activation_path(venv_name):
    config = get_config()

    venv_index = config.find(venv_name_pattern.format(venv_name))
    venv_path = re_venv_path.search(config, venv_index)

    path = venv_path.groups()[0]

    for before, after in replacements:
        path = path.replace(before, after)

    return '/'.join(path.split('/')[:-1]) + '/activate'


def get_config():
    glob_pattern = '~/.PyCharm*'
    full_glob = os.path.expanduser(glob_pattern)

    folders = sort_rows(glob.glob(full_glob))

    with open(folders[-1] + config_path) as fp:
        return fp.read()


def sort_rows(rows):
    sorted_rows = []

    for pattern in re_patterns_order:
        sorted_rows += sorted([x for x in rows if pattern.search(x)])

    return sorted_rows


if __name__ == '__main__':
    print(get_activation_path('Python 3.5.1 virtualenv at ~/atata 1'))
