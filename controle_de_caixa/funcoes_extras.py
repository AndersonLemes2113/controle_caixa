def imprimir_linha():
    linha = ('-='*50)
    return linha


def verificar_numero(txt):
    valor = txt
    while True:
        try:
            valor = valor.replace(',', '.').strip()
            valor = float(valor)
            return valor
        except ValueError:
            if valor == '':
                print('\033[32mValor não digitado!\033[m')
                print(imprimir_linha())
            else:
                print(f'O valor digitado {valor} não é um valor válido!\n\033[34mDigite apenas números!\033[m')
                print(imprimir_linha())
            valor = input('Qual vai ser o valor do pagamento? R$ ')


def verificar_S_ou_N(txt):
    try:
        esc = input(f'{txt} ').strip().upper()[0]
        while True:
            if esc in 'SN':
                lista = [True, esc]
                return lista
            else:
                print('Escolha inválida!')
                break
    except:
        print('ERRO!')

