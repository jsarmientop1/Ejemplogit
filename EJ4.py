import math
print("Distancia entre dos puntos")
print("Ingrese la coordenada en X para el punto A")
XA =float(input())
print("Ingrese la coordenada en Y para el punto A")
YA = float(input())

print("Ingrese la coordenada en X para el punto B")
XB = float(input())
print("Ingrese la coordenada en X para el punto B")
YB = float(input())

dist  = float(((((XA - XB)**2) +((YA - YB)**2)  )**.5))

print("La distancia entre los dos puntos es de:",round(dist,2))
