num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 != num2:
    if num1 > num2:
        print(num2, num1)
    else:
        print(num1, num2)
else:
    print("Operação encerrada")