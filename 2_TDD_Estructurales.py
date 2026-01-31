

# *************************** 1. LAS LISTAS: son array, vector, arreglo, matrices.
# son colecciones ordenadas de datos, el orden es secuencial y preciso.
# Cada dato coleccionado es un elemento.
# La lista puede contener cualquier tipo de dato, incluso otras listas (matrices).
# Al elemento se accede por su posición (índice, que comienza desde 0), para:
# √ Obtenerlo, √ Reasignale valor, √ Eliminarlo... Entonces las listas son mutables.
#!❌ Acceder a una posición fuera de rango, genera un error.


#?⭐ Creación de una lista: Se representa, conteniendo a sus elementos entre corchetes []
lista_numeros = [1,2,3,4,'5', False]
print(lista_numeros) # [1, 2, 3, 4, '5', False]

#& 💡Utilidad de las listas: 
# Entre otras utilidades, es la forma de empaquetar un conjunto de data relacionada para, 
# por ejemplo, transportarla de un sistema a otro: https://jsonplaceholder.typicode.com/users


#?⭐ Acceso: medidante su índice (posición)
print(lista_numeros[5]) # False → Retorna el elemento en la posición 5
print(lista_numeros[-2]) # "5"  → Con indices negativos, accedemos desde el final (-1 es el último ele)

# #?⭐ Saber el TDD de las Listas
print('TDD de una lista', type(lista_numeros)) # <class 'list'>
print('TDD del ultimo elemento', type(lista_numeros[-1])) # <class 'bool'>


#?⭐ Modificación de un elemento
lista_numeros[-2] = 5
print(lista_numeros) # [1, 2, 3, 4, 5, False]

#?⭐ Longitud
print(len(lista_numeros)) #6

#?⭐ ❌ Acceder o Modificar una posición fuera de rango, genera un error.
#lista_numeros[6] = 'ultimo'  #! IndexError: list assignment index out of range
print(lista_numeros)

#? 🤔🙋🏻‍♂️⁉️entonces como agregar elementos a una lista?

#?⭐ Metodo append(ele): agrega su parametro al final de la lista.
lista_numeros.append('ultimo')
print(lista_numeros) # [1, 2, 3, 4, 5, False, 'ultimo']

#?⭐ Metodo pop([index]): elimina y retorna el elemento en la posición parametro 
# (si no se le pasa, elimina el último)
ele_eliminado = lista_numeros.pop()
print('Elemento eliminado:', ele_eliminado) # 'ultimo'
print(lista_numeros) # [1, 2, 3, 4, 5, False]

#?⭐ Metodo remove(ele): elimina la primera ocurrencia del elemento parametro.
lista_numeros.append(5)
print(lista_numeros) # [1, 2, 3, 4, 5, False, 5]
lista_numeros.remove(5)
print(lista_numeros) # [1, 2, 3, 4, False, 5]

#?⭐ Metodo sort(): ordena la lista in-place (modifica la lista original), retorna None.
# Funciona bien si todos los elementos son del mismo comparables.
lista_numeros.sort()
print(lista_numeros) #[False, 1, 2, 3, 4, 5]
lista_numeros.sort( reverse=True ) # ordena en orden descendente
print(lista_numeros) # [5, 4, 3, 2, 1, False]

#?⭐ Metodo index(ele, [start, end]): retorna el índice o posision de la 
# primera ocurrencia del elemento parametro.
print(lista_numeros.index(5)) # 0
print(lista_numeros.index(3, 1, 5)) # 2 → Busco y retorno el 3 entre las posiciones 1 y 5.

# TODO: 🧠TAREA:Existen otros metodos de las listas, te invito a que los investigues
# y pruebes. Los usaremos mas adelante.


# *************************** 2. TUPLAS: (tuple)
# Son colecciones ordenadas de datos, el orden es secuencial y preciso.
# Cada dato coleccionado es un elemento.
# A diferencia de las listas, son inmutables, no se pueden modificar, agregar o eliminar elementos.
# si ese es tu objetivo, haz un casting a lista.
# #! Acceder a una posición fuera de rango, genera un error.

# #?⭐ Creación de una tupla: Se representa, conteniendo a sus elementos entre paréntesis ()
tupla_numeros = (1,2,3,4,'5', False) #Con parentesis.
print(tupla_numeros)

tupla = 1, 2, True # Otra forma de crear tuplas, SIN los parentesis.
print(tupla)

# #& 💡Utilidad de las tuplas: 
# # Entre otras utilidades, es la forma de empaquetar un conjunto de data 
# que por seguridad no deseamos que sea modificable.

# #?⭐ Acceso: meidante su índice (posición)
print(tupla_numeros[5]) # False
print(tupla_numeros[-2]) # "5" Con indices negativos, accedemos desde el final (-1 es el último ele)

# #?⭐ ❌❌❌ NO podemos Modificar las tuplas
# tupla_numeros[-2] = 5 #! TypeError: 'tuple' object does not support item assignment

# #?⭐ Saber el TDD de las Tuplas
print('TDD de una tupla', type(tupla_numeros)) # <class 'tuple'>
print('TDD del ultimo elemento', type(tupla_numeros[-1])) # <class 'bool'>

# #?⭐ Longitud
print(len(tupla_numeros)) #6

# *************************** METODOS CONSTRUCTORES: list(mi_iletable), tuple(mi_iterable). 
# Existen metodos constructores de listas y tuplas, cuyo parametro es el iterable a comvertir.
# 💡Utilidad: hacer casting de un tipo de dato a otro por sus caracteristicas. Ejemplo: recibes 
# una tupla pero necesitas una lista para modificar sus ele, entonces haces el casting. 
#? Ejemplo:
print('--- METODOS CONSTRUCTORES ---')
print('Tupla', tupla_numeros) # (1, 2, 3, 4, '5', False)
lista_desde_tupla = list(tupla_numeros)
print('lista desde tupla', lista_desde_tupla) # [1, 2, 3, 4, '5', False]

print('Lista', lista_numeros) # (1, 2, 3, 4, '5', False)
tupla_desde_lista = tuple(lista_numeros)
print('tupla desde lista', tupla_desde_lista) # (1, 2, 3, 4, 5, False)

#************************** TDD ESTRUCUTRALES: STR (CADENA DE TEXTO)
nombre = 'Edily'
print(len(nombre)) # 5 → Longitud de la cadena de texto.
print(nombre[0]) # E → Acceso por índice a una cadena de texto.
#! str sin inmutables: una vez que creado, no puedes cambiar sus caracteres
# nombre[1] = 's' INMUTABES → #! TypeError: 'str' object does not support item assignment.
# tambien los podemos recorrer con ciclos, cuyas estructuras veremos a continuacion


# ***************************** OTROS TIPOS DE COLECCIONES ITERABLES
# Existen otros tipos de colecciones en Python que también son iterables (ademas de lista, tupla), como:
# diccionario, conjunto. Los veremos luego.

# TODO: A CONTINUACION LOS CICLOS: para recorrer, mapear o filtrar los elementos de los iterables. 
# ? ir a: 3_ciclos.py
# VEREMOS: FOR, WHILE, BREAK, CONTINUE, RANGE()
