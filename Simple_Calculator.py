def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: You can't divide by zero")
        return None
    else:
        return x / y

print("Welcome to Simple Calculator!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Choose an operation (1-4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print("Result:", num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print("Result:", num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            result = divide(num1, num2)
            if result is not None:

                print("Result:", num1, "/", num2, "=", result)
    else:
        print("Invalid input")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        print("Goodbye!")
        break
