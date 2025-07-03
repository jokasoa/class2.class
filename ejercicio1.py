import math

radio = float(input("Ingrese el radio del círculo: "))

if radio <= 0:
    print("Error: El radio debe ser un valor positivo.")
else:
    area = math.pi * radio ** 2

    perimetro = 2 * math.pi * radio

    # Mostrar los resultados
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
