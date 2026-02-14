
#*definicion 
personaje = {
    'nombre': 'Mujer Maravilla',
    'edad':28,
    'peso':56.66,
    'poderes':['volar', 'fuerza sobrenatural'],
    'hobbies':('ayudar', 'correr'),
    'mujer':False, 
    'mujer':True, #* Las key reperidas sobreescrben la anterior
    2:'dos',
    False:'falso',
    ('notas', 'materia'):['20', 'math'],
    
    #* utilidad de las tuplas: 
    (0, 0): 'inicio',
    (1, 5): 'Cobre de oro',
    (10, 2): 'Enemigo',
    'vidas':5,
    # menos_vidad: def name(args):
    # pass
    
    "precio": 100.01 
}

#* accedr a los valores mediante las key
print(personaje['nombre'])
print(personaje['edad'])
print(personaje['poderes'])    #['volar', 'fuerza sobrenatural']
print(personaje['poderes'][0]) #volar
print(personaje[('notas', 'materia')]) #['20', 'math']
print(personaje[('notas', 'materia')][1]) # math
print(personaje[False])
print(personaje[2])
#! print(personaje['2'])#KeyError: '2'

# posicion = (0, 0) #En la posc(0, 0) hay inicio
posicion = (10, 2) #En la posc(10, 2) hay Enemigo
# posicion = (1, 5)
print(f'En la posc{posicion} hay {personaje[posicion]}')

for clave in personaje:
    print(f'{clave}')
    print(f'{clave} - {personaje[clave]}')
    
# lista = [1,3,4]
# for elemento in lista:
#     print(elemento)

#* actualizarlo valores
print(personaje['edad']) #28
personaje['edad'] = 30 
print(personaje['edad']) 

print(personaje['poderes']) #['volar', 'fuerza sobrenatural']
personaje['poderes'][0] = 'cantar'
print(personaje['poderes']) # ['cantar', 'fuerza sobrenatural']

# def rebajaPre(pre):
#     return pre*0.2-pre

# totalizar =  rebajaPre(personaje['precio'])

print(type(personaje)) #<class 'dict'>
print(type(personaje['edad'])) #<class 'int'>



#* ⭐⭐⭐⭐⭐metodos mas importantes en los dict
print(personaje.keys()) #dict_keys(['nombre', 'edad', 'peso', 'poderes', 'hobbies', 'mujer', 2, False, ('notas', 'materia'), (0, 0), (1, 5), (10, 2), 'vidas', 'precio'])

for k in personaje.keys():
    print(k)
    
    
for v in personaje.values():
    print(v)
    
    
for k,v in personaje.items():
    print(f"{k} - {v}")


    
mi_list =  list( (k,v)  for k,v in personaje.items() ) #TODO: esto es una list comprehension.
print(mi_list)
print(personaje)

print('EL GENERADOR')
generador  = ((k,v)  for k,v in personaje.items())
lista_dict = list((k,v)  for k,v in personaje.items())

#* Comprenhension: Forma rápida y elegante de crear colecciones en memoria. Lo veremos luego.

#* 💡LIST Comprehension de las k:v del dict


#? TAREA: como guardar en memoria: listas de los valores, listas de las keys, 💽 LOS LOOPS DE ARRIBA NO TIENEN PERSISTENCIA
lista_valores_dict = [v for v in personaje.values()] #['Mujer Maravilla', 30, 56.66, ['cantar', 'fuerza sobrenatural'], ('ayudar', 'correr'), True, 'dos', 'falso', ['20', 'math'], 'inicio', 'Cobre de oro', 'Enemigo', 5, 100.01]
lista_valores_dict = list(v for v in personaje.values()) #['Mujer Maravilla', 30, 56.66, ['cantar', 'fuerza sobrenatural'], ('ayudar', 'correr'), True, 'dos', 'falso', ['20', 'math'], 'inicio', 'Cobre de oro', 'Enemigo', 5, 100.01]
print('lista de valores')
print(lista_valores_dict)

lista_keys_dict = list([k for k in personaje.keys()])
print('lista de keys')
print(lista_keys_dict) #['nombre', 'edad', 'peso', 'poderes', 'hobbies', 'mujer', 2, False, ('notas', 'materia'), (0, 0), (1, 5), (10, 2), 'vidas', 'precio']

#* para que me serviria tenerlas en listas?
#? 💡Metodo zip(lista A, lista B)
# Va uniendo el índice 0 de la lista A con el índice 0 de la lista B, y así sucesivamente.

#? ⭐ Dict Comprehension: tienes lista de claves y de valores:
keys = lista_keys_dict[:4]
print(keys) #['nombre', 'edad', 'peso', 'poderes']
valores = ['Hombre Anara', 20, 70.70, ['tejer', 'muy rapido']]
#* 💡 Usamos zip para emparejarlas y la comprensión para construir el dict
dict_homb_ana = {k: v for k,v in zip(keys, valores)}
print('Dict del hombre anara')
print(dict_homb_ana)

#* 💡💡La forma más rápida (Constructor dict)
dict_homb_ana_constr = dict(zip(keys, valores))
print(dict_homb_ana_constr) #{'nombre': 'Hombre Anara', 'edad': 20, 'peso': 70.7, 'poderes': ['tejer', 'muy rapido']}

#? ⭐ Crear un Dict con su constructor dict()

personaje_dos = dict(nombre='sumerman', edad=22, genero=False)
print(personaje_dos ) #

#? ⭐ Se accede a los values a traves de la key y get(), get() retorna → None | valor
print(personaje['nombre']) # Mujer Maravilla
#print(personaje['altura']) #!KeyError: 'altura'
print(personaje.get('altura')) # None 
print(personaje.get('altura', 'Lo siento pero esa key no existe')) # Lo siento pero esa key no existe
print(personaje.get('nombre')) # Mujer Maravilla


#? ⭐ Se obtiene la cantidad de key/value con len()
print(len(personaje)) #14

#? ⭐ Se verifica si una key existe en el dict, con el operador "in"

print('edad' in personaje) #True


#? ⭐ Se recorre tambien con get(), con for
for key in personaje:
    print(f'{key}--{personaje.get(key)}')
    print(f'{key}--{personaje[key]}')
    
for key, valor in personaje.items():
    print(f'{key}--{valor}')
   
copia_personaje = {k:v for k,v in personaje.items()}

    # print(f"{k} - {v}")
    
#? ⭐ modificar el valor de una key

personaje['nombre'] = 'Rosa Poderosa'
print(personaje.get('nombre'))  # Rosa Poderosa

#? ⭐ agregar una nueva key al dict
personaje['nacionalidad'] = 'Espanola'
print(personaje.get('nacionalidad'))  # Espanola

print(len(personaje)) #15


#? ⭐❌ eliminar key/value y vaciarlo
print(personaje)
personaje.pop('peso') # elimina la k:v que le pases por paremtro
personaje.popitem() # elimina la ultima k:v 
print(personaje)

personaje.clear() # elimina la ultima k:v 
print(personaje) # {} 


# # TODO: LOS CONJUNTOS O SETS
#? ir a 8_conjuntos.py