
# dict con pares de k:v, donde las key solo pueden ser TDD inmutable
# es con la key que accedes al valor
personaje = {
    "nombre":'Mujer Marav',
    "edad":28,
    'peso':50.5,
    2:'el nim es dos'
    # volar:def()
}

nombre_personaje = personaje['nombre']
el_dos = personaje[2]
print(nombre_personaje)
print(el_dos)