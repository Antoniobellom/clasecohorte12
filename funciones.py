def es_primo(numero):
    if numero == 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print(es_primo(1))
print(es_primo(2))
print(es_primo(17*17))
print(es_primo(17))

def saludar(nombre):
    print(f'hola {nombre}')

nombre = input('di tu nombre ')   
saludar(nombre) 


def esMayor(edad):
    if edad > 18:
        print('es mayor')

edad = int(input('tu edad?'))
esMayor(edad)

def numeroImpar(x):
    if x % 2 != 0:
        numbers = x**0.5
        if numbers == int(numbers):  
            numbers = int(numbers)  
        print(numbers, "es primo")
    else:
        print(x, "no es primo")

