from facilitators import colors


def readint(userInput):
    while True:
        try:
            value = int(input(userInput).strip())
        except (ValueError, TypeError):
            print(f'{colors.red()}ERRO! São permitidos apenas números inteiros, tente novamente')
            continue
        except KeyboardInterrupt:
            print('O usuário optou por não informar os dados')
            return 0
        else:
            return value


def readfloat(userInput):
    while True:
        try:
            value = float(input(userInput).strip())
        except (ValueError, TypeError):
            print(f'{colors.red()}ERRO! São permitidos apenas numeros decimais, tente novamente')
        except KeyboardInterrupt:
            print('O usuário optou por não informar os dados')
            return 0
        else:
            return value


nInt = readint(f'{colors.erase()}Digite um número inteiro: ')
nFloat = readfloat(f'{colors.erase()}Digite um número real: ')
print(f'Seu número inteiro foi {nInt} e o seu decimal foi {nFloat}')
