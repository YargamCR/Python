# Fase 3 Bucles (loops)


# 1. For loop
# for i in range(5):
# print(i)


# 2. While loop


# contador = 0

# while contador < 5:
# print(contador)
# contador += 1

# 3. Recorrer listas

# numeros = [10, 20, 30]

# for num in numeros:
# print(num)


# RETO PRINCIPAL

print("Calculadora del 1 al 10")
num = int(input("Cual tabla desea saber, escriba el number que desea ver: "))

for i in range(1, 11):
    multi = num * i
    print(f"{num} x {i} = {multi}")


# RETO EXTRA + BONUS

cont_negativos = 0
cont_positivos = 0
suma = 0
print("SUMAS INFINITAS, ESCRIBA '0' PARA TERMINAR")
print("Ingrese todos los numeros que desea sumar")
while True:
    num_sumas = int(input("Numero: "))
    suma = num_sumas + suma

    if num_sumas == 0:
        break
    if num_sumas > 0:
        cont_positivos += 1
    elif num_sumas < 0:
        cont_negativos += 1

print(f"La suma total es: {suma}")

print(f"La cantidad de numero positivos es: {cont_positivos}")
print(f"La cantidad de numero negativos es: {cont_negativos}")
