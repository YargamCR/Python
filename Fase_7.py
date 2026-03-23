# Fase 7 — POO en Python

# 1. Clase básica

# class Persona:
#  def __init__(self, nombre, edad):
#     self.nombre = nombre
#    self.edad = edad

# 2. Método


# def mostrar(self):
# print(f"{self.nombre} ({self.edad})")

# RETO PRINCIPAL
import os

personas = []


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


def agregar_persona(lista):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    lista.append(Persona(nombre, edad))


def mostrar_personas(lista):
    if len(lista) == 0:
        print("No hay personas registradas")
    else:
        for persona in lista:
            print(persona.nombre, persona.edad)


def es_mayor(personas):
    print("=== Mayores de edad ===")
    for persona in personas:
        if persona.edad >= 18:
            print(persona.nombre, persona.edad)


def calcular_promedio(personas):
    print("=== Promedio de edades ===")
    suma = sum(persona.edad for persona in personas)
    promedio = suma / len(personas)
    print(f"Promedio: {promedio}")


def menu(personas):
    print("\n1. Ver personas")
    print("2. Agregar persona")
    print("3. Mostrar mayores")
    print("4. Promedio")
    print("6. Salir")

    opcion = int(input("--> "))

    match opcion:
        case 1:
            mostrar_personas(personas)
        case 2:
            agregar_persona(personas)
        case 3:
            es_mayor(personas)
        case 4:
            calcular_promedio(personas)
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


# Correction

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor(self):
        return self.edad >= 18


def agregar_persona(lista):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    lista.append(Persona(nombre, edad))


def mostrar_personas(lista):
    if not lista:
        print("No hay personas registradas")
        return

    for persona in lista:
        print(f"{persona.nombre} ({persona.edad})")


def mostrar_mayores(lista):
    print("=== Mayores de edad ===")
    for persona in lista:
        if persona.es_mayor():
            print(f"{persona.nombre} ({persona.edad})")


def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(p.edad for p in lista) / len(lista)


def menu(personas):
    print("\n1. Ver personas")
    print("2. Agregar persona")
    print("3. Mostrar mayores")
    print("4. Promedio")
    print("5. Salir")

    opcion = int(input("--> "))

    match opcion:
        case 1:
            mostrar_personas(personas)
        case 2:
            agregar_persona(personas)
        case 3:
            mostrar_mayores(personas)
        case 4:
            print(f"Promedio: {calcular_promedio(personas)}")
        case 5:
            return False
        case _:
            print("Opción inválida")

    return True
