peso = float(input("Digite el peso de la persona : " ))
estatura = float(input("Digite la estatura de la persona :"))
mc = float(input(peso/(estatura/2)))
if mc<18.5:
    print("Esta en bajo :", mc)
elif mc>18.5 and mc<24.9:
    print("Esta normal : ", mc)
elif mc>25 and mc<29.9:
    print("Esta en sobrepeso: ", mc)
elif mc>30 and mc<34.9:
    print("Esta en obesidad 1 : ", mc )
elif mc>35 and mc<39.9:
    print("Esta en obesidad 2 :", mc)
elif mc>40 and mc<49.9:
    print("Esta en obesidad 3 : ", mc)
elif mc>50:
    print("Esta en obesidad 4 : ", mc)
