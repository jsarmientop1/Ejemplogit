import math

print("Copias de seguridad:")
print("Ingrese el tamano del disco duro en gigabytes:")
GB = float(input())
MG = (1024 * GB)
MD = float(MG/1.44)

print("El total de microdiscos que se requiere es:",round(MD,2))
