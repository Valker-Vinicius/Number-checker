def fact(n1):
    f = 1
    for c in range(1, n1+1):
        f *= c
    return f


def triple(n1):
    return n1 * 3


def double(num, form=False):
    result = num*2
    if form:
        result = f'R${result}'
    return result


def half(num, form=False):
    result = num/2
    if form:
        result = f'R${result}'
    return result


def increase(num, percent, form=False):
    percent *= num
    percent /= 100
    result = num + percent
    if form:
        result = f'R${result}'
    return result


def reduce(num, percent, form=False):
    percent *= num
    percent /= 100
    result = num - percent
    if form:
        result = f'R${result:2f}'
    return result


def coin(value):
    value = f'R${value}'
    return value.replace('.', ',')


def readMoney(phase):
    val = False
    while not val:
        frase = str(input(f'\033[1;30m{phase}')).replace(',', '.').strip()
        if frase.isalpha() or frase == '':
            print(f'\033[1;31mERRO! "{frase}" é um número inválido!')
        else:
            val = True
            frase = float(frase)
            return frase


def leiaint(a):
    while True:
        global n
        n = input(a)
        if n.isnumeric():
            return n
        else:
            print('\033[1;31mERRO! Apenas números inteiros são permitidos.')
