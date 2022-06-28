print ("Ingresa el numero de respuestas correctas")
RC=int (input("RC: "))

print ("Ingresa el numero de respuesras incorrectas")
RI=int (input("RI: "))

print ("Ingresa el numero de respuestas en blanco")
RB=int (input("RB: "))

PRC = int (RC*3)
print ("Puntaje de respuestas correctas: ")
print (PRC)

PRI = int (RI*(-1))
print ("Puntaje de respuestas incorrectas: ")
print (PRI)

PRB = int (RB*0)
print ("Puntaje de respuestas en blanco: ")
print (PRB)

PF = int (PRC+PRI+PRB)
print ("El Puntaje Final es: ")
print (PF)