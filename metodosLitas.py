# lista = [1,3,4,5]
# #* Metodo mi_lista.insert(index, ele)
# # lista.insert(1, 'Carlos')
# lista.insert(1, 2)
# print(lista) # [1, 2, 3, 4, 5]

# #* Metodo mi_lista.extend(iterables)
# lista_dos = [6, 7, 8]
# lista.extend(lista_dos)
# print(lista) #[1, 2, 3, 4, 5, 6, 7, 8]


# #* Metodo sort() Vs. sorted() 

# print(lista.sort(reverse=True)) # None
# print(lista) #[8, 7, 6, 5, 4, 3, 2, 1]

# print(sorted(lista)) # [1, 2, 3, 4, 5, 6, 7, 8]
# lista_ordenada  = sorted(lista)
# print('afectada por siempre por sort()', lista) #[8, 7, 6, 5, 4, 3, 2, 1]
# print('ordenada guadada en var', lista_ordenada)  # [1, 2, 3, 4, 5, 6, 7, 8]




# #!lista_desOrd = ['a', 'v', 'c', True, [1,3]]
# # lista_desOrd = [1, 4, 2, 3]
# # print(lista_desOrd) #[1, 4, 2, 3]
# # lista_desOrd.sort()
# # print(lista_desOrd) #[1, 2, 3, 4]

# lista_desOrd = [1, 4, 2, 3]
# print(lista_desOrd)         #[1, 4, 2, 3]
# mi_lista_ord_sorted = sorted(lista_desOrd)
# print(lista_desOrd)         #[1, 4, 2, 3]
# print(mi_lista_ord_sorted)  #[1, 2, 3, 4]


# #* Metodo map(func, iterable)
def calcular_cubo(num):
    return num **3
mi_iterable = [1,2,3,4,5]

print(map(calcular_cubo, mi_iterable)) #<map object at 0x000001FF4EDB3700>
print(list(map(calcular_cubo, mi_iterable))) #[1, 8, 27, 64, 125]
print(tuple(map(calcular_cubo, mi_iterable))) #(1, 8, 27, 64, 125)

mi_iterable_lista_cub = list(map(calcular_cubo, mi_iterable))
print(mi_iterable) #[1, 2, 3, 4, 5]
print(mi_iterable_lista_cub) #[1, 8, 27, 64, 125]



# #* Metodo filter(func, iterable)

def es_par(num):
    return num % 2 == 0

lista_par = list(filter(es_par, mi_iterable_lista_cub))
print(lista_par) #[8, 64]
    
# lista_traer = pro.title.inclued(input)