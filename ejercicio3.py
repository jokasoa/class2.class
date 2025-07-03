largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

if largo <= 0 or ancho <= 0:
    print("Error: El largo y el ancho deben ser valores positivos.")
else:
    # Calcular área
    area = largo * ancho

    # Calcular perímetro
    perimetro = 2 * (largo + ancho)

    # Mostrar resultados
    print(f"Área del rectángulo: {area:.2f}")
    print(f"Perímetro del rectángulo: {perimetro:.2f}")
