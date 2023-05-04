# 3- Ingresar las medidas de los lados de un triángulo y mostrar por
# pantalla si se trata de un triángulo equilátero, escaleno o isósceles.

a = (float)(input("Ingrese la medida del primer  lado -> "))
b = (float)(input("Ingrese la medida del segundo lado -> "))
c = (float)(input("Ingrese la medida del tercer  lado -> "))

if(a == b ) and (b == c):
    print ("Es un triangulo equilatero.")
elif (a == b) or (b == c) or (c == a):
    print("Es un triangulo isoceles.")
else :
    print("Es un triangulo escaleno.")