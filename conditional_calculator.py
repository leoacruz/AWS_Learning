# Request two values
x = float(input("Enter a value: "))
y = float(input("Enter another value: "))

# Request the operation
z = input("""Enter an option: 
              (a) Add
              (s) Substract
              (m) Multiply
              (d) Divide: 
          """)

# Operation to do
if z == "a":
    print("Result: ", x + y)
elif z == "s":
    print("Result: ", x - y)
elif z == "m":
    print("Result: ", x * y)
elif z == "d":
    if y != 0:
        print("Result: ", x / y)
    else:
        print("Error: cannot divide by zero.")
else:
    print("Not a valid option")