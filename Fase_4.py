# 1. Crear listas

# numeros = [1, 2, 3, 4]


# 2. Acceder a elementos


# print(numeros[0])  # 1


# 3. Recorrer listas

# for numW in numeros:
#  print(numW)

# 4. Metodos Clave

# numeros.append(5)
# numeros.remove(2)
# numeros.sort()


# RETO PRINCIPAL
num = []
cont = len(num)
num_sum = 0
for i in range(0, 5):
    new_num = int(input("Ingrese el numero de la lista: "))
    num.append(new_num)
    num_sum += new_num

for numL in num:
    print(numL)

# BONUS Sin usar max() ni min()
num_max = num[0]
num_min = num[0]

for n in num:
    if n > num_max:
        num_max = n
    if n < num_min:
        num_min = n

print(f"\n El numero maximo es : {num_max}")
print(f"\n El numero minimo es : {num_min}")

num_par = []

for numL in num:
    if numL % 2 == 0:
        num_par.append(numL)

print(f"\n Los numeros pares son:  ", end="")
print(", ".join(str(n) for n in num_par))

prom = num_sum / cont
print(f"\n\n El promedio de los numeros es :  {prom}\n")


# version mejorada

numeros = []
suma = 0

for _ in range(5):
    n = int(input("Ingrese un número: "))
    numeros.append(n)
    suma += n

print("\nLista:", numeros)

# Máximo y mínimo manual
num_max = numeros[0]
num_min = numeros[0]

for n in numeros:
    if n > num_max:
        num_max = n
    if n < num_min:
        num_min = n

print(f"Máximo: {num_max}")
print(f"Mínimo: {num_min}")

# Pares
pares = [n for n in numeros if n % 2 == 0]
print("Pares:", ", ".join(str(n) for n in pares))

# Promedio
promedio = suma / len(numeros)
print(f"Promedio: {promedio}")
