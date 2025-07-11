#Import librarie
import math

#Request the values
ax = float(input("Ingresa la primer coordenada: "))
ay = float(input("Ingresa la segunda coordenada: "))
bx = float(input("Ingresa la tercera coordenada: "))
by = float(input("Ingresa la cuarta coordenada: "))

#Operation
distance = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
print("distance: ", distance)
