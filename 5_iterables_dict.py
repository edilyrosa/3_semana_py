
#************************** LOS TIPO DE DATO DICT (diccionarios).
# Son colecciones de pares key:value, que representan una entidad con sus propiedades y acciones
# La key puede ser TDD inmutables: str, int, bool, tuple
# los datos por lo generan se comparten en un json [{}, {}, {}]
personaje = {
    "nombre": 'Mujer Maravilla',
    "edad":28,
    'peso': 56.66,
    "poder":['volar', 'fuerza sobrenatural'],
    'hobbies':('salvar el mundo', 'criar ganado'),
    'mujer':False,
    'mujer':True, #!las key repetidas sobreenscriben el valor
    2:'dos',
    False:'falso',
    ('nota', 'materia'):['20', 'matematicas'],
    
    # Imagina un mapa de un juego. Una ubicación se define por (x, y). 
    # No puedes tener dos cosas distintas en la misma coordenada exacta.
    (0, 0): "Inicio",
    (1, 5): "Cofre de Oro",
    (10, 2): "Enemigo Final"
}

#? ⭐ Acceso a sus valores, mediante sus claves o keys
print(personaje['nombre'])  # Mujer Maravilla
print(personaje['edad'])    # 28
print(personaje[False])     # falso
print(personaje[2])         # dos

print(personaje[('nota', 'materia')])     # ['20', 'matematicas']
print(personaje[('nota', 'materia')][1])  # matematicas

posicion = (1, 5)           # Si usuario ingresa esta posicion
posicion = (0, 0)
posicion = (10, 2)
print(f"En la posición {posicion} hay: {personaje[posicion]}")

print(type(personaje))      # <class 'dict'>
print(personaje)            # {'nombre': 'Mujer Maravilla', 'edad': 33, 'pe...


#? ⭐ Si ya sabes accederlo, puedes Recorrer un dict con for
for key in personaje:
    print(f'{key}-{personaje[key]}') 

#? ⭐ Metodos mas importantes
print('⭐ Metodos mas importantes ⭐')
print('keys', personaje.keys())     #dict_keys(['nombre'.. lo interesante es recorrelo.

for k in personaje.keys():
    print(k)


for v in personaje.values():
    print(v)
    
for k,v in personaje.items():
    print(f'{k} -- {v}')
    
mi_list = ( [k, v] for k, v in personaje.items() ) # 🧠 Avanzado: lista de listas (o de tuplas) con for contraido.
mi_list = list( (k,v)  for k, v in personaje.items() )
print(mi_list)


#? ⭐ Se accede a los values a traves de la key y get()
# print(personaje['altura']) #! KeyError: 'altura'  (si la key no existe, lanza error)
print(personaje.get('altura'))      # Si la key no existe, NO lanza error.
print(personaje.get('caminar'))     # None
print(personaje.get('camimar', 'No existe la key "caminar", lo siento')) # No existe la key "caminar", lo siento

#? ⭐ Se obtiene la cantidad de key/value con len()
print(len(personaje))      # 9

#? ⭐ Se verifica si una key existe en el dict, con el operador "in"
print('edad' in personaje) # True

# #? ⭐ Se recorre tambien con get(), con for
for key in personaje:
    print(f'{key}-{personaje.get(key)}') 

    
#? ⭐ modificar el valor de una key
personaje['nombre'] = 'Edily Mora'
print(personaje['nombre'])

#? ⭐ agregar una nueva key al dict
personaje['nacionalidad'] = 'Espanola' # Se anade al final
print(personaje['nacionalidad'])

#? ⭐ eliminar key/value y vaciarlo
print(personaje)
personaje.pop('peso') # Elimina el de la key argumento
print(personaje)

personaje.popitem()   # Elimina el ultimo
print(personaje)

personaje.clear()     # Elimina todas las key/value
print(personaje)      # {}

#? ⭐ Crear dict con la funcion dict()
personaje_dos = dict(nombre="Mujer Anara", edad=22, mujer=True)
print(personaje_dos)

#* Diccionario original
dict_original = {
    'a': 10,
    'b': 5,
    'c': 20,
    'd': 3
}

#? ⭐ Dict compacto
# ACTIVIDAD: Crear nuevo diccionario con elementos cuyo valor sea mayor a 5

# Necesitas paréntesis (k, v) porque el constructor pide "una lista de tuplas".
dict_filtrado = dict((k, v) for k, v in dict_original.items() if v > 5) 

#✅ Mismo resultado con comprensión de diccionarios (dict comprehension), mas usado
dict_filtrado_2 = {k:v for k, v in dict_original.items() if v > 5}

print(dict_filtrado)  # Salida: {'a': 10, 'c': 20}
print(dict_filtrado_2)  # Salida: {'a': 10, 'c': 20}


# # TODO: PROXIMO EJERCICIO CONSUMO DE APIS
#? ir a 6_ejercicio_dict.py