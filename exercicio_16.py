hora_inicio = int(input("Digite a hora de início do jogo: "))
hora_fim = int(input("Digite a hora do fim do jogo: "))

horas = hora_fim - hora_inicio

if hora_inicio >= hora_fim:
    horas = (24-hora_inicio) + hora_fim
print("O jogo teve",horas,"Horas")
