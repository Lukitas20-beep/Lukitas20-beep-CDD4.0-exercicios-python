dia_idade = int(input("Digite o dia em que você nasceu: "))
dia_atual = int(input("Digite o dia atual: "))
mes_idade = int(input("Digite o mês em que você nasceu: "))
mes_atual = int(input("Digite o mês atual: "))
idade=int(input("Digite a sua idade: "))

mes = mes_atual - mes_idade
dias = dia_atual - dia_idade
if mes < 0:
    mes = mes *(-1)
dia_atual = dia_atual - dias
if dia_atual < 0:
    dia_atual = dia_atual*(-1)

idade_dias = 365 * idade + 30 * mes + dia_atual
print("Sua idade em dias é: ",idade_dias)