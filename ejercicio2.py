print("Conversión de Temperatura")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Elija una opción (1 o 2): ")

if opcion == "1":
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")
elif opcion == "2":
    fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit:.2f} °F equivalen a {celsius:.2f} °C")
else:
    print("Opción no válida. Debe elegir 1 o 2.")
