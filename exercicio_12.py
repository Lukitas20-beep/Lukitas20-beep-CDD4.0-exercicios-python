votos_brancos = int(input("Quantos votos brancos tivemos: "))
votos_nulos = int(input("Quantos votos nulos tivemos: "))
votos_validos = int(input("Quantos votos válidos nós tivemos: "))

total = votos_validos + votos_nulos + votos_brancos
print("O total de eleitores é: ", total)

percentual_b = ((votos_brancos / total)*100)
print(percentual_b,"% de votos brancos")
percentual_n = ((votos_nulos / total*100))
print(percentual_n,"% de votos nulos")
percentual_v = ((votos_validos / total* 100))
print(percentual_v,"% votos validos")