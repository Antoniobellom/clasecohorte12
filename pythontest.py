


palabra = input('Ingrese tu palabra: ')
def contar_palabras(palabras):

    
    palabras_lista = palabras.split(' ')
    contador = len(palabras_lista)
    return contador

numero_de_palabras = contar_palabras(palabra)
print(f"El número de palabras es: {numero_de_palabras}")

estutiantes = ['antonio','loreto','felipe']

for estudiante in estutiantes:
    print(f'estos son los estudiantes nuevos:{estudiante}')









def  esMayor(edad):
    if edad >=18:
        print('eres mayor de edad')
    else:
        print('eres menor de edad')   

edad = int(input('introduce tu edad'))
esMayor(edad)

def fizzbuzz(num):
    if num % 3 == 0 and num %5 == 0:
        print('fizzbuzz')
    elif num %3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print(num)  
num = int(input('tu numero es'))        
fizzbuzz(num)         

def vive_cerca(distancia):
    if distancia >= 1000:
        print('vive  muy lejos')
    elif distancia >= 500:
        print('vive lejos')    
    else:
        print('vive cerca')    

distancia = int(input('introduce tu distancia'))
vive_cerca(distancia)

def suma(a,b):
    return a + b

def filtrar(palabra):
    palabra_nueva = palabra.replace('a', " ")
    return palabra_nueva

palabra = input('Introduce tu palabra: ')
resultado = filtrar(palabra)
print('Resultado:', resultado)









