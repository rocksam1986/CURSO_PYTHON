#los metodos son datos + . + el metodo 
cadena1 = "Hola soy oscar"
cadena2 = "Hola soy Mimi"

#este metoda nos vuelve  en mayuscula (.upper)
relustado = cadena1.upper()
relustado2 = "estoy embolatado".upper()

#este metoda nos vuelve  en minuscula (.lower)

relustado3 = cadena2.lower()
relustado4 = "Estoy Embolatado".lower()

#este metodo nos vuelve la primera leyra en mayuscula (.capitalize)

relustado5 = cadena2.capitalize()
relustado6 = "Estoy Embolatado".capitalize()


#este metodo busca una cadena en otra cadena  (.find) si no hay conicidencias devuelve -1

relustado7 = cadena2.find("m")

#este metodo busca una cadena en otra cadena  (.index) si no hay concidencias lanza una exepcion 

relustado8 = cadena2.index("i")


#si es numerico devuelve true, si no es jumerico devuelve false (.isnumeric)

relustado9 = cadena2.isnumeric()


#si es alfanumerico devuelve true, si no es alfamerico devuelve false (.isalpha)

relustado10 = cadena2.isalpha()


#contamos las coincidencias de una cadena dentro de otra cadena, nos devuelve la cantidad de concidencias (.count)

relustado11 = cadena1.count("a")

#contamos cuantos carracteres tiene un cadena (len+(variable))

relustado12 = len(cadena1)

#verifica que la cadena empieza con otra cadena dada, si es asi devueve true (startswith)

relustado13 = cadena1.startswith("H")

#verifica que la cadena termine con otra cadena dada, si es asi devueve true (endswith)

relustado14 = cadena1.endswith("H")

#si el valor es 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2 (replace)
relustado15 = cadena1.replace("Hola", "me voy")
 
#separa las cadenas con las cadenas que le pasemos (.split)
 
relustado16 = cadena1.split (".")
 
print (relustado16)