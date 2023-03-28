num1 = input("Insert a number: ")
variable = input("Insert a variable(+, -, *, /): ")
num2 = input("Insert a number: ")

add = float(num1) + float(num2)
subtract = float(num1) - float(num2)
multiply = float(num1) * float(num2)
divide = float(num1) / float(num2)
Floor Division = float(num1) // float(num2)
Exponential = float(num1) ** float(num2)

if variable == "+":
    print (add)

elif variable == "-":
    print(subtract)

elif variable == "*":
    print(multiply)

elif variable == "/":
    print(divide)
  
elif variable == "//":
    print(Floor Division)

  elif variable == "**":
    print(Exponential)

else:
    print("Error: Invalid Input")
