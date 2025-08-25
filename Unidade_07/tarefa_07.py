#Escreva uma função que receba uma lista de números e retorne o valor mínimo encontrado.
def encontrar_minimo(lista):
    if not lista: 
        return None
    return min(lista)

numeros = [15, 4, 0, 3,-1, 11, -3]
print("O valor mínimo é:", encontrar_minimo(numeros))

#Escreva uma função que receba uma lista de números e um valor inteiro n, e retorne uma nova lista com os n primeiros valores da lista original.
def primeiros_n(lista, n):
    return lista[:n]

numeros = [4, 8, 15, 20, 41, 50]
print(primeiros_n(numeros, 4))
