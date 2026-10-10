calificaciones = [1.0, 2.5, 4.2, 5.0, 2.3, 3.5, 3.0]

suma = 0

for notas in calificaciones:
    suma = suma + notas

promedio = suma / len(calificaciones) # len = número de calificaiones 

print("Promedio De Las Notas: ", promedio)

# Mostrar las Notas superiores e inferiores al promedio

print("Calificaciones superiores e inferioresal promedio:")

for notas in calificaciones:   #for (recorre lista de calificaciones)

    if notas > promedio:
        print(notas, "es superior al promedio")

    elif notas < promedio:
        print(notas, "es inferior al promedio")