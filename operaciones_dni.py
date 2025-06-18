# operaciones_dni.py

def procesar_dnis(dnis):
    """
    Procesa una lista de DNIs para realizar operaciones de conjuntos y análisis de dígitos.
    """
    conjuntos_dnis = []
    print("\n--- Procesamiento de DNIs ---")
    for i, dni_str in enumerate(dnis):
        conjunto = set(int(d) for d in dni_str)
        conjuntos_dnis.append(conjunto)
        print(f"Conjunto DNI{i+1}: {conjunto}")

    if len(conjuntos_dnis) >= 2:
        d1 = conjuntos_dnis[0]
        d2 = conjuntos_dnis[1]

        union = d1.union(d2)
        interseccion = d1.intersection(d2)
        diferencia_d1_d2 = d1.difference(d2)
        diferencia_d2_d1 = d2.difference(d1)
        diferencia_simetrica = d1.symmetric_difference(d2)

        print(f"\nUnión (D1 U D2): {union}")
        print(f"Intersección (D1 ∩ D2): {interseccion}")
        print(f"Diferencia (D1 - D2): {diferencia_d1_d2}")
        print(f"Diferencia (D2 - D1): {diferencia_d2_d1}")
        print(f"Diferencia Simétrica (D1 Δ D2): {diferencia_simetrica}")

    print("\n--- Frecuencia de dígitos por DNI ---")
    for i, dni_str in enumerate(dnis):
        frecuencia = {}
        for digito in dni_str:
            frecuencia[digito] = frecuencia.get(digito, 0) + 1
        print(f"Frecuencia de dígitos en DNI {i+1} ({dni_str}): {frecuencia}")

    print("\n--- Suma de dígitos por DNI ---")
    for i, dni_str in enumerate(dnis):
        suma_digitos = sum(int(d) for d in dni_str)
        print(f"Suma de los dígitos del DNI {i+1} ({dni_str}): {suma_digitos}")

    print("\n--- Evaluación de Condiciones Lógicas ---")

    if len(conjuntos_dnis) >= 2:
        interseccion_total = conjuntos_dnis[0]
        for j in range(1, len(conjuntos_dnis)):
            interseccion_total = interseccion_total.intersection(conjuntos_dnis[j])

        if 0 in interseccion_total:
            print(f"Condición Lógica 1: El dígito 0 está presente en la intersección de todos los conjuntos. Resultado: 'Dígito común'.")
        else:
            print(f"Condición Lógica 1: El dígito 0 NO está presente en la intersección de todos los conjuntos.")

        d1 = conjuntos_dnis[0]
        d2 = conjuntos_dnis[1]
        if len(d1) > len(d2):
            print(f"Condición Lógica 2: La cantidad de elementos del Conjunto DNI1 ({len(d1)}) es mayor que la del Conjunto DNI2 ({len(d2)}). Resultado: 'El primer DNI tiene mayor diversidad de dígitos'.")
        else:
            print(f"Condición Lógica 2: La cantidad de elementos del Conjunto DNI1 ({len(d1)}) NO es mayor que la del Conjunto DNI2 ({len(d2)}).")

    for i, conjunto in enumerate(conjuntos_dnis):
        if len(conjunto) > 6:
            print(f"Condición Adicional (Diversidad numérica alta): El Conjunto DNI{i+1} tiene más de 6 elementos ({len(conjunto)} elementos).")
            break
    else:
        print("Condición Adicional (Diversidad numérica alta): Ningún conjunto tiene más de 6 elementos.")