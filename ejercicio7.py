notas = []

print("Ingrese las notas una por una.")
print("Cuando termine, escriba 'fin' para calcular el promedio.")

while True:
    entrada = input("Ingrese una nota o 'fin': ").lower()
    if entrada == "fin":
        break
    try:
        nota = float(entrada)
        if nota < 0:
            print("La nota no puede ser negativa.")
        else:
            notas.append(nota)
    except ValueError:
        print("Entrada inválida. Por favor ingrese un número o 'fin'.")

