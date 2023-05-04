# 4- Calcular el plus que un trabajador recibe en el reparto anual de
# utilidades si a este se le asigna como porcentaje de su salario mensual
# que depende de su antigüedad en la empresa de acuerdo con la
# siguiente tabla (Simulando Swith)

def esNumeroPositivo( numero : float):
    if(numero >= 0):
        return 1
    else:
        return 0

def opcion1(salarioMensual : float):
    print("Salario a pagar $", round(salarioMensual * 1.05))

def opcion2(salarioMensual : float):
    print("Salario a pagar $", round(salarioMensual * 1.07))

def opcion3(salarioMensual : float):
    print("Salario a pagar $", round(salarioMensual * 1.10))

def opcion4(salarioMensual : float):
    print("Salario a pagar $", round(salarioMensual * 1.15))

def opcion5(salarioMensual : float):
    print("Salario a pagar $", round(salarioMensual * 1.20))

switch = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5
}

print("Ingrese la opcion segun corresponda.")
print("1 -> para Menos de 1 año de antiguedad.")
print("2 -> para Menos de 2 años de antiguedad.")
print("3 -> para Menos de 5 años de antiguedad.")
print("4 -> para Menos de 10 años de antiguedad.")
print("5 -> para Mas de 10 años de antiguedad.")
print()

while(1):

    antiguedad = int(input("Ingrese la opcion segun su antiguedad -> "))
    salarioMensual = float(input("Ingrese el salario mensual            -> $"))

    if(esNumeroPositivo(antiguedad) and esNumeroPositivo(salarioMensual) and antiguedad in switch):
        switch[antiguedad](salarioMensual)
    else: 
        print("dato/s ingresado/s incorrectos.")
    print()

