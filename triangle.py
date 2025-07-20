#Reques tree values
a = float(input("Introduce one side: "))
b = float(input("Introduce second side: "))
c = float(input("Introduce third value: "))

# Check viability
if a > b + c or b > a + c or c > a+ b:
    print("The triangle is not viable")
else:
    print("Triangle is viable")