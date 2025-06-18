# operaciones_anio_nacimiento.py

def es_bisiesto(year):
    """
    Implementa una función para determinar si un año es bisiesto.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def procesar_anios_nacimiento(anios_nacimiento):
    """
    Procesa una lista de años de nacimiento para realizar análisis y operaciones.
    """
    print("\n--- Procesamiento de Años de Nacimiento ---")

    pares = 0
    impares = 0
    anios_set = set()
    edades_actuales_set = set()

    for anio in anios_nacimiento:
        anios_set.add(anio)
        if anio % 2 == 0:
            pares += 1
        else:
            impares += 1
        # El año actual es 2025, de acuerdo a la información provista.
        edad_actual = 2025 - anio
        edades_actuales_set.add(edad_actual)

    print(f"Cantidad de nacidos en años pares: {pares}")
    print(f"Cantidad de nacidos en años impares: {impares}")

    todos_despues_2000 = True
    for anio in anios_nacimiento:
        if anio <= 2000:
            todos_despues_2000 = False
            break
    if todos_despues_2000:
        print("Condición: ¡Grupo Z!")
    else:
        print("Condición: No todos nacieron después del 2000.")

    alguno_bisiesto = False
    for anio in anios_nacimiento:
        if es_bisiesto(anio):
            alguno_bisiesto = True
            break
    if alguno_bisiesto:
        print("Condición: ¡Tenemos un año especial (alguno nació en año bisiesto)!")
    else:
        print("Condición: Ninguno nació en año bisiesto.")

    print("\n--- Producto Cartesiano (Años de Nacimiento x Edades Actuales) ---")
    producto_cartesiano = [(anio, edad) for anio in sorted(list(anios_set)) for edad in sorted(list(edades_actuales_set))]
    print(f"Años únicos: {sorted(list(anios_set))}")
    print(f"Edades actuales únicas (aprox.): {sorted(list(edades_actuales_set))}")
    print(f"Producto Cartesiano: {producto_cartesiano}")