class Empleado:
    def  __init__(self):
        self.codigo=""
        self.nombres=""
        self.apellidos=""
        self.salario_base=""

    def calcular_retencion(self):
        retencion= (self.salario_base)*0.10
        return retencion

    def mostrar_nombrecompleto(self):
        nombrecomp= self.nombres + " " + self.apellidos
        return nombrecomp

    def calcular_salario_neto(self):
        if(self.salario_base<=828.116):
            salarioneto= self.salario_base+100000
        else:
            salarioneto=self.salario_base
        return salarioneto   

emp = Empleado()
emp.codigo =input("Ingrese el codigo : ")
emp.nombres=input("Ingrese los nombres : ")
emp.apellidos=input("Ingrese los apellidos : ")
emp.salario_base=float(input("Digite el salario base : "))
print("La retencion es de : " ,emp.calcular_retencion())
print("El nombre completo es : ",emp.mostrar_nombrecompleto())
print("El salario es :" ,emp.calcular_salario_neto())
