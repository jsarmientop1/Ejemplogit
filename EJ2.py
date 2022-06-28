print ("Ingrese el numero de partidos ganados")
PG=int (input("PG: "))

print ("Ingrese el numero de partidos empatados")
PE=int (input("PE: "))

print ("Ingrese el numero de partidos perdidos")
PP=int (input("PP: "))

PPG = int (PG*3)
print ("Puntaje de partidos ganados: ")
print (PPG)

PPE = int (PE*(1))
print ("Puntaje de partidos empatados: ")
print (PPE)

PPP = int (PP*0)
print ("Puntaje de partidos perdidos: ")
print (PPP)

PT = int (PPG+PPE+PPP)
print ("El Puntaje total es: ")
print (PT)
