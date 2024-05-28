frutas = ["banana", "manzanas","ciruelas", "peras", "naranjas", "granada", "durazno"] 
cadena = 'oscar sam'
numeros = [2,5,7,8]

#evitando que se coma una ciruelas, con la sentencia continue

for fruta in frutas:
    if fruta == 'ciruelas':
        continue
    print(f'me voy acomer una: {fruta}')
    
    
#evitar que el bucle continue (el else no se ejecuta tampoco)


for fruta in frutas:
    print(f'me voy a comer una fruta {fruta}')
    if fruta == 'peras':
        break
else:
    print('terminar')   
    
    
#recorrer una cadena de texto

for letra in cadena:
    print(letra)     
    
#for en una sola linea de codigos

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)    
    
    