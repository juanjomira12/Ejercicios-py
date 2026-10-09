num=int(input("Escribe un numero para determinar los numeros primos de hasta ese numero: "))
for i in range(1,num):
    if num % i == 0:
        print(F"{i} es primo")
    else:
        print(F"{i} no es primo")