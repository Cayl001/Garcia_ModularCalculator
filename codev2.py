def addition(num1, num2):
  return num1 + num2

def subtraction(num1, num2):
  return num1 - num2
  
def multiplication(num1, num2):
  return num1 * num2

def division(num1, num2)
 if num2==0:      
    return "Error: Cannot divide by zero."
  else:
    return num1 / num2

print("===== MODULAR CALCULATOR =====")
print("1. Addition (+)")
print("2. Subraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Choose an operation (1-4):  ")

num1 = float(input("Enter the first number:  "))
num2 = float(input("Enter the second number:  "))

if choice == "1":
  result = addition(num1, num2)
  print("Result:  ", result)
elif choice == "2":
  result = subtraction(num1, num2)
  print("Result:  ", result)
elif choice == "3":
  result = multiplication(num1, num2)
  print("Result:  ", result)
elif choice == "4":
  result = division(num1, num2)
  print("Result:  ", result)
else:
  print("Invalid choice, please select 1-4.")
