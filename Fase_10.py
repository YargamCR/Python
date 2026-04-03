import requests
import json


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    data = response.json()
else:
    print("Error en la petición")
    exit()

"""requests.get() → hace petición a internet
.json() → convierte respuesta a lista/dict
data → ya es como trabajar con JSON local"""

for user in data:
    print(user["name"], user["email"])

info_user = [{"name": p["name"], "email": p["email"]} for p in data]
email_org = [p["email"] for p in data if p["email"].endswith(".org")]

with open("usuarios.json", "w") as f:
    json.dump(info_user, f, indent=4)

print(email_org)
