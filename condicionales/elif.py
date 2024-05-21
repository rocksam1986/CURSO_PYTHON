ingresos_mensuales = 81000
gastos_mensuales = 70000

#if anidados y else if (elif)

if ingresos_mensuales > 10000:
    if ingresos_mensuales - gastos_mensuales   < 0:
        print ("estas en deficit")
    elif ingresos_mensuales - gastos_mensuales  > 3000:
        print ("las cosas estan bien")    
    else:
        print ( "estas gastando ,mucho")    
    
elif ingresos_mensuales > 1000:
    print ("estas bien en colombia")    

elif ingresos_mensuales > 500:
    print ("estas bien en españa")
    
elif ingresos_mensuales > 200:
    print ("estas bien en chile")
    
else:
    print ("eres pobre")       