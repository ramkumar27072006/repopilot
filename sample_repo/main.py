from calculator import add, subtract, multiply, divide

def main():
    print("Welcome to simple calc")
    print("Choose operation: +  -  *  /")

    op = input("Enter operation: ").strip()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == "+":
        print(f"{a} + {b} = {add(a, b)}")
    elif op == "-":
        print(f"{a} - {b} = {subtract(a, b)}")
    elif op == "*":
        print(f"{a} * {b} = {multiply(a, b)}")
    elif op == "/":
        try:
            print(f"{a} / {b} = {divide(a, b)}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
