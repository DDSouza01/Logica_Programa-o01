# Escreva um programa que imprima a tabuada (Multiplicação) de um número inteiro informado pelo usuário. Imprima a tabuada de maneira organizada.
numero = int(input("Digite um número inteiro. "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
# Escreva um programa que calcule o fatorial de um número inteiro informado pelo usuário.
numero = int(input("Digite um número inteiro: "))
if numero < 0:
    print("Não é possível calcular o fatorial desse número negativo. ")
else:
    fatorial = 1
    contador = numero

    while True:
        fatorial *= contador
        contador -= 1
        if contador < 1:
            break

    print(f"O resultado fatorial de {numero} é {fatorial}: ") 

  



