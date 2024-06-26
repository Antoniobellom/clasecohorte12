#Imprimir Números del 1 al 10
for i in range(1, 11):
    print(i)

#Suma de los Primeros N Números
n = int(input("Introduce un número: "))
suma = 0
for i in range(1, n+1):
    suma += i
print(f"La suma de los primeros {n} números es: {suma}")

#Tabla de Multiplicar
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#Listar Elementos de una Lista
lista = ["manzana", "banana", "cereza", "durazno"]
for fruta in lista:
    print(fruta)

#Contar Vocales en una Cadena
cadena = input("Introduce una cadena de texto: ")
vocales = "aeiouAEIOU"
contador = 0
for letra in cadena:
    if letra in vocales:
        contador += 1
print(f"La cadena contiene {contador} vocales.")


#Ejercicios de Python para while
#Contar del 1 al 10
i = 1
while i <= 10:
    print(i)
    i += 1

#Sumar Números hasta 0
suma = 0
numero = int(input("Introduce un número (0 para terminar): "))
while numero != 0:
    suma += numero
    numero = int(input("Introduce un número (0 para terminar): "))
print(f"La suma de los números es: {suma}")



#Menú Interactivo
opcion = ""
while opcion != "4":
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        print("Elegiste la opción 1.")
    elif opcion == "2":
        print("Elegiste la opción 2.")
    elif opcion == "3":
        print("Elegiste la opción 3.")
    elif opcion == "4":
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Intenta de nuevo.")

#Promedio de Notas
suma = 0
contador = 0
continuar = "sí"
while continuar.lower() == "sí":
    nota = float(input("Introduce una nota: "))
    suma += nota
    contador += 1
    continuar = input("¿Quieres introducir otra nota? (sí/no): ")
if contador > 0:
    promedio = suma / contador
    print(f"El promedio de las notas es: {promedio:.2f}")
else:
    print("No se introdujeron notas.")


def fizzbuzz(num):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

fizzbuzz(3)



def es_primo(num):
    if num == 1 or num == 0:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

print(es_primo(0))
print(es_primo(1))
print(es_primo(83))
print(es_primo(97*97))
print(es_primo(9409))
print(es_primo(100003)



#Adivinar el Número
import random
numero_secreto = random.randint(1, 100)
adivinanza = int(input("Adivina el número entre 1 y 100: "))
while adivinanza != numero_secreto:
    if adivinanza < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    else:
        print("Demasiado alto. Intenta de nuevo.")
    adivinanza = int(input("Adivina el número entre 1 y 100: "))
print("¡Felicidades! Has adivinado el número.")









