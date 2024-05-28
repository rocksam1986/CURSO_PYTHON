#crando dicionarios con dict()
    
diccionario = dict(nombre= "oscar", apellidos="sam")


#las listas no pieden se claves y usamos frozenset para meter conjuntos

diccionario = {frozenset(["oscar","dos" ]): "ohoh"}

#creando diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellidos"])

#creando diccionario con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellidos"], "no se")


print(diccionario)