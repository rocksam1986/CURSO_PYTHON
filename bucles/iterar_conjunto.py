nombres = {"oscar", "carlos" , "jorge","maicol"}
numeros = {2,4,5,8,}

#recorriendo la conjunto nombre
for alumnos in nombres:
    print (f'estos son los alumnos inscritos: {alumnos}')
    
#recorriendo la conjunto numero y multiplicando por     10
for numero in numeros:
    resultado = numero *10
    print (f' este es el resultado multiplicado por 10: {resultado}')
    
    
#iterando  dos conjuntos del mismo tamño al mismo tiewmpo

for alumnos,numero in zip(nombres,numeros):
    print(f'recorriendo conjunto 1: {alumnos}')    
    print(f'recorriendo conjunto 2: {numero}')  
 
 

#forma correcta de recorrer una conjunto con su indice 

for num in enumerate(numeros):
    indice = num[0]
    valor = num [1]
    print (f'el indice es:{indice} y el valor es: {valor}')
    
    
#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
 print("el ultimo bucle termibno")        
 
 #todo lo anterior funciona exactamente igual para tuplas