
#* Comprensiones (Comprehensions)
# Esa forma rápida y elegante de crear colecciones, dependiendo de los símbolos que utilices.

#* Sintaxis     Nombre en Español              Nombre en Inglés               Resultado
# [...]         Comprensión de lista            List Comprehension                 list
# {...}         Comprensión de conjunto         Set Comprehension                   set
# {k: v...}     Comprensión de diccionario      Dict Comprehension                  dict
# (...)         Expresión generadora            Generator Expression              generator


#! mi_list = n for n in range(4)
# El error ocurre porque la comprensión no puede existir "en el aire". 
# Python necesita los delimitadores ([], {}, o ()) para saber qué tipo de estructura estás intentando construir. 
# Sin ellos, el intérprete lee "n" como una variable suelta y luego no sabe qué hacer con el for que sigue.

for n in range(4): # 0, 1, 2, 3
    print(n)


# n for n in range(4) #!Error 

(n for n in range(4)) #<generator object <genexpr> at 0x0000013EE4060510> 



#* 1. List Comprehension (Comprensión de Listas)
lista_const = list(n for n in range(4))
lista_const = list(n for n in range(4))
lista_comprehesion = [n for n in range(4)]
print(lista_const)        #[0, 1, 2, 3]
print(lista_comprehesion) #[0, 1, 2, 3]


tupla_const = tuple(n for n in range(4))
que_es = (n for n in range(4)) #tupla
print(tupla_const)        #(0, 1, 2, 3)
print(que_es)             # <generator object <genexpr> at 0x000001B8919420A0>






#* 2. Set Comprehension (Comprensión de Conjuntos)

set_const = set(n for n in range(4))
set_compreh = {n for n in range(4)}
print(set_const)   #{0, 1, 2, 3}
print(set_compreh) #{0, 1, 2, 3}

#* 3. Dict Comprehension (Comprensión de Diccionarios)
mi_dict = {
    'a': 10,
    'b': 5,
    'c': 20,
    'd': 3,
}

mi_dict_2 = { k: v  for k, v in mi_dict.items() }
print(mi_dict_2) #{'a': 10, 'b': 5, 'c': 20, 'd': 3}

mi_dict_filtrado = { k: v  for k, v in mi_dict.items() if v > 5 }
print(mi_dict_filtrado) #{'a': 10, 'c': 20}



#* 💡⭐ lo interesante seria filtrarlo



#* 4. Generator Expression (Expresión Generadora)





#* Agregar un if convierte a las comprensiones en una herramienta de filtrado superpotente.

#* 1. Filtrado en List Comprehension


#* 2. Filtrado en Dict Comprehension



#* 3. El "Else" (Transformación + Filtrado)



# # TODO: FUNCIONES
#? ir a 10_funciones.py













# # mi_list = ( [k, v] for k, v in personaje.items() ) # 🧠 Avanzado: lista de listas (o de tuplas) con for contraido.
# # mi_list = [ k, v for k, v in personaje.items() ] # 🧠 Avanzado: lista de listas (o de tuplas) con for contraido.

# #* La función list() solo acepta un argumento (iterable), en este caso "n" dado el for.
# mi_list = [n for n in range(4) ]   # [0, 1, 2, 3]
# mi_obj = {n for n in range(4) }   # {0, 1, 2, 3}      
# #mi_list = n for n in range(4)     #! SyntaxError: invalid syntax, si es un for sobra la "n", si es una structura requiere el clouser

# #* Con [k, v] o (k, v) crea un Objeto Genereador perezoso (lazy evaluation), sus ele NO ocupan memoria hasta que list() o tuple() los pide.
# mi_list = ( [k, v] for k, v in mi_dict.items() )  # <generator object <genexpr> at 0x000001D6450520A0>
# mi_list = ( (k, v) for k, v in mi_dict.items() )  # <generator object <genexpr> at 0x000001D6450520A0>

# #* List Comprehension: 
# mi_list = [ (k, v) for k, v in mi_dict.items() ] # lista →  [('nombre', 'Mujer Maravilla'), ('edad', 30)
# #mi_list =  (k, v) for k, v in personaje.items() #! SyntaxError: invalid syntax

# print('aca')
# print(mi_list)
# # print(personaje)

# #* El constructor list() o tuple() recibe el generador como unico parametro, y hace el casting a su tipo.
# mi_list = list( (k, v) for k, v in mi_dict.items() )  # lista → [('nombre', 'Mujer Maravilla'), ... ]
# mi_list = tuple( (k, v) for k, v in mi_dict.items() ) # tupla → (('nombre', 'Mujer Maravilla'), ('edad', 30), ...
# #! mi_list = list( k, v for k, v in personaje.items() )  #! SyntaxError: 
# # √ Múltiples argumentos: Al no tener paréntesis, como se dijo La función list() solo acepta 1 arg.
# # √ Ambigüedad: El intérprete no sabe que k, v deben ir juntos como una sola unidad dentro de la lista.




