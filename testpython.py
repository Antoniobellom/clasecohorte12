



def numero_negativo(num):
    if num > 0:
        return 'es positivo'
    else:
        return 'es negativo'

resultado = numero_negativo(3)        

print(resultado)





def convertir_mayus(string):
    return string.upper()

string_mayus = convertir_mayus('este es el texto')

print(string_mayus)


def numeros_pares(datos):
    for num in datos:
        if num % 2== 0:
            print("el numero es par")
        else:
            print('el numero es impar')

conjunto_de_datos = [2,4,5,6,23,17]

numeros_pares(conjunto_de_datos)

def sumar_lista(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

lista_numeros = [2,2,4,6]

print(sumar_lista(lista_numeros))

def palindromo(palabra):
    return palabra == palabra[::-1]

print(palindromo('radar'))
print(palindromo('ramon'))


def contar_vocales(texto):
    vocales = 'aeiou'
    contador = 0
    for caracteres in texto.lower():
        if caracteres in vocales:
            contador += 1
    return contador

print(contar_vocales('muercielag'))


def contar_letrasA(texto):
    letraA = 'a'
    contador = 0
    for caracteres in texto.lower():
        if caracteres in letraA:
            contador +=1
    return contador

print(contar_letrasA('AndraA'))

def encontrar_maximo(lista):
    i = 0
    maximo = lista[0]
    while i < len(lista):
        if lista[i] > maximo:
            maximo = lista[i]
        i += 1
    return maximo     

numeros = [5, 3, 9, 1]
print(encontrar_maximo(numeros))       

def limpiar_texto(string):
    texto_limpio = string.upper()
    texto_final = texto_limpio.replace(' ','')

    return texto_final

print(limpiar_texto('Mi texto'))    

def formatear_texto(texto):
    palabras = texto.split()
    texto_limpio = ' '.join(palabra.capitalize() for palabra in palabras)
    return texto_limpio

# Ejemplo de uso
texto_mal_formateado = " hola    Mundo!   este texto necesita limpieza  "
print(formatear_texto(texto_mal_formateado))  # Salida: "Hola Mundo! Este Texto Necesita Limpieza"

            
def invertir_numero(n):
    invertido = 0
    signo = 1 if n > 0 else -1
    n = abs(n)
    while n != 0:
        invertido = invertido * 10 + n % 10
        n //= 10
    return invertido * signo

# Ejemplo de uso
numero = 123
print(invertir_numero(numero))  # Salida: 321
      

def esMayorDeEdad(edad):
    if edad >= 18:
        print("es mayor de edad")
    else:
        print("es menor de edad")

edad = int(input("introduce tu edad: "))
esMayorDeEdad(edad)

def fizzbuzz():
    for num in range(1,101):
        if num %3 == 0  and num %5==0:
            print('fizzbuzz')
        elif num %3==0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')     
        else:
            print(num)       

fizzbuzz()            


    




