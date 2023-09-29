preco = 0
qtd_macas = int(input("Digite a quantidade de maçãs: "))

if qtd_macas >= 12:
    preco = 1.30
else:
    preco = 1.0
custo = preco * qtd_macas
print("O custo das maçãs foi de: ",custo)