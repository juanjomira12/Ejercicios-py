# Según el precio, se aplica un impuesto del 5 %, 10 % o 19 %.

# Rangos definidos en el programa
LIMITE_BAJO = 50000    # precios menores a este valor pagan 5 %
LIMITE_MEDIO = 200000  # precios hasta este valor pagan 10 %; mayores pagan 19 %


def obtener_tasa(precio):
    """Devuelve el porcentaje de impuesto según el rango del precio."""
    if precio < LIMITE_BAJO:
        return 5
    elif precio <= LIMITE_MEDIO:
        return 10
    else:
        return 19


def calcular_impuesto(precio, tasa):
    """Calcula el valor del impuesto a partir del precio y la tasa."""
    return precio * tasa / 100


def pedir_precio():
    """Pide el precio al usuario hasta que escriba un número válido y positivo."""
    while True:
        entrada = input("Ingrese el precio del producto: ")
        try:
            precio = float(entrada)
            if precio <= 0:
                print("El precio debe ser mayor que cero. Intente de nuevo.")
            else:
                return precio
        except ValueError:
            print("Eso no es un número válido. Intente de nuevo.")


def main():
    print("=== CALCULADORA DE IMPUESTO ===")
    print(f"- Menos de ${LIMITE_BAJO:,.0f}: 5 %")
    print(f"- De ${LIMITE_BAJO:,.0f} a ${LIMITE_MEDIO:,.0f}: 10 %")
    print(f"- Más de ${LIMITE_MEDIO:,.0f}: 19 %")
    print()

    precio = pedir_precio()
    tasa = obtener_tasa(precio)
    impuesto = calcular_impuesto(precio, tasa)
    total = precio + impuesto

    print()
    print(f"Precio:          ${precio:,.2f}")
    print(f"Tasa aplicada:   {tasa} %")
    print(f"Impuesto:        ${impuesto:,.2f}")
    print(f"Total a pagar:   ${total:,.2f}")


if __name__ == "__main__":
    main()