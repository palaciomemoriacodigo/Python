# Operadores aritméticos

# Permiten realizar operaciones matemáticas 

# Suma (+)
# Resta (-)
# Multiplicación (*)
# División (/)
# División Entera (//)
# Módulo (%)
# Potencia (**)

a = 5
b = 2
c = 2.5
d = 3 + 2j

print(a + b + c)
print(a - b + c)
print(a * b + c)
print(a / b)
print(a // b)
print(a % b)
print(a**b)




# Operadores de Comparación

# Devuelven un booleano

# Igual a (==)
# No igual a (!=)
# Mayor que (>)
# Menor que (<)
# Mayor o igual que (>=)
# Menor o igual que (<=)
print()
a = 5
print( 3 == 4)
print( 4 == 4)
print( 3 != 4)
print( 3 > 4)
print( 3 >= 4)


# Operadores Lógicos

# Se utilizan para combinar sentencias condicionales. Devuelven valores booleanos

# and
# or
# not

print()
d = True
e = False
print( d and e)
print( d or e)
print(not d)


# Ejemplo, el banco solo te da el credito para un coche si pagas de tu bolsillo el 50% del mismo o si pagas el 20% y pones un aval. 
# Sobre el dinero aportado por el banco, te pide un 4%.
print()
dinero = 6000
precio_coche = 25000
aval = True

requisitos = (dinero >= precio_coche * 0.5) or (dinero >= precio_coche * 0.2 and aval == True)
print(requisitos)

dinero_banco = precio_coche - dinero
print(dinero_banco)

dinero_banco_devolucion = dinero_banco * 1.04
print(dinero_banco_devolucion)

