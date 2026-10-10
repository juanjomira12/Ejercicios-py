num = int(input("Escribe un numero para determinar los numeros primos hasta ese numero: "))

for i in range(2, num + 1):
    es_primo = True
    for divisor in range(2, i):
        if i % divisor == 0:
            es_primo = False
    if es_primo:
        print(f"{i} es primo")
    else:
        print(f"{i} no es primo")