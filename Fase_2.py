# Fase 2 Control de flujo

# 1. Condicionales

edad = 18

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# 2. if / elif / else

nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# 3. Operadores lógicos

edad = 20
tiene_id = True

if edad >= 18 and tiene_id:
    print("Puede entrar")

# 4.RETO PRINCIPAL

edad_e = int(input("Ingrese la edad: "))
identification_e = input("Cuenta con identificacion? (si o no): ").lower()
idetification_test = False

identification_e = idetification_test == True


if idetification_test == True and edad_e >= 18:
    print("Puedes entrar al concierto")
else:
    print("No tienes accesso, disculpa")


# RETO EXTRA

nota = int(input("Ingresa tu nota: "))


if nota >= 90:
    print(f"Nota: {nota}, Tu nota es exelente!!")
elif nota <= 89 and nota >= 70:
    print(f"Nota: {nota}, Estas aprobado felicidades!")
elif nota <= 69:
    print(f"Nota: {nota}, reprobaste, sigue esforzandote")


# Mejoradas

edad = int(input("Ingrese la edad: "))
identificacion = input("Cuenta con identificacion? (si o no): ").lower()

tiene_id = identificacion == "si"

if edad >= 18 and tiene_id:
    print("Puedes entrar al concierto")
else:
    print("No tienes acceso, disculpa")


nota = int(input("Ingresa tu nota: "))

if nota < 0 or nota > 100:
    print("Error: nota inválida")
elif nota >= 90:
    print(f"Nota: {nota}, tu nota es excelente")
elif 70 <= nota <= 89:
    print(f"Nota: {nota}, estás aprobado")
else:
    print(f"Nota: {nota}, reprobaste")
