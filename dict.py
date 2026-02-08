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

#accedr a los valores mediante las key
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



# metodos mas importantes en los dict
print(personaje.keys()) #dict_keys(['nombre', 'edad', 'peso', 'poderes', 'hobbies', 'mujer', 2, False, ('notas', 'materia'), (0, 0), (1, 5), (10, 2), 'vidas', 'precio'])

for k in personaje.keys():
    print(k)
    
    
for v in personaje.values():
    print(v)
    
    
for k,v in personaje.items():
    print(f"{k} - {v}")
    
mi_list =  list( (k,v)  for k,v in personaje.items() )
print(mi_list)
print(personaje)