def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x, y):
    return x * y

def divide(x,y):
    return x/y

def main():
    x = float(input("Input a number: "))
    y = float(input("Input another number: "))

    print("Add result: " + str(add(x,y)))
    print("Subtract result: " + str(subtract(x,y)))

    x = float(input("Input a number: "))
    y = float(input("Input another number: "))

    print("Multiply result: " + str(multiply(x,y)))
    print("Divide result: " + str(divide(x,y)))

main()