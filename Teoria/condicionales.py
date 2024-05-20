import numpy as np

###
# Condicionales
###

# Los condicionales permiten a los programas tomar decisiones basadas en condiciones. 

# if Statement
# El if statement se usa para evaluar una condición. Si la condición es True, se ejecuta el bloque de código indentado que sigue al if

print()
nota = 6.5
if nota >= 5:
    print("Aprobado")
    
# else Statement
# El else statement proporciona una alternativa que se ejecuta si la condición del if es False.

print()
nota = 4
if nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
    

# elif Statement
# El elif statement (abreviatura de "else if") permite verificar múltiples condiciones. Se ejecuta el primer bloque de código cuyo elif statement evalúa como True.

print()
nota = 10
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Suspenso")


# Operadores lógicos

print()
nota = 4.5
practicas = True

if nota >= 9 and practicas == True:
    print("Sobresaliente")
elif nota >= 7 and practicas == True:
    print("Notable")
elif nota >= 6 and practicas == True:
    print("Bien")
elif nota >= 5 and practicas == True:
    print("Suficiente")
else:
    print("Suspenso")
    
print()
x = 120
if 10 <= x <= 100:
    print("x está entre 10 y 100")
else:
    print("No se encuentra en el intervalo")


###
# Anidación de Condicionales
###

# Los condicionales pueden anidarse dentro de otros condicionales para evaluar condiciones más complejas.

print()
nota = 4
practicas = True

if practicas == True:
    if nota >= 9:
        print("Sobresaliente")
    elif nota >= 7:
        print("Notable")
    elif nota >= 6:
        print("Bien")
    elif nota >= 5:
        print("Suficiente")
    else:
        print("Suspenso con practicas.")
else:
    print("Suspenso, no tiene practicas.")


###
# Operador ternario
###

nota = 6.5
practicas = True

print()
mensaje = "Aprobado" if nota >= 5 and practicas == True else "Suspenso"
print(mensaje)

print()
edad = 18
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

###
# Condicionales Complejos
###

nota = 4
nota_practicas = 8
print()
if (nota >= 5 and nota_practicas == True) or (nota >= 4 and nota_practicas >= 7):
    print("Aprobado")
else:
    print("Suspenso")

###
# in junto a condicionales
###

letra = 'z'
if letra in 'aeiou':
    print(f"{letra} es una vocal")
else:
    print(f"{letra} no es una vocal")
    
###
# Otros ejemplos
###

numero = 5
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
    
    
edad = 35
if edad < 13:
    print("Niño")
elif edad < 20:
    print("Adolescente")
elif edad < 65:
    print("Adulto")
else:
    print("Anciano")



# ejemplo_input = float(input('Dame un numero del 1 al 10: '))
# print(f'El numero aportado es: {ejemplo_input}')


# print()
# print("Menú Principal")
# print("1. Saludar")
# print("2. Sumar dos números")
# print("3. Restar dos números")
# print("4. Salir")
# print()

# opcion = input("Selecciona una opción (1-4): ")
# if opcion == '1':
#     print("Hola!")
#     print()
# elif opcion == '2':
#     numero1 = float(input("Introduce el primer número: "))
#     numero2 = float(input("Introduce el segundo número: "))
#     suma = numero1 + numero2
#     print(f"La suma de {numero1} y {numero2} es {suma}.")
#     print()
# elif opcion == '3':
#     numero1 = float(input("Introduce el primer número: "))
#     numero2 = float(input("Introduce el segundo número: "))
#     resta = numero1 - numero2
#     print(f"La resta de {numero1} y {numero2} es {resta}.")
#     print()
# elif opcion == '4':
#     print("¡Adiós!")
# else:
#     print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
#     print()



# print()
# print("Menú Principal")
# print("1. Saludar")
# print("2. Crear un número aleatorio")
# print("3. Crear un número aleatorio entero de 1 a 100")
# print("4. Salir")
# print()

# opcion = input("Selecciona una opción (1-4): ")

# if opcion == '1':
#     print("Hola!")
#     print()

# elif opcion == '2':
#     numero_aleatorio = np.random.random()
#     print(f"El número aleatorio generado es {numero_aleatorio}.")
#     print()

# elif opcion == '3':
#     numero_aleatorio_entero = np.random.randint(1, 101)
#     print(f"El número aleatorio entero generado es {numero_aleatorio_entero}.")
#     print()

# elif opcion == '4':
#     print("¡Adiós!")

# else:
#     print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
#     print()