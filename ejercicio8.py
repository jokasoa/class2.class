# Solicitar datos al usuario
precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento (0 a 100): "))

if precio <= 0:
    print("Error: El precio debe ser un valor positivo.")
elif descuento < 0 or descuento > 100:
    print("Error: El porcentaje de descuent
