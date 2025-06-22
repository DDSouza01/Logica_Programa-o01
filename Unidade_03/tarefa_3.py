#Escreva um algoritmo que receba do usuário dois números e retorne a soma, a subtração, a multiplicação e a divisão entre eles.
numero_01 = int(input("Digite um número:" ))
numero_02 = int(input("Digite um outro número:" ))
calculo_01 = numero_01 + numero_02 
calculo_02 = numero_01 - numero_02
calculo_03 = numero_01 * numero_02
calculo_04 = numero_01 // numero_02
print(f"O resultado da soma dos números é: {calculo_01}")
print(f"O resultado da subtração dos números é: {calculo_02}")
print(f"O resultado da multiplicação dos números é: {calculo_03}")
print(f"O resultado da divisão dos números é: {calculo_04}")

#Escreva um algoritmo que receba do usuário a base e a altura de um triângulo, calcule e exiba sua área.
base = int(input("Digite o valor da base do triângulo:" ))
altura = int(input("Digite o valor da altura do triângulo:" ))
area = (base * altura) // 2
print(f" O valor da área do triângulo é: {area}")

#Faça um Programa que pergunte ao usuário quanto você ganha por hora e o número de horas trabalhadas por dia, considerando que se trabalha 5 dias por semana. Calcule e mostre o total do seu salário ao mês.
valor_hora = float(input("Valor da hora trabalhada?" ))
horas_trabalho = float(input("Quantidade de horas trabalhadas por dia?" ))
dias_semana = 5
salario_mes = (valor_hora * horas_trabalho) * dias_semana
print(f"O valor do salário do mês é: {salario_mes}")

#Escreva um programa que peça ao usuário para digitar a sua idade e imprima na tela o número de dias que ele viveu até o momento.
idade = int(input("Digite sua idade:" ))
dias_vivido = idade * 365
print(f"Dias vividos até o momento é: {dias_vivido}")

#Escreva um programa que peça ao usuário para digitar seu nome e sobrenome SEPARADAMENTE e imprima na tela o nome completo.
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
n_completo = nome + " " + sobrenome
print(f" Seu nome completo é: {n_completo}")

#Escreva um programa que peça ao usuário para digitar a temperatura em Fahrenheit e converta para Celsius e Kelvin, imprimindo o resultado na tela.
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = float((celsius * 1.8) + 32)
kelvin = float(celsius + 273.15)
print(f"A temperatura em graus Farrenheit é: {fahrenheit}º")
print(f"A tempoeraturta em graus Kelvin é: {kelvin}º")

#Escreva um programa que informe a quantidade de 1’s que estão em um string. Exemplo: ´ 1011001 -> 4. A string será recebida de um usuário.
numero = input("Digite um número composto somente por 0's e 1's:")
quantidade_de_uns = numero.count("1")
print(f"A quantidade de uns na string é: {quantidade_de_uns}")

#Escreva um programa que receba do usuário uma palavra e a imprima de trás para frente.
palavra = input("Digite uma palavra: ")
inverso = palavra [::-1]
print(f"O inverso da palavra é: {inverso}")

#Escreva um programa que leia uma string contendo letras de uma frase inclusive os espaços em branco e retire os espaços em branco e depois escreva a string resultante.
string = input("Digite uma frase: ")
sem_espacos = string.replace(" ", "")
print(f"A frase sem os espaços é: {sem_espacos}")

#Escreva um programa que receba duas frases SEPARADAMENTE e imprima de maneira invertida, em adição, troque as letras A por *.
frase_01 = input("Digite a primeira frase: ")
frase_02 = input("Digite a segunda frase: ")
frase_01_alteracao = frase_01[::-1].replace('A', '*').replace('a', '*')
frase_02_alteracao = frase_02[::-1].replace('A', '*').replace('a', '*')
print(f"A primeira frase alterada é: {frase_01_alteracao}")
print(f"A segunda frase alterada é: {frase_02_alteracao}")
