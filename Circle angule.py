# New programm
import math

#Read values
radio = input("Ingresa el radio: ")
angulo = input("Ingresa el angulo: ")
radio = float(radio)
angulo = float(angulo)

#Convert angle from degrees to radians
angulo = angulo * math.pi /180

#Calculate point coordinates
x = radio * math.cos(angulo)
y = radio * math.sin(angulo)

#Print result
print("Coordenadas: ", x, "/", y)