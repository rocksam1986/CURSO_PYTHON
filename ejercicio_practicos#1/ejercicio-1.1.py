#el promedio de duracion

otro_cursos_min = 2.5
otro_cursos_max = 7
otro_cursos_prom = 4
dalton_curso = 1.5

#diferencias de crudo

crudo_prom = 5
crudo_dalto =3.5


#diferecias de duracion

diferencia_con_min = 100 - dalton_curso / otro_cursos_min *100
diferencia_con_max = 100 - dalton_curso *1000 // otro_cursos_max / 10
diferencia_con_prom = 100 - dalton_curso / otro_cursos_prom * 100


#calculando el porsentaje de tiempo vacio removido

tiempo_vacio_prom = 100 - otro_cursos_prom *1000 // crudo_prom / 10
tiempo_vacio_dalto = 100 - dalton_curso *1000 // crudo_dalto / 10




# mostrando las diferencias de duracion (ejecicio a)
print("------------------------")
print("el curso de dalton dura:")
print (f'el curso de dalton dura un {diferencia_con_min} % menos que el mas rapido')
print (f'el curso de dalton dura un {diferencia_con_max} % menos que el mas lentoo')
print (f'el curso de dalton dura un {diferencia_con_prom} % menos que el promedio')
print("------------------------")


#mostrando la cantidad de espacios vacios que se remueven (b)
print("------------------------")
print("los cursos elimitan esta cantidad de tiempos vacios:")
print (f'el curso de promedio remueve un {tiempo_vacio_prom} % de tiempo vacio')
print (f'el curso de dalton remueve un {tiempo_vacio_dalto} % de tiempo vacio')
print("------------------------")

print("------------------------")
print("este es el tiempo si todos los cursos duraran 10 horas:")
#mostrando diferencias si los cursos duraran 10 horas
print (f'ver 10 horas de este curso equivale a ver  {otro_cursos_prom *100 // dalton_curso /10} horas de otros cursos')
print (f'ver 10 horas de otros curso equivale a ver  {dalton_curso *100 // otro_cursos_prom /10} horas de otros cursos')
print("------------------------")