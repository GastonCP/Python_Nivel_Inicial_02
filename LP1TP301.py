# 1- Ingresar un número que represente el día de la semana, mostrar por
# pantalla el nombre del día correspondiente, ej: 1- Domingo, 2- Lunes, 3-
# Martes, etc.

def opcion1():
    print("Lunes.")

def opcion2():
    print("Martes.")

def opcion3():
    print("Miercoles.")

def opcion4():
    print("Jueves.")

def opcion5():
    print("Viernes.")

def opcion6():
    print("Sabado.")

def opcion7():
    print("Domingo.")

switch = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5,
    6: opcion6,
    7: opcion7
}

opcion = int(input("ingrese el numero del dia de la semana correspondiente : "))
if(opcion in switch):
    switch[opcion]()
else:
    print("opcion ingresada incorrecta.")


