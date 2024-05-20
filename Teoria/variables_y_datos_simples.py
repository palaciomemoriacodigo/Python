# Variable: Contenedor que permite almacenar datos que pueden ser utilizados y manipulados posteriormente. 

# Generalmente se suelen escribir con elementos alfanuméricos y la separación de las palabras con _ (Ej mi_primera_variable)

# a = 5
# print(a)
# print(type(a))

# _a = 3
# print(_a)

# mi_primera_variable = 'hola mundo'
# print(mi_primera_variable)
# print(type(mi_primera_variable))
# print(a)
# a = 7
# A = 12
# print(a)
# print(A)

# ---

# Datos simples

#  Contienen un solo valor en un momento dado.

# Numeros: int, float, complex 
# Cadenas de texto: str 
# Booleanos: bool

a = 20
b = 8
c = 5.5
d = 3 + 2j

print(type(a))
print(type(c))
print(type(d))

# Operadores aritméticos

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

## Cadenas de texto 

cadena_uno = 'Hola mundo'

cadena_dos = 'Hasta la vista.'

cadena_tres = cadena_uno + " " + cadena_dos
print(cadena_tres)

# Métodos de cadenas

# cadena_tres = cadena_tres.upper()
print(cadena_tres.upper())
print(cadena_tres.lower())
print(cadena_tres.capitalize())
print(cadena_tres.title())
print(cadena_tres.strip())
print(cadena_tres.startswith('Hola'))
print(cadena_tres.endswith('vista.'))
print(cadena_tres)

# bool

# Operadores Lógicos


d = True
e = True
print( d and e)
print( d or e)
print(not d)

# Convertir variable 

a = int(3.14)
print(a)
print(type(a))

b = float("4.5")
print(b)
print(type(b))

c = str(4.5)
print(c)
print(type(c))

d = bool(1)
print(d)
print(type(d))

e = bool(0)
print(e)
print(type(e))

# Asignación múltiple

nombre, edad = "Alberto", 28
print(nombre)
print(type(nombre))
print(edad)
print(type(edad))

x = y = z = 0
print(x)
print(y)
print(z)

