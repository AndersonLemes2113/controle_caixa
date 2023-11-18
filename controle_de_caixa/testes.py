from classe_Caixa import *
from classe_Produtos import *

caixa1 = Caixa()
caixa1.abrir_caixa()
print(caixa1.contar_dinheiro())
prateleira1 = Produtos()
venda = prateleira1.vender()
caixa1.dar_troco(venda)
