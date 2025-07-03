# Solicitar la cantidad en millas
millas = float(input("Ingrese la cantidad en millas: "))

if millas < 0:
    print("Error: La cantidad de millas no puede ser negativa.")
else:
    kilometros = millas * 1.60934

    metros = kilometros * 1000

    # Mostrar resultados
    print(f"{millas:.2f} millas equivalen a {kilometros:.2f} kilómetros.")
    print(f"{millas:.2f} millas equivalen a {metros:.2f} metros.")
