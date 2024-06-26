def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Error: División por cero"
    return x / y

def calculadora():

    while True:


def calculadora():
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    while True:
        try:
            eleccion = int(input("Ingrese su elección (1/2/3/4): "))
            if eleccion in [1, 2, 3, 4]:
                break
            else:
                print("Elección no válida. Por favor, ingrese un número entre 1 y 4.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
    
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese números válidos.")
    
    if eleccion == 1:
        print(f"{num1} + {num2} = {suma(num1, num2)}")
    elif eleccion == 2:
        print(f"{num1} - {num2} = {resta(num1, num2)}")
    elif eleccion == 3:
        print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
    elif eleccion == 4:
        print(f"{num1} / {num2} = {division(num1, num2)}")

if __name__ == "__main__":
    calculadora()


