# Solicitar la cantidad de horas
horas_totales = float(input("Ingrese la cantidad de horas: "))

if horas_totales < 0:
    print("Error: La cantidad de horas no puede ser negativa.")
else:
    dias = int(horas_totales // 24)
    
    horas_restantes = int(horas_totales % 24)
    
    parte_decimal = horas_totales - int(horas_totales)
    minutos = int(parte_decimal * 60)
    
    segundos = int((parte_decimal_
