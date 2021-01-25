

print("            Calculadora")

x=int(input("Ingresa tu 1er entero para operar :  "))
y=int(input("Ingresa tu 2do entero para operar :  "))

print("Digita 1 si quieres sumar : " )
print("Digita 2 si quieres restar : " )     
print("Digita 3 si quieres multiplicar : " )
print("Digita 4 si quieres dividir : " )


o=int(input("Digita la operación que vas a realizar: " ))




if o == 1:  
    r = x+y
    print("el resultado es: " + str(r))
    
elif o==2:
    r = x-y
    print("el resultado es: " + str(r))
    
elif o==3:
    r = x*y
    print("el resultado es: " + str(r))  
    
elif o==4:
    r = x/y
    print("el resultado es: " + str(r))
    
else:
    print("su operación es incorrecta")
    print("\n Hecho por dennisq")

    

