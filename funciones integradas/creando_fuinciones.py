#creando una funcion simple

#def saludar():
    #print("hola soy oscar, el alumno")
    
#ejecutando la funcion simple    
#saludar()  

#creando una fincion que tenga parametros

def saludar(nombre,sexo):
    sexo = sexo.lower() 
    if (sexo=="mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
    
    
    print(f"hola {nombre}, mi {adjetivo} ¿como estas?")
    
saludar("oscar", "hombre")    
                 
#crear un afuncion que nos retorne multiples  valores
def creando_contraseña(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5    
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desempaquetando la funcion
password,primer_numero = creando_contraseña(254)


#mostrando los resultados obtenidos y los datos utilizados para obtnerlo

print(f"tu contraseña nueva es:{password}")
print(f"el numero untilizada para crearla fue::{primer_numero}")
#password = creando_contraseña(10)
#frase = f"tu contaseña es:{password}"
#print(frase)
                 