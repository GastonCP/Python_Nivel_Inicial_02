# 2- Ingresar 3 números y mostrarlos en forma ordenada de menor a
# mayor.

a = (int)(input("Ingrese el primer  numero -> "))
b = (int)(input("Ingrese el segundo numero -> "))
c = (int)(input("Ingrese el tercer  numero -> "))

if (a < b):
    aux = a
    a   = b
    b   = aux 

if (b < c):
    aux = b
    b   = c
    c   = aux 

if (a < b):
    aux = a
    a   = b
    b   = aux

print(a, b, c) 