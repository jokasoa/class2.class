# Solicitar datos al usuario
capital = float(input("Ingrese el capital inicial: "))
tasa = float(input("Ingrese la tasa de interés anual (en %): "))
anios = int(input("Ingrese el número de años: "))

if capital <= 0 or tasa < 0 or anios <= 0:
    print("Error: El capital, la tasa y los años deben ser valores positivos.")
else:
    monto = capital * (1 + tasa / 100) ** anios

    print(f"El monto final después de {anios} años es: {monto:.2f}")
