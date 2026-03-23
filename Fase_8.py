# Fase 8 Python más avanzado (nivel fuerte)
import json
# RETO
"""Guarda personas en JSON
Carga personas al iniciar
Usa list comprehension para:
filtrar mayores
Convierte JSON ↔ objetos Persona"""


personas = []


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad
        }

    def from_dict(data):
        return Persona(data["nombre"], data["edad"])


def cargar_personas():
    try:
        with open("personas.json", "r") as f:
            data = json.load(f)
            return [Persona.from_dict(p) for p in data]

    except FileNotFoundError:
        return []


def guardar_persona(lista):
    with open("personas.json", "w") as f:
        json.dump([p.to_dict()for p in lista], f, indent=4)


def agregar_persona(lista):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    lista.append(Persona(nombre, edad))


def mayores_de_edad(lista):
    return [p for p in lista if p.edad >= 18]


def mostrar(lista):
    for p in lista:
        print(p.nombre, p.edad)


personas = cargar_personas()


def main(personas):

    while True:
        print("\n1. Agregar")
        print("2. Mostrar")
        print("3. Mostrar mayores")
        print("4. Guardar y salir")

        op = input("Opción: ")

        if op == "1":
            agregar_persona(personas)

        elif op == "2":
            mostrar(personas)

        elif op == "3":
            mayores = mayores_de_edad(personas)
            mostrar(mayores)

        elif op == "4":
            guardar_persona(personas)
            break


main(personas)
