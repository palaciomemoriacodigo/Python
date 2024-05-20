# Colecciones

# Son aquellos que pueden contener múltiples valores o colecciones de datos

# Tipos principales:
    # - Listas (list)
    # - Tuplas (tuple)
    # - Diccionarios (dict)
    # - Conjuntos (set)

# Características

# Pueden almacenar múltiples valores y tipos de datos

# Permiten realizar operaciones de búsqueda, ordenamiento y manipulación de datos en masa.

#####
### Listas
#####

# Características

# Mutable: Los elementos dentro de una lista pueden cambiarse.

# Indexada: Los elementos se pueden acceder mediante índices numéricos.

# Permite duplicados: Una lista puede contener elementos duplicados.


# Ejemplo 

lista = ['perro', 'gato', 'lechuza']
print(type(lista))
lista.append('gallina')
lista.extend(['perro',"gallina", "gato"])
print(lista)

print()
lista.remove('gallina')
print(lista)

print()
lista[2] = 'gallina'
print(lista)

print()
lista.append(['perro', 'perro', 'gato'])
print(lista)

print()
lista_mezcla = ['a',1,True]
print(lista_mezcla)

print()
print(lista[6])

print()
print(lista[6][0])

#####
### Tuplas
#####

# Características

# Inmutable: Una vez creada, sus elementos no pueden cambiarse.

# Ordenada

# Indexada: Similar a las listas, los elementos se acceden mediante índices numéricos.

# Permite duplicados: Una tupla puede contener elementos duplicados.

# Menor uso de memoria: Consume menos memoria comparado con listas.

# Ejemplo 

print()
tupla = ('gato', 'perro', 'lobo')
print(tupla)
print(type(tupla))

# print()
# tupla[0] = 'perro'

print()
tupla_convertida_a_lista = list(tupla)
print(type(tupla_convertida_a_lista))
print(tupla_convertida_a_lista)

print()
lista_convertida_a_tupla = tuple(tupla_convertida_a_lista)
print(type(lista_convertida_a_tupla))
print(lista_convertida_a_tupla)

print()
tupla_mezcla = ('a',1,True)
print(tupla_mezcla)

print()
tupla_anidada = ((1,2),3,(8,19))
print(tupla_anidada[0])
print(tupla_anidada[0][1])

#####
### Diccionarios
#####

# Características

# Mutable: Se pueden añadir, cambiar o eliminar pares clave-valor.

# Desordenado: Los elementos no tienen un orden específico.

# Claves únicas: Cada clave debe ser única, aunque los valores pueden repetirse.

# Acceso rápido: Acceso a valores mediante claves, lo que hace las búsquedas muy rápidas.

# Ejemplo

diccionario = {"nombre": 'snowball', 'edad':4, 'raza':'Border Collie'}

print(diccionario['nombre'])

diccionario['edad'] = 5
print(diccionario['edad'])

diccionario["ciudad"] = "Murcia"
print(diccionario)

print()
diccionario.pop("ciudad")
print(diccionario)

print()
print(diccionario.keys())    
print(diccionario.values())  
print(diccionario.items())

dict_claves_convertido_lista = list(diccionario.keys())
dict_valores_convertido_lista = list(diccionario.values())
dict_items_convertido_lista = list(diccionario.items())
print(dict_claves_convertido_lista)
print(dict_valores_convertido_lista)
print(dict_items_convertido_lista)
print(type(dict_items_convertido_lista))
print(type(dict_items_convertido_lista[0]))

#####
### Conjuntos
#####

# Características

# Mutable: Los elementos pueden añadirse o eliminarse.

# No permite duplicados: Todos los elementos son únicos.

# Desordenado: No se garantiza el orden de los elementos.

# Permite operaciones de conjuntos (unión, intersección, diferencia, etc).

# Permite eliminar duplicados.

print()
conjunto_a = {1,3,5,7,9}
conjunto_b = {2,4,6,8,10}
conjunto_c = {2,3,4,5}
print(conjunto_a)
print(type(conjunto_a))

conjunto_a = set([1,3,5,7,9])
print(conjunto_a)
print(type(conjunto_a))

conjunto_con_list_dup = set([1,1,1,2,2,2,3,5,5])
print(conjunto_con_list_dup)

print()
conjunto_a.add(11)
print(conjunto_a)

print()
conjunto_a.remove(9)
print(conjunto_a)

print()
int_set_ac = conjunto_a.intersection(conjunto_c)
print(int_set_ac)