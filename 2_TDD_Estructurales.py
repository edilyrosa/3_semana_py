# listas , tuplas, dict, conjuntos

# listas → [ele, ele, ele, ...] son mutables y ordenadas.


#&==============================LISTAS
#* creacion
lista_numeros = [1, 2, 3, 4, '5', False]
print(lista_numeros)

# acceso con la posi del ele dentro de la lista, comienza desde 0

print(lista_numeros[0]) #1
print(lista_numeros[4]) # '5'
print(lista_numeros[-1]) # False
print(lista_numeros[-2]) # '5'

print('el tipo es: ', type(lista_numeros)) #el tipo es:  <class 'list'>
print('el tipo es: ', type(lista_numeros[-1])) #el tipo es:  <class 'bool'>
print('el tipo es: ', type(lista_numeros[-2])) #el tipo es:  <class 'str'>

lista_numeros[-2] = 5
print('el tipo es: ', type(lista_numeros[-2])) # el tipo es:  <class 'int'>
print(lista_numeros)

print(len(lista_numeros)) # 6

#lista_numeros[6] = True #!ndexError: list assignment index out of range

lista_numeros.append('ultimo') #[1, 2, 3, 4, 5, False, 'ultimo']
print(lista_numeros)

ele_eliminado = lista_numeros.pop()
# lista_numeros.pop(0) → pasale por parametro la pos del elemento que queres eliminar, 
# sino le pasas post  o sea nada de p[arametros, eliminada el ultimo.
print(f'el eliminado es "{ele_eliminado}"', lista_numeros)


lista_numeros.append(5)
print(lista_numeros)
lista_numeros.remove(5)
# lista.remove(ele, start, end)

lista_numeros.sort() #lso elementos dentro del iterable deben tener el mismo TDD par que peudan ser ordenados
print(lista_numeros)
lista_numeros.sort(reverse=True) 
print(lista_numeros)

#&=========================TUPLAS
tupla_numerica = (1, 2, 3, 4, False, 'soy tupla')
print(tupla_numerica)

tupla = 1, 'Sam', 2.2
print(tupla)

print(type(tupla)) #<class 'tuple'>
ultimo = tupla_numerica[-1]
print(ultimo) #False

# 💡 las tupla son inmutables
#tupla_numerica[-1] = True #!TypeError: 'tuple' object does not support item assignment

print(len(tupla_numerica)) #5
 
lista_de_tupla = list(tupla_numerica)
print(lista_de_tupla)
print(tupla_numerica)

lista_de_tupla.append('soy el ultimo')
print(lista_de_tupla)

tupla_de_lista = tuple(lista_de_tupla)
print(tupla_de_lista)

#&==========================STR
nombre = 'Edily'
primera_letra = nombre[0]
nombre[1] = 's' #!TypeError: 'str' object does not support item assignment
print(primera_letra)