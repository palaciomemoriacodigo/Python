primera_cadena = ' esto es Una Cadena de texto y esto tiene espacios  '
cadena_sin_espacios = 'estoesUnaCadenadetextosinespacios'
cadena_sin_espacios_con_num = 'estoesUnaCadenadetextosinespacios3'
saludo_mal = "¡ola! ¡ola! ¿Qué haces?"
cadena_numeros = '98654'
cadena_mayus = 'HOLA'
cadena_minus = 'hola'
Cadena_title = 'Ese Arbol Es El Bueno'


# format()

# Formatea la cadena usando marcadores de posición.

print()
nombre = "Jack"
edad = 25
cadena_formateada = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(cadena_formateada)  

# f-strings (formatted string literals)
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

w = 4
y = 6
print(f'La suma de {w} y {y} es: {w+y}.')

print(f'El texto en mayúsculas es: {primera_cadena.upper()}')


# format_map()

# Similar a format(), pero usa un diccionario.

print()
datos = {"nombre": "Jack", "edad": 25}
cadena_formateada = "Hola, mi nombre es {nombre} y tengo {edad} años.".format_map(datos)
print(cadena_formateada) 


# upper()

# Devuelve la cadena con todos sus caracteres a mayúscula

print()
print(primera_cadena.upper())
    
# lower()

# Devuelve la cadena con todos sus caracteres a minúscula

print()
print(primera_cadena.lower())
    
# capitalize()

# Devuelve la cadena con su primer carácter en mayúscula

print()
print(primera_cadena.capitalize())
print(cadena_minus.capitalize())
    
# title()

# Devuelve la cadena con el primer carácter de cada palabra en mayúscula

print()
print(primera_cadena.title())

# strip()

# Borra todos los espacios por delante y detrás de una cadena y la devuelve

print()
print(primera_cadena.strip())
    
# # count()

# # Devuelve una cuenta de las veces que aparece una subcadena en la cadena

print()
print(primera_cadena.count('Una'))
print(primera_cadena.count('una'))
    
# # find()

# # Devuelve el índice en el que aparece la subcadena (-1 si no aparece)
 
print()
print(primera_cadena.find('esto')) 
print(primera_cadena.find('Esto')) 
    
# # rfind()

# # Devuelve el índice en el que aparece la subcadena, empezando por el final

print()
print(primera_cadena.rfind('esto')) 
print(primera_cadena.rfind('Esto')) 
    
# # isdigit()

# # Devuelve True si la cadena es todo números (False en caso contrario)

print()
print(primera_cadena.isdigit())
print(cadena_numeros.isdigit())

# # isalnum()

# # Devuelve True si la cadena es todo números o carácteres alfabéticos

print()
print(primera_cadena.isalnum())
print(cadena_sin_espacios.isalnum())  

# # isalpha()

# # Devuelve True si la cadena es todo carácteres alfabéticos

print()
print(cadena_sin_espacios_con_num.isalpha())
print(cadena_sin_espacios.isalpha()) 
   
# # islower()

# # Devuelve True si la cadena es todo minúsculas

print()
print(cadena_minus.islower())
print(primera_cadena.islower()) 

# # isupper()

# # Devuelve True si la cadena es todo mayúsculas

print()
print(cadena_mayus.isupper())
print(primera_cadena.isupper()) 
    
# # istitle()

# # Devuelve True si la primera letra de cada palabra es mayúscula

print()
print(Cadena_title.istitle())
print(primera_cadena.istitle())

# # startswith()

# # Devuelve True si la cadena empieza con una subcadena

print()
print(primera_cadena.startswith(' esto'))
print(primera_cadena.startswith('esto'))


# # endswith()

# Devuelve True si la cadena acaba con una subcadena

print()
print(primera_cadena.endswith('  '))
print(primera_cadena.endswith('espacios  '))

# # split()

# # Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista

print()
primera_cadena_split = primera_cadena.split()
primera_cadena_split_indice = primera_cadena.split()[3]
print(type(primera_cadena_split))
print(primera_cadena_split)
print(primera_cadena_split_indice)
print(primera_cadena_split[3])
    
# # join()

# # Une todos los caracteres de una cadena utilizando un caracter de unión

print()
print(" ".join("Se busca"))
print(" ".join(saludo_mal))

# # replace()

# # Reemplaza una subcadena de una cadena por otra y la devuelve

print(saludo_mal.replace('ola','hola'))

# # swapcase()

# # Devuelve la cadena con todos sus caracteres en mayúscula convertidos a minúscula y viceversa.

print(primera_cadena.swapcase())

# # zfill()

# # Devuelve la cadena rellenada con ceros a la izquierda hasta alcanzar el ancho especificado.

print()
numero = "17"
numero_con_ceros = numero.zfill(4)  
print(numero_con_ceros) 

# # removeprefix()

# # Devuelve una copia de la cadena con el prefijo especificado eliminado si comienza con dicho prefijo.

print()
material_1 = 'PE-5004'
material_1 = material_1.removeprefix("PE-")
print(material_1)


# # removesuffix()

# Devuelve una copia de la cadena con el sufijo especificado eliminado si termina con dicho sufijo.

print()
material_1 = '5004-PE'
material_1 = material_1.removesuffix("-PE")
print(material_1)
