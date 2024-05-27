#le pediremos al usuario que nos diga una frace o varias
frase = input ("escribe una frace y te calculo cunto tiempo tardas en decirla: ")

#creamos una lista con la palabras de la frace ( se separan cada vez qyue hay un espacio en blanco)
plabras_separadas = frase.split(" ")

#usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(plabras_separadas)

#en caso que tarde mas de un minuto le decimos que paso el limite
if cantidad_de_palabras > 120:
    print("exediste el numero de palabras")
    
#calculamos cuanto tyardaria en decir las palbras y se lo decimos
print (f"digites {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo")
print (f'dalto lo diria en {cantidad_de_palabras *100 //2 *1.3 /100} segundos')