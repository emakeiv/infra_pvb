import os

BASEDIR = ''

def symbol_to_path(symbol, extension, base_dir=BASEDIR):
    return os.path.join(base_dir, '{}.{extension}'.format(symbol))