base = float(input("Digite o valor da base de um triângulo: "))
while(base <= 0):
    base = float(input("Digite um valor valido valor da base de um triângulo: "))
altura = float(input("Digite o valor da altura de um triangulo: "))
while(altura <= 0):
    altura = float(input("Digite um valor válido da altura de um triângulo: "))

A = (base * altura)/2
print("A área do triângulo é de: ",A)