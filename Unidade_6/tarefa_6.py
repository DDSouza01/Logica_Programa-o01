#1:Crie um programa que solicite ao usuário que insira 10 palavras. Armazene essas palavras em uma lista. Depois: a) Exiba a lista na ordem inversa. b) Substitua todas as palavras que começam com a letra "a" por ***. c) Exiba a lista modificada.
palavras = []
for i in range(10):
    palavra = input(f"Digite a {i+1}ª palavra: ")
    palavras.append(palavra)
print(palavras[::-1])

for i in range(len(palavras)):
    if palavras[i].lower().startswith("a"):
        palavras[i] = "b"
print(palavras)

#2: Escreva um programa que leia os nomes e as notas de 5 alunos e armazene esses dados em um dicionário, onde a chave seja o nome do aluno e o valor seja a nota. Depois: a) Exiba de maneira organizada o nome e a nota de cada aluno. b) Calcule e exiba de maneira organizada a média da turma. c) Identifique e exiba o nome do aluno de maior nota.

#3: Diferencie tuplas de listas e dicionários.
#Resposta: Lista é um container mutável (podendo sofrer modificações) e armazenar informações ordenadas. As Tuplas são imutáveis e que armazenam múltiplos valores, além de serem indexadas, usando assim elementos com índices. No caso dos Dicionários, já temos uma estrutura de dados que armazena pares (chave-valor). As chaves são imutáveis, já os valores podem ser de qualquer tipo.

#4: Elabore um programa que: Dada a seguinte tupla de frutas:frutas = ("banana", "maçã", "uva", "laranja", "maçã", "melancia", "uva"). Pergunte ao usuário o nome de uma fruta. Informe quantas vezes essa fruta aparece na tupla. Se a fruta estiver presente, mostre o índice da primeira ocorrência. Caso contrário, exiba uma mensagem informando que a fruta não foi encontrada.
