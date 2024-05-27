#creando una lista con list()
lista = list(["hola","oscar",12,25,45,True])

#devuelve la cantidad de elementos de la lista

cantidad_elementos = len(lista)

#agrega un elemento a la lista
lista.append ("sam")

#agrega u  elemento en la lista en un indice especifico
lista.insert(3,"rock")
 
 #agrega varios elementos a la lista
lista.extend(["mi","casa"])
 
#elimina elentos de la lista por su indice
lista.pop(5) #-1 para eliminal elultimo, -2 el antepenultimo y asi sucesivamente

#ordena la lista de fotma acendente  (si usamos el parametro reverse=true lo ordena en reversa)
lista.sort()

#eliminando todos los elementos de la lista
#lista.clear

#invirte la lista si  ordenar 
lista.reverse()

print(lista)

