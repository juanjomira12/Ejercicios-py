print("=== EJERCICIOS EQUIPO COCOSETES ===")

while True:
    print("\nAlgoritmos disponibles:")
    print("6  - Clasificacion de temperaturas")
    print("9  - Calculadora de impuesto")
    print("18 - Numeros primos")
    print("21 - Pares e impares")
    print("23 - Promedio de calificaciones")

    opcion = input("\nQue algoritmo quieres ver? ")

    if opcion == "6":
        exec(open("ejercicio6.py").read())
    elif opcion == "9":
        exec(open("ejercicio_9.py").read())
    elif opcion == "18":
        exec(open("primosgit.py").read())
    elif opcion == "21":
        exec(open("ejercicio-21.py").read())
    elif opcion == "23":
        exec(open("ejercicio23.py").read())
    else:
        print("Opcion no valida")

    seguir = input("\nQuieres ver otro algoritmo o cerrar la sesion? (otro/cerrar): ")
    if seguir == "cerrar":
        print("Sesion cerrada")
        break
