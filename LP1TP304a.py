# 4- Calcular el plus que un trabajador recibe en el reparto anual de
# utilidades si a este se le asigna como porcentaje de su salario mensual
# que depende de su antigüedad en la empresa de acuerdo con la
# siguiente tabla

def esNumeroPositivo( numero : float):
    if(numero >= 0):
        return 1
    else:
        return 0

def calcularSalario(aniosDeAntiguedad : int, salarioMensual : float):
    if(aniosDeAntiguedad == 0):
        print("Salario a pagar $", round(salarioMensual * 1.05))
    elif(aniosDeAntiguedad == 1):
        print("Salario a pagar $", round(salarioMensual * 1.07))
    elif(aniosDeAntiguedad < 5):
        print("Salario a pagar $", round(salarioMensual * 1.10))
    elif(aniosDeAntiguedad < 10):
        print("Salario a pagar $", round(salarioMensual * 1.15))
    else:
        print("Salario a pagar $", round(salarioMensual * 1.20))

while(1):

    aniosDeAntiguedad = int(input("Ingrese los años de antiguedad -> "))
    salarioMensual = float(input("Ingrese el salario mensual      -> $"))

    if(esNumeroPositivo(aniosDeAntiguedad) and esNumeroPositivo(salarioMensual)):
        calcularSalario(aniosDeAntiguedad, salarioMensual)
    else: 
        print("dato/s ingresado/s incorrectamente.")
    print()

