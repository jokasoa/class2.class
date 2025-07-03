while True:
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))

    potencia = base ** exponente

    print(f"{base} elevado a la {exponente} es {potencia}")

    continuar = input("¿Desea calcular otra potencia? (s/n): ").lower()
    if continuar != "s":
        print("Programa finalizado.")
        break
