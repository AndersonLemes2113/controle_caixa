from funcoes_extras import imprimir_linha, verificar_numero
from classe_Caixa import Caixa


class Produtos(object):
    def __init__(self, lista_produtos=[], codigo='', nome='', preco=0, validade=0, aumento=0, desconto=0):
        lista_produtos = [{'Codigo': 'ABC123', 'Nome': 'CHOCOLATE NESTLE', 'Preço': 14.25, 'Validade': '10/10/23'},
                          {'Codigo': 'ABC1234', 'Nome': 'BARRA DE SEREAL FITNES', 'Preço': 4.75,
                           'Validade': '10/10/23'}]
        self.lista_produtos = lista_produtos
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.validade = validade
        self.aumento = aumento
        self.desconto = desconto

    def cadastrar_produto(self):
        dicionario = {}
        self.codigo = input('Digite o código do produto: ').upper().strip()
        dicionario['Codigo'] = self.codigo
        self.nome = input('Digite o nome do produto: ').upper().strip()
        dicionario['Nome'] = self.nome
        self.preco = float(input('Digite o preco do produto: '))
        dicionario['Preço'] = self.preco
        self.validade = input('Digite a validade do produto: ')
        dicionario['Validade'] = self.validade
        self.lista_produtos.append(dicionario)
        return dicionario

    def vender(self):
        dados_venda = {}
        valor_venda = 0
        pagamento = 0
        while True:
            produto = self.encontrar_produto()
            valor_venda += float(produto['Preço'])
            esc = input('Tem mais produtos? [S/N] ').upper().strip()[0]
            if esc == 'N':
                print(imprimir_linha())
                break
            elif esc not in 'SN':
                while True:
                    print('\033[31mEscolha digitada está incorreta!\033[m')
                    esc = input('Tem mais produtos? [S/N] ').upper().strip()[0]
                    if esc in 'SN':
                        break
        print(f'O valor total da compra é: R$ {valor_venda:.2f}')
        if Caixa.pedir_moeda(valor_venda):
            print(Caixa.pedir_moeda(valor_venda))
        while True:
            valor_recebido = input('Qual vai ser o valor do pagamento? R$ ')
            dinheiro_recebido = verificar_numero(valor_recebido)
            if float(dinheiro_recebido) < float(valor_venda):
                print('-='*50)
                print(f'\033[31mValor do pagamento\033[m\033[32m (R$ {dinheiro_recebido:.2f})\033[m\033[31m menor que o valor da compra \033[m\033[32m(R$ {valor_venda:.2f})\033[m\033[31m! Verifique o valor!\033[m')
                print('-='*50)
            else:
                break
        pagamento += dinheiro_recebido
        dados_venda['Valor da Venda'] = valor_venda
        dados_venda['Pagamento'] = pagamento
        return dados_venda

    def encontrar_produto(self):
        while True:
            print(imprimir_linha())
            codigo = input('Digite o código do produto: ').upper().strip()
            for v in self.lista_produtos:
                for k, i in enumerate(v):
                    if codigo == v[i]:
                        print(f'Código: {v[i]}\nNome: {v["Nome"]}\nPreço: R$ {v["Preço"]:.2f}\nValidade: {v["Validade"]}')
                        print(imprimir_linha())
                        return v
            print('Produto não encontrado!Favor verificar o código digitado!')

