edad = int(input("Digite su edad : "))
genero = input("Digite sexo, H para hombre ,M para mujer : ")

if edad>=18 and genero in 'Hh':
    print ("Señor, usted es mayor")
elif edad<18 and genero in 'Hh':
    print("Niño usted es menor de edad")
if edad>=18 and genero in 'Mm':
    print ("Señora, Usted es mayor")
elif edad<18 and genero in 'Mm':
    print("Niña usted es menor de edad")
if edad<=0:
    print("Usted no a nacido")


