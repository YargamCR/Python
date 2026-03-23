# 1. Función básica

# def saludar(nombre):
# print(f"Hola {nombre}")

# 2. Con retorno


# def sumar(a, b):
# return a + b

import os
personas = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Pedro", "edad": 12}
]


def mostrar_personas(personas):
    print("=== Todas las personas ===")
    for persona in personas:
        for clave, valor in persona.items():
            print(f"{clave}: {valor}")
    print()


def filtrar_mayores(personas):
    print("=== Mayores de edad ===")
    for persona in personas:
        if persona["edad"] >= 18:
            print(f"{persona['nombre']} ({persona['edad']})")


def calcular_promedio(personas):
    print("=== Promedio de edades ===")
    suma = sum(p["edad"] for p in personas)
    promedio = suma / len(personas)
    print(f"Promedio: {promedio}")


def buscar_mayor(personas):
    print("=== Persona con mayor edad ===")
    persona_mayor = personas[0]

    for persona in personas:
        if persona["edad"] > persona_mayor["edad"]:
            persona_mayor = persona
    print(f"{persona_mayor['nombre']} ({persona_mayor['edad']})")


def agregar_persona(personas):
    n = input("Escriba el nuevo nombre de usuario: ")
    e = int(input("Escriba la edad: "))
    personas.append({"nombre": n, "edad": e})


def menu(personas):
    print("\n1. Ver personas")
    print("2. Agregar persona")
    print("3. Mostrar mayores")
    print("4. Promedio")
    print("5. Mayor edad")
    print("6. Salir")

    opcion = int(input("--> "))

    match opcion:
        case 1:
            mostrar_personas(personas)
        case 2:
            agregar_persona(personas)
        case 3:
            filtrar_mayores(personas)
        case 4:
            print(f"Promedio: {calcular_promedio(personas)}")
        case 5:
            p = buscar_mayor(personas)
            print(f"{p['nombre']} ({p['edad']})")
        case 6:
            return False
        case _:
            print("Opción inválida")

    return True


def clear_screen():
    # 'cls' for Windows, 'clear' for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')


# Loop principal
while True:
    continuar = menu(personas)
    if not continuar:
        print("Saliendo...")
        break

    input("\nPresiona ENTER para continuar...")
    clear_screen()
