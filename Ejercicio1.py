sueldo  =  float ( input ( 'Ingresa el valor de sueldo: ' ))
if sueldo<1000:
    aumento=sueldo*0.15
else:
    aumento=0
nuevo_sueldo=sueldo+aumento
print ('Aumento: ' + repr (aumento))
print ('Nuevo sueldo: ' + repr (nuevo_sueldo))