#questão 1
nome = "Danilo"
idade = 37
print (f"Meu nome é {nome} e eu tenho {idade} anos.")

#questão 2
a = 5
b = 10
(a,b) = (b,a)
print (f"o valor de a é",a)
print (f"o valor de b é:", b)

#questão 3
pi = 3.14159
r = 4
área = pi*r**2
print (f" A área do circulo de raio 4 é {área}")

#questão 4
inteiro = 14 # tipo int
real = 7.1 # tipo float
texto = "Saudações terraqueos!" # tipo string
print (f"O tipo de inteiro é, {inteiro}")
print (f"O tipo de real é, {real}")
print (f"O tipo de texto é, {texto}")

#questão 5
cálculo = 10+5*2-3**2
print (f"O resultado do cálculo é: {cálculo}") #o resultado seguiu a ordem de precedência, onde 1º = (), 2º = **, 3º = *, /, //, %, 4º = + e -.

#questão 6
celsius = 30
fahrenheit = (celsius*1.8+32)
print (f"A temperatura de {celsius}ºC celsius em Fahrenheit é {fahrenheit}ºF")

#questão 7
x = 3
y = 9
verifique = if x != y and x > 0 and y > 0 
print(f"As variáveis x e y são diferentes e maiores que zero {verifique}.")
else:
print(f"A condição de verifique {verifique} não foi satisfeita")

#questão 8
true = (5>3)
false = (2<1)
expressão = (5>3) and (2<1)
print(f"O resultado da expressão {expressão}")

#questão 9
altura_str = "1.75"
altura_float = float(altura_str)
print (f"A altura convertida é: {altura_float}")

#questão 10
alunos_python = {"Rosana, Lourdes, Dayse"}
alunos_java = {"Vitor, Lourdes, Pedro"}
ambos = alunos_python & alunos_java
só_python = alunos_python - alunos_java
todos = alunos_python | alunos_java
print (f"Alunos que fazer as duas linguas {ambos}")
print (f"Alunos que fazem só python: {só_python}")
print(f"Todos os alunos sem repetição: {todos}")