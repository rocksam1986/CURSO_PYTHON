diccionario = {
    "nombre" : 'oscar',
    "apellidos" : 'sam',
    "subs" : 100000
}

#nos devuelve un objeto dict_item
clave = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continua)
clave = diccionario.get("nombre")


#elimiando todo el dicionario
# diccionario.clear()

#eliminando un elemneto del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)