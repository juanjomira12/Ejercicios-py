temperaturas = []
frias = []
templadas = []
calientes = []

for i in range(12):
    t = float(input("Temperatura: "))
    temperaturas.append(t)
    if t < 15:
        frias.append(t)
    elif t <= 25:
        templadas.append(t)
    else:
        calientes.append(t)

promedio = sum(temperaturas) / 12
print("Frías:", frias)
print("Templadas:", templadas)
print("Calientes:", calientes)
print("Promedio:", promedio)

if len(frias) > len(templadas) and len(frias) > len(calientes):
    print("Predominan las frías")
elif len(templadas) > len(calientes):
    print("Predominan las templadas")
else:
    print("Predominan las calientes")
