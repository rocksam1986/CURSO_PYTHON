diccionario = {
    "nombre": "oscar",
    "apellido": "sam",
    "edad": 37
}

#recorriendo diciionarios con items() para obtener la clave y el valor
for key in diccionario:
    
    print(f'la clave es: {key}')
  

    
#recorriendo diciionarios con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos [0]
    value = datos [1]
    print(f'la clave es: {key} y el valor es {value}')    