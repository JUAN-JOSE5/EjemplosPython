num1 = int(input("Digite el primer numero : " ))
num2 = int(input("Digite el segundo numero :"))
operacion = int(input("Digite 1 para suma, 2 para resta , 3 para multiplicacion y 4 para division " ))
if operacion==1:
    print("La suma es de : ", num1+num2)
elif operacion==2:
    print("La resta es de : ", num1-num2)
elif operacion==3:
    print("La multiplicacion es de : ", num1*num2)
elif operacion==4:
    print("La division es de : ", num1/num2 )
else:
    print("Digite un numero valido")
