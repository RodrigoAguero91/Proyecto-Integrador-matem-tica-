# programa_principal.py

# Importamos las funciones de los otros archivos
from operaciones_dni import procesar_dnis
from operaciones_anio_nacimiento import procesar_anios_nacimiento

def main():
    print("¡Bienvenido al Trabajo Integrador de Matemática !")

    # Parte A: Operaciones con DNIs
    dnis_input = []
    while True:
        try:
            num_integrantes = int(input("Ingrese el número de integrantes del grupo (ej: 2): "))
            if num_integrantes > 0:
                break
            else:
                print("El número de integrantes debe ser mayor que 0.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    for i in range(num_integrantes):
        dni = input(f"Ingrese el DNI del Integrante {i+1}: ")
        dnis_input.append(dni)

    procesar_dnis(dnis_input) # Llamada a la función del otro archivo

    # Parte B: Operaciones con años de nacimiento
    anios_nacimiento_input = []
    print("\nAhora ingrese los años de nacimiento (Si dos o más integrantes del grupo tienen el mismo año, ingresar algún dato ficticio, según el caso):")
    for i in range(num_integrantes):
        while True:
            try:
                anio = int(input(f"Ingrese el año de nacimiento del Integrante {i+1}: "))
                anios_nacimiento_input.append(anio)
                break
            except ValueError:
                print("Por favor, ingrese un año válido (número entero).")

    procesar_anios_nacimiento(anios_nacimiento_input) # Llamada a la función del otro archivo

if __name__ == "__main__":
    main()