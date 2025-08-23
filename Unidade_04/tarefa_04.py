#Escreva um programa que leia o nome de um dia da semana e verifique se é um dia útil ou um dia de fim de semana. Caso seja um dia útil, imprima "Dia útil". Caso seja um dia de fim de semana, imprima "Fim de semana

dias_semana = input('Digite um dia da semana: ')
if dias_semana in ['segunda', 'terça', 'quarta', 'quinta', 'sexta']:
    print('Dia útil')
else:
    print('Fim de semana')

#No mundo de The Witcher, criaturas diferentes apresentam características únicas. Baseado nas pistas abaixo, escreva um programa que identifique o tipo de criatura que Geralt está enfrentando:

horario = input("Digite o horário (dia/noite): ")
caracteristica1 = input("Digite a primeira característica: ")
caracteristica2 = input("Digite a segunda característica: ")

if horario == "noite" and caracteristica1 == "garras" and caracteristica2 == "evita prata":
    print("É um Lobisomem")
elif (horario in ["dia", "noite"]) and caracteristica1 == "rápido" and caracteristica2 == "ataca em grupo":
    print("É um Nekker")
elif (horario in ["dia", "noite"]) and caracteristica1 == "não tem olhos" and caracteristica2 == "imita vozes humanas":
    print("É um Mímico")
else:
    print("Criatura desconhecida. Prepare-se para o pior. ")

#Escreva um programa que receba o salário de uma pessoa e diga quanto ela pagará apenas de Imposto de Renda. Considere as seguintes faixas de incidência do imposto:

salario = float(input('Digite o salário: R$ '))

if salario <= 2259.20:
    print('Isento do imposto de renda. ')
elif salario == 2259.21 or salario <= 2826.65:
    print('O imposto de renda é de 7,5%. ')
elif salario == 2826.65 or salario <= 3751.05:
    print('O imposto de renda é de 15%. ')
elif salario == 3751.06 or salario <= 4664.68:
    print('O imposto de renda é de 22,5%. ')
else:
    print('O imposto de renda é de 27,5%. ')

#Escreva um programa que peça ao usuário um número entre 1 e 100. O programa deve verificar

numero = int(input("Digite um número entre 1 e 100: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Número divisível por 3 e por 5.")
elif numero % 3 == 0:
    print("Número divisível por 3.")
elif numero % 5 == 0:
    print("Número divisível por 5.")
else:
    print("Número comum.")

#Crie um programa que receba uma senha e verifique sua validade com base nas seguintes condições

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
