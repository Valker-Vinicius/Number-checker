def blue(frase=''):
    if frase == '':
        return '\033[34m'
    else:
        return f'\033[34m{frase}\033[m'


def green(frase=''):
    if frase == '':
        return '\033[32m'
    else:
        return f'\033[32m{frase}\033[m'


def purple(frase=''):
    if frase == '':
        return '\033[35m'
    else:
        return f'\033[35m{frase}\033[m'


def white(frase=''):
    if frase == '':
        return '\033[30m'
    else:
        return f'\033[30m{frase}\033[m'


def red(frase=''):
    if frase == '':
        return '\033[31m'
    else:
        return f'\033[31m{frase}\033[m'


def yellow(frase=''):
    if frase == '':
        return '\033[33m'
    else:
        return f'\033[33m{frase}\033[m'


def whiteblue(frase=''):
    if frase == '':
        return '\033[36m'
    else:
        return f'\033[36m{frase}\033[m'


def grey(frase=''):
    if frase == '':
        return '\033[37m'
    else:
        return f'\033[37m{frase}\033[m'


def erase(frase=''):
    if frase == '':
        return '\033[m'
    else:
        return f'\033[m{frase}\033[m'


def negrito(frase=''):
    if frase == '':
        return '\033[1m'
    else:
        return f'\033[1m{frase}\033[m'
