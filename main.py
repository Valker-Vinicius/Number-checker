from facilitators import cores


def readint(a):
    while True:
        try:
            f = int(input(a).strip())
        except (ValueError, TypeError):
            print(f'{cores.red()}ERRO! São permitidos apenas números inteiros, tente novamente.')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por não informar os dados.')
            return 0
        else:
            return f


def readfloat(a):
    while True:
        try:
            f = float(input(a).strip())
        except (ValueError, TypeError):
            print(f'{cores.red()}ERRO! São permitidos apenas numeros decimais, tente novamente.')
        except KeyboardInterrupt:
            print('O usuário optou por não informar os dados.')
            print(f'Seu número inteiro foi {n1} e o seu decimal foi {n2}')
            return 0
        else:
            return f


n1 = readint(f'{cores.erase()}Digite um número inteiro: ')
n2 = readfloat(f'{cores.erase()}Digite um número real: ')
print(f'Seu número inteiro foi {n1} e o seu decimal foi {n2}')