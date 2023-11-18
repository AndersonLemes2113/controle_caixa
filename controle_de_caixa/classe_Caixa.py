from funcoes_extras import imprimir_linha
from random import randint
from decimal import *
getcontext().prec = 2


class Caixa(object):
    '''
    Classe para definir Caixa e suas funcionalidades, além de suas características/Atributos na aplicação.
    '''
    def __init__(self, nome='', usuario='', senha='', valor=0, notas=[], moedas=[]):
        self.abrir_caixa()
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
        self.valor = valor
        self.notas = notas
        self.moedas = moedas

    def contar_dinheiro(self):
        notas_caixa = self.notas
        moedas_caixa = self.moedas

        valores = {
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0,
            1: 0,
            0.50: 0,
            0.25: 0,
            0.1: 0,
            0.05: 0,
            0.01: 0
        }

        for nota in notas_caixa:
            if nota in valores:
                valores[nota] += 1

        for moeda in moedas_caixa:
            if moeda in valores:
                valores[moeda] += 1

        frase = "No caixa temos:\n"
        for valor, quantidade in valores.items():
            if quantidade > 0:
                frase += f"{quantidade} {'nota' if quantidade == 1 else 'notas'} de {valor}{' Reais' if valor >= 1 else ' Centavos'},\n"

        return frase

    def dar_troco(self, dados_venda={}):
        valor_caixa = self.valor
        notas_caixa = self.notas
        moedas_caixa = self.moedas
        valor_pagamento = dados_venda['Pagamento']
        valor_venda = dados_venda['Valor da Venda']
        troco = valor_pagamento - valor_venda
        print(imprimir_linha())
        print(f'O valor de troco a ser dado é R$ \033[33m{troco:.2f}\033[m.')
        while troco > 0:
            print(f'Valor no caixa R$ \033[32m{valor_caixa:.2f}\033[m.')
            while True:
                print(imprimir_linha())
                print(self.contar_dinheiro())
                print(imprimir_linha())
                esc = input('Usar nota ou moeda? [N=Nota/M=Moeda] ').upper().strip()[0]
                if esc in 'NM':
                    break
                print('Desculpe, mas a escolha digitada está incorreta!')
            if esc == 'N':
                while True:
                    try:
                        nota = int(input('Nota de qual valor deseja usar? ').strip())
                        if nota not in [200, 100, 50, 20, 10, 5, 2]:
                            print(f'\033[31mNão existe nota de valor {nota}!\033[m')
                        else:
                            break
                    except ValueError:
                        print('\033[31mValor digitado incorreto!\033[m')
                while True:
                    while True:
                        try:
                            qtd = int(input(f'Quantas Notas de {nota} Reais deseja usar? '))
                            break
                        except ValueError:
                            print('\033[31mValor digitado incorreto!\033[m')
                    cont = 0
                    for v in notas_caixa:
                        if v == nota:
                            cont += 1
                    if qtd > cont:
                        print('Não há moedas o suficiente!')
                    else:
                        break
                valor = nota * qtd
                troco -= valor
                valor_caixa -= valor
                for c in range(0, qtd):
                    notas_caixa.remove(nota)
            elif esc == 'M':
                while True:
                    try:
                        while True:
                            moeda = int(input('Qual valor de moeda deseja usar? '))
                            if moeda not in [1, 50, 25, 10, 5, 1]:
                                print(f'\033[31mNão existe moeda de valor {moeda}!\033[m')
                            else:
                                break
                        moeda = Decimal(float(moeda)) / 100
                        break
                    except ValueError:
                        print('Valor inválido!')

                valor = 0
                if int(moeda * 100) > 1:
                    while True:
                        qtd = int(input(f'Quantas moedas de {moeda*100} Centavos deseja usar? '))
                        cont = 0
                        for v in moedas_caixa:
                            if v == float(moeda):
                                cont += 1
                        if qtd > cont:
                            print('Não há moedas o suficiente!')
                        else:
                            break
                    valor = float(moeda) * qtd
                    valor_caixa -= float(valor)
                    for c in range(0, qtd):
                        moedas_caixa.remove(float(moeda))
                elif int(moeda * 100) == 1:
                    qtd = 0
                    while True:
                        esc1 = input('Deseja utilizar moeda de 1 real ou de 1 Centavo? [R=Real/C=Centavo] ').upper().strip()[0]
                        if esc1 in 'RC':
                            break
                        print('Desculpe, mas a escolha digitada está incorreta!')
                    if esc1 == 'R':
                        while True:
                            qtd = int(input(f'Quantas moedas de {int(moeda * 100)} Real deseja usar? '))
                            cont = 0
                            for v in moedas_caixa:
                                if v == int(moeda * 100):
                                    cont += 1
                            if qtd > cont:
                                print('Não há moedas o suficiente!')
                            else:
                                break

                    elif esc1 == 'C':
                        while True:
                            qtd = int(input(f'Quantas moedas de {int(moeda * 100)} Centavo deseja usar? '))
                            cont = 0
                            for v in moedas_caixa:
                                if v == float(moeda):
                                    cont += 1
                            if qtd > cont:
                                print('Não há moedas o suficiente!')
                            else:
                                break
                    if esc1 == 'R':
                        moeda = Decimal(1)
                        valor = float(moeda) * qtd
                        valor_caixa -= float(valor)
                        for c in range(0, qtd):
                            moedas_caixa.remove(float(moeda))
                    elif esc1 == 'C':
                        moeda = Decimal(0.01)
                        valor = float(moeda) * qtd
                        valor_caixa -= float(valor)
                        for c in range(0, qtd):
                            moedas_caixa.remove(float(moeda))
                else:
                    qtd = int(input(f'Quantas moedas de {int(moeda)} deseja usar? '))
                    valor = moeda * qtd
                    valor_caixa -= float(valor)
                    for c in range(0, qtd):
                        moedas_caixa.remove(float(moeda))
                troco = float(troco) - valor
            if float(troco) > 0:
                print(imprimir_linha())
                print(f'Ainda tem R$ \033[33m{troco:.2f}\033[m de troco a ser entregue!')
                print(float(troco))
            elif float(troco) < 0:
                print('Desculpe mas você entregou troco a mais! Quebra de caixa!')
                print(float(troco))
            else:
                print(imprimir_linha())
                print('\033[32mTroco entregue corretamente!\033[m')
                print(imprimir_linha())
        return troco

    def guardar_dinheiro(self, dados_venda={}):
        pass

    def sangrar_caixa(self):
        pass

    def fechar_caixa(self):
        pass

    def abrir_caixa(self):
        # O objetivo dessa função é criar notas de valores e quantidades aleatórias para simular de forma melhor situações diferenciadas ao vivenciar o dia a dia de um operador de caixa
        combinacao_1 = [50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 5, 5, 2, 2, 1, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5,
                        0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.1, 0.1,
                        0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05,
                        0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                        0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                        0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
        combinacao_2 = [100, 20, 20, 10, 10, 5, 5, 5, 5, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
                        0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                        0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
        sorteado = randint(1, 2)
        if sorteado == 1:
            notas = []
            moedas = []
            for v in combinacao_1:
                if v > 1:
                    notas.append(v)
                else:
                    moedas.append(v)
            self.notas = notas
            self.moedas = moedas
            self.valor = round(sum(combinacao_2), 2)
        elif sorteado == 2:
            notas = []
            moedas = []
            for v in combinacao_1:
                if v > 1:
                    notas.append(v)
                else:
                    moedas.append(v)
            self.notas = notas
            self.moedas = moedas
            self.valor = round(sum(combinacao_2), 2)
        return self.contar_dinheiro()

    @staticmethod
    def pedir_moeda(texto):
        '''
        Função com objetivo de fazer análise no valor que deve ser dado de troco, visando simplificar a entrega do troco e
        manter o caixa sempre com notas e moedas de vários valores e em quantidade ideal para bom funcionamento do caixa.
        '''
        txt = str(texto).split()
        lista = []
        for v in txt:
            for i in v:
                lista.append(i)
        ponto = int(lista.index('.') + 1)
        tamanho = int(len(lista))
        if int(texto) % 2 != 0:
            if tamanho - ponto == 1 and int(lista[ponto]) != 0:
                return f'\033[34mPerguntar se tem 1 real e {lista[ponto]}0 centavos trocados!\nOu qualque moeda para ajudar no troco.\033[m'
            if tamanho - ponto > 1:
                return f'\033[34mPerguntar se tem 1 real e {lista[ponto]}{lista[ponto+1]} centavos trocados!\nOu qualque moeda para ajudar no troco.\033[m'
            else:
                return f'\033[34mPerguntar se tem 1 Real para ajudar no troco!\033[m'
        else:
            if tamanho - ponto == 1 and int(lista[ponto]) != 0:
                return f'\033[34mPerguntar se tem {lista[ponto]}0 centavos trocados!\nOu qualque moeda para ajudar no troco.\033[m'
            if tamanho - ponto > 1:
                return f'\033[34mPerguntar se tem {lista[ponto]}{lista[ponto+1]} centavos trocados!\nOu qualque moeda para ajudar no troco.\033[m'
