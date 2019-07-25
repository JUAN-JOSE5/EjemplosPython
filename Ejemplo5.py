peso=float(input("Ingrese el peso: "))
estatura=float(input("Ingrese la estatura: "))
imc=peso/(estatura*estatura)
if imc<18.5:
    print(imc," Bajo de peso")
elif imc>=18.5 and imc<24.9:
    print(imc,"Normal")
elif imc>=25 and imc<29.9:
    print(imc," Sobrepeso")
elif imc>=30 and imc<34.9:
    print(imc," Obesidad I")
elif imc>=35 and imc<39.9:
    print(imc," Obesidad II")
elif imc>=40 and imc<49.9:
    print(imc," Obesidad III")
else:
    print(imc," Obesidad IV")
