# 1. Diccionario básico

# persona = {
#  "nombre": "Yordan",
#  "edad": 30,
#  "activo": True
# }

# print(persona["nombre"])


# 2. Recorrer diccionarios

# for clave, valor in persona.items():
# print(clave, valor)


# RETO PRINCIPAL


personas = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Pedro", "edad": 12}
]
print("============== Muestra todas las personas =================")
for diccionario in personas:
    print("Information: ")
    for clave, valor in diccionario.items():
        print(clave, valor)

print("================= Mostrar solo mayores de edad ====================")
for diccionario in personas:
    if diccionario["edad"] > 18:
        print("Mayor de edad: ", diccionario["nombre"], diccionario["edad"])


print("================== Calcular promedio de edades ==================")
suma = 0
for diccionario in personas:
    suma += diccionario["edad"]

prom = suma/len(personas)
print(f"Promedio de edad: {prom}")

print("================= Buscar la persona con mayor edad (sin usar max()) ====================")

persona_mayor = personas[0]

for persona in personas:
    if persona["edad"] > persona_mayor["edad"]:
        persona_mayor = persona

print(f"Persona mayor: {persona_mayor['nombre']} ({persona_mayor['edad']})")
