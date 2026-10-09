# 21. Separar números pares e impares. Crear una lista de 15 números enteros y generar dos listas nuevas: una con los pares y otra con los impares.

numeros = [4, 7, 12, 19, 22, 25, 30, 31, 38, 41, 44, 50, 53, 60, 67]


pares = []
impares = []


for numero in numeros:

    if numero % 2 == 0:
        pares.append(numero)
    
    else:
        impares.append(numero)


print("Lista original:", numeros)
print("Números pares:", pares)
print("Números impares:", impares)
