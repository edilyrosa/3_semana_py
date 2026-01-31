
#?⭐ ya sabemos recorrer, filtrar y mapear los iterables con los ciclos.

#? ⭐ Operador "in" 
#& 💡Recorrer iterables con Operador "in" 
print('💡Recorriendo una lista con Operador "in" ')
mi_lista = [10, 20, 30, 40] 
for elemento in mi_lista:
    print(elemento)
    
#& 💡Tmabien podemos saber si un elemento existe en el iterable con Operador "in"
mi_tupla =  (1,2,3,4,5) 
# 5 in mi_tupla #* True
respuesta = 'Si' if 5 in mi_tupla else 'No'
print(f'💡Existe el elemento "5" dentro de "mi_tupla": {respuesta}')


#? ⭐ Slicing de los iterables: para extraer (retornando) todo o parte de sus elementos.
# mi_lista[inicio: fin: paso] 
# 1. inicio: índice desde donde comienza el corte.
# Incluye el elemento en esta posición, Si se omite es indice 0.
# Puede ser negativo, contando desde el final (-1 es el último elemento).
# 2. fin: índice donde termina el corte. 
# Excluye el elemento en esta posición, Si se omite va hasta el final.
# También puede ser negativo para contar desde el final (-1 es el último elemento).
# 3. paso: Indica de cuánto en cuánto se avanza para tomar elementos.
# Por defecto es 1 → Toman elementos consecutivos de inicio a fin, -1 los toma a la inversa.
# No puede ser 0 (causa Error). 

lista_slicing = [1,2,3,4,5]
print('💡Haciendo Slicing de iterables')

print(lista_slicing[::])     # [1,2,3,4,5]      → Los toma todos de incio a fin, sin paso ni reversa
print(lista_slicing[2::])    # [3,4,5]          → Los toma desde la pos 2 (incluyente) hasta el fin, sin paso ni reversa
print(lista_slicing[::-1])   # [5, 4, 3, 2, 1]  → Los toma todos con reversa de 1 en 1.
print(lista_slicing[::-2])   # [5, 3, 1]        → Los toma con reversa de 2 en 2.
print(lista_slicing[:2:-1])  # [5, 4]           → Los toma con reversa hasta la posicion 2 (excluyente, por eso al ele 4)

#?⭐⭐⭐ Lista compacta: 
# Forma resumida de crear una lista, es muy utilizadas profesionalmente, acostumbrate a esta sintaxis
# EJEMPLO: Vamos a crear una lista compacta con elementos que NO son múltiplos de 2
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_filtrada = [x for x in lista_original if not x % 2 == 0] # x es la variable que representa cada ele

tupla_filtrada = (x for x in lista_original if not x % 2 == 0)    # ❌ Esto crea un generador
tupla_filtrada = tuple(x for x in lista_original if x % 2 != 0)   # ✅ Generator a tupla
tupla_filtrada = tuple([x for x in lista_original if x % 2 != 0]) # ✅ List comprehension a tupla

print('💡Impresion de listas compactas')
print(lista_filtrada)  # Salida: [1, 3, 5, 7, 9]
print(tupla_filtrada)  # Salida: (1, 3, 5, 7, 9)

#? 🤸🏻 EJERCICO: realiza una lista compacta con 24 elementos: "ciudad-1", "ciudad-2", ... "ciudad-24"
num_ciudades = 25
ciudades = [f'Ciudad-{num}' for num in range(1, num_ciudades)]
print('💡Impresion de lista compacta de ciudades')
print(ciudades)
    
    
#? ⭐ Desempaquetamiento de los iterables
# para extraer facilmente los elementos de iterables en variables, 
mi_tupla_empaquetada = False, 1,'dos', ['profesor', 'alumno'], (10, 20)
uno, dos, tres, cuatro, cinco = mi_tupla_empaquetada
print('💡Impresion elementos unpacking de tupla')
print(uno)      # False
print(dos)      # 1
print(cuatro)   # ['profesor', 'alumno']

print('💡Impresion elementos unpacking de tupla con operador "*"')
#? 💡unpacking (operadores con el operador "*")
a, b, *rest = [1, 2, 3, 4]
# a=1, b=2, rest=[3,4]
print(a, b, rest)
lst = [*range(3), 10]        # [0, 1, 2, 10]
tup = (*range(3), 10)        # (0, 1, 2, 10)
print(lst, tup)



#& *************************************Tipo de dato SET
# Es una colección *desordenada* de elementos **únicos**.
# Es mutable (puedes añadir/quitar elementos) pero los elementos deben ser 
# hashables (no cambia mientras exista, son inmutable → int, str, tuple).
# (por ejemplo: números, strings, tuplas; NO listas ni diccionarios).
# Se crean entre corchetes {} o con el constructor.

#? ⭐ Creación:
s = {1, 2, 3}               # literal
s = set([1, 2, 3, 3])       # desde iterable (los duplicados se eliminan)
s = set(range(5))           # desde cualquier iterable

#? ⭐ Propiedades y operaciones comunes:
#   - Añadir: s.add(x)
#   - Quitar: s.remove(x)       # lanza KeyError si x no existe
#             s.discard(x)      # no lanza si x no existe
#   - Extraer arbitrario: s.pop() # como están desordenados, devuelve cualquier elemento
#   - Limpiar: s.clear()
#   - Unión: s | t     (o s.union(t))
#   - Intersección: s & t  (o s.intersection(t))
#   - Diferencia: s - t  (o s.difference(t))
#   - Diferencia simétrica: s ^ t (o s.symmetric_difference(t))
#   - Subconjunto/sobconjunto: s.issubset(t), s.issuperset(t)
#   - Disjuntos: s.isdisjoint(t)

#? Ejemplos:
s1 = {1, 2, 2, 3}
s2 = set([3, 4, 5])
print('💡Set (duplicados eliminados):', s1)

print('UNION DE SETS')
union = s1 | s2
union_metodo = s1.union(s2)
print('💡s1 union s2:', union) # {1, 2, 3, 4, 5}
print('💡s1 union s2 con metodo:', union)

print('INTERSECION DE SETS')
intersection = s1 & s2
intersecion_metodo = s1.intersection(s2)
print('💡s1 interseccion s2:', intersection) # {3}
print('💡s1 interseccion s2 con metodo:', intersecion_metodo)

print('DIFERENCIA DE SETS')
diferencia = s1 - s2
difencia_metodo = s1.difference(s2)
print('💡s1 diferencia s2:', diferencia) # {1, 2}
print('💡s1 diferencia s2:', difencia_metodo)
