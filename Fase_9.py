# Automatización con JSON (flujo real)
# Paso 1 : Leer el archivo

import json

"""with open("personas.json", "r") as f:
    data = json.load(f)

# Paso 2: Procesar (CLAVE)

mayores = [p for p in data if p["edad"] >= 18]


# Paso 3: Guardar resultado

with open("mayores.json", "w") as f:
    json.dump(mayores, f, indent=4)


Esto que hiciste es:

👉 ETL básico (Extract → Transform → Load)

Extract → leer JSON
Transform → filtrar datos
Load → guardar resultado

💡 Esto es EXACTAMENTE lo que hacen bots RPA

REQUISITOS

Crea un script que:

Lea personas.json
Genere:
mayores.json (>=18)
menores.json (<18)
Muestre en consola:
Cantidad de mayores
Cantidad de menores

"""


with open("personas.json", "r") as f:
    data = json.load(f)


# Procesar
cont_menores = 0

mayores = [p for p in data if p["edad"] >= 18]
menores = [p for p in data if p["edad"] < 18]


print(
    f"Las personas mayores son: {len(mayores)} y las personas menores son: {len(menores)}")


with open("mayores.json", "w") as f:
    json.dump(mayores, f, indent=4)


with open("menores.json", "w") as f:
    json.dump(menores, f, indent=4)
