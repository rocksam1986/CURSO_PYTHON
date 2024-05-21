#creando una lista se pueden modificar 
lista = ["oscarsam","soy",True,1.75]

#creando una tupla (no se pueden modificar)
tupla = ("oscarsam","soy",True,1.75)

#esto es valido
lista[3]= "maquina"

#esto no se ejecuta
#tupla[3]="maquina"

print (lista[0])

#creando un comjunto (set) (no se accede a los datos por su indice, no almacena datos duplicado)

conjunto ={"oscarsam","soy",True,1.75}

conjunto = {"maquina3"}

#print = (conjunto[3]) -> no se puede acceder al elemento

tupla = {"maquina3"}

print(conjunto)

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
     'nombre' : "oscar",
     'canal' : "rocksam",
     'como_estas' : True,
     'altura' : 1.75,
     'dato_duplicado' : "rocksam"   
}
 
print(diccionario['altura'])
print (lista[3])