
#* Sets (conjuntos) 
# Colecciones desordenadas de elementos únicos.
# Sirven para agrupar elementos sin que se repitan y para ver qué tienen en común (o de diferente) con otros grupos.
#* Características principales
# √ Sin duplicados: son eliminados
# √ Desordenados: No tienen un índice (no puedes hacer mi_set[0]).
# √ Mutables: Puedes añadir o quitar elementos, pero los elementos dentro deben ser inmutables (como números, strings o tuplas).

#* Operaciones de Conjuntos (El "Core")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print('A = ', A)
print('B = ', B)

#* Union (| o .union())
# Junta todos los elementos de ambos, eliminando duplicados.
union_op = A | B
union_method = A.union(B)
print(union_op)         # {1, 2, 3, 4, 5, 6}
print(union_method)     # {1, 2, 3, 4, 5, 6}

# * Intersection (& o .intersection())
inter_op = A & B
inter_method = A.intersection(B)
print(inter_op)         # {3, 4}
print(inter_method)     # {3, 4}

#* Symmetric Difference (^ o .symmetric_difference())
sym_op = A ^ B
sym_method = A.symmetric_difference(B)
print(sym_op)         # {1, 2, 5, 6}
print(sym_method)     # {1, 2, 5, 6}

#* Difference (- o .difference())
sym_op = A - B
sym_method = A.difference(B)
print(sym_op)         # {1, 2}
print(sym_method)     # {1, 2}


#* Agregar un elemento al set
A.add(8)
print(A) #{1, 2, 3, 4, 8}


#* 💡UTILIDAD: Filtrar!
frutas = ['manzana', 'peras', 'bann']
citricos = ['lim', 'naranja', 'manzana']

todos = set(frutas) | set(citricos)
print(todos) #{'naranja', 'manzana', 'lim', 'peras', 'bann'}


comunes = set(frutas) & set(citricos)
print(comunes) # {'manzana'}


#* ¿Qué frutas tenemos en total? (Unión)

#* ¿Qué fruta es común en ambos? (Intersección)



# # TODO: COMPREHENSION
#? ir a 9_comprehension.py
