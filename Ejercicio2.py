año = float (input ('Ingresa el año: '))
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("Es bisiesto")
print("No es bisiesto")