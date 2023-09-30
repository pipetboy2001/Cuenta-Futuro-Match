# Función para determinar el rango según el saldo
def determinar_rango(saldo):
    if 1000 <= saldo <= 50000:
        return "Bronce"
    elif 50001 <= saldo <= 200000:
        return "Plata"
    elif 200001 <= saldo <= 800000:
        return "Oro"
    elif 800001 <= saldo <= 4000000:
        return "Platino"
    elif saldo > 4000000:
        return "Diamante"
    else:
        return "Saldo inválido"

# Función para calcular las ganancias mantenidas en un tiempo
def calcular_ganancias_mantenidas(saldo, meses):
    tasa_anual = 0
    if 1000 <= saldo <= 50000:
        tasa_anual = 0.78
    elif 50001 <= saldo <= 200000:
        tasa_anual = 3.45
    elif 200001 <= saldo <= 800000:
        tasa_anual = 4.54
    elif 800001 <= saldo <= 4000000:
        tasa_anual = 5.67
    elif saldo > 4000000:
        tasa_anual = 6.77

    ganancia_mensual = saldo * tasa_anual / 100 / 12
    ganancia_total = ganancia_mensual * meses
    rango = determinar_rango(saldo)
    return ganancia_mensual, ganancia_total, rango

# Función para calcular las ganancias abonando mes a mes
def calcular_ganancias_abonando(saldo_inicial, abono_mensual, meses):
    tasa_anual = 0
    if 1000 <= saldo_inicial <= 50000:
        tasa_anual = 0.78
    elif 50001 <= saldo_inicial <= 200000:
        tasa_anual = 3.45
    elif 200001 <= saldo_inicial <= 800000:
        tasa_anual = 4.54
    elif 800001 <= saldo_inicial <= 4000000:
        tasa_anual = 5.67
    elif saldo_inicial > 4000000:
        tasa_anual = 6.77

    ganancia_mensual = (saldo_inicial + abono_mensual / 2) * tasa_anual / 100 / 12
    ganancia_total_interes = ganancia_mensual * (meses - 1)  # Ganancia por interés sin contar el último mes
    saldo_final = saldo_inicial + abono_mensual * meses
    ganancia_total_guardar = saldo_final * tasa_anual / 100 / 12  # Ganancia por guardar el último mes
    ganancia_total = ganancia_total_interes + ganancia_total_guardar
    rango = determinar_rango(saldo_final)
    return ganancia_total, rango

# Bucle principal del programa
while True:
    print("Cuenta futuro Match - Escoge qué hacer:")
    print("1.- Calcular ganancias mantenidas en un tiempo")
    print("2.- Calcular ganancias abonando mes a mes")
    print("3.- Salir")
    opcion = input("Ingresa tu opción: ")

    if opcion == "1":
        try:
            saldo = float(input("Ingresa tu saldo en la cuenta futuro: "))
            meses = int(input("Ingresa la cantidad de meses que mantendrás el saldo: "))
            ganancia_mensual, ganancia_total, rango = calcular_ganancias_mantenidas(saldo, meses)
            print(f"Ganancia mensual: {ganancia_mensual:.2f}")
            print(f"Ganancia total en {meses} meses: {ganancia_total:.2f}")
            print(f"Rango: {rango}")
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos.")

    elif opcion == "2":
        try:
            saldo_inicial = float(input("Ingresa tu saldo inicial en la cuenta futuro: "))
            abono_mensual = float(input("Ingresa la cantidad que abonarás mensualmente: "))
            meses = int(input("Ingresa la cantidad de meses que mantendrás el saldo: "))
            ganancia_total, rango = calcular_ganancias_abonando(saldo_inicial, abono_mensual, meses)
            print(f"Ganancia total abonando mes a mes en {meses} meses: {ganancia_total:.2f}")
            print(f"Rango después de {meses} meses: {rango}")
        except ValueError:
            print("Por favor, ingresa valores numéricos válidos.")

    elif opcion == "3":
        print("Gracias por usar Cuenta futuro Match. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida (1, 2 o 3).")
