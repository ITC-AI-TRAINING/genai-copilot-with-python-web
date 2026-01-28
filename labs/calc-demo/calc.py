import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def log(x):
    if x <= 0:
        return "Error! Logarithm undefined for non-positive numbers."
    return math.log10(x)

def sqrt(x):
    if x < 0:
        return "Error! Square root undefined for negative numbers."
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def calculator():
    print("Scientific Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Sin")
    print("6. Cos")
    print("7. Tan")
    print("8. Log (base 10)")
    print("9. Square Root")
    print("10. Power")
    
    while True:
        choice = input("\nEnter choice (1-10) or 'q' to quit: ")
        
        if choice == 'q':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Result: {num1} ÷ {num2} = {result}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        elif choice in ['5', '6', '7', '8', '9']:
            try:
                num = float(input("Enter number: "))
                
                if choice == '5':
                    print(f"Result: sin({num}°) = {sin(num)}")
                elif choice == '6':
                    print(f"Result: cos({num}°) = {cos(num)}")
                elif choice == '7':
                    print(f"Result: tan({num}°) = {tan(num)}")
                elif choice == '8':
                    result = log(num)
                    print(f"Result: log10({num}) = {result}")
                elif choice == '9':
                    result = sqrt(num)
                    print(f"Result: √{num} = {result}")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        elif choice == '10':
            try:
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print(f"Result: {base} ^ {exponent} = {power(base, exponent)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid choice! Please select 1-10.")

if __name__ == "__main__":
    calculator()