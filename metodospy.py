
def filtrar(palabra):
    palabra_nueva = palabra.replace('a', " ")
    return palabra_nueva

def filtradonuevo(palabra):
    palabra_nueva = palabra.replace(" ", 'A')
    return palabra_nueva

palabra = input('Introduce tu palabra: ')

# Usamos la primera función para cambiar 'a' por espacio
resultado = filtrar(palabra)
print("Después de filtrar (a -> espacio):", resultado)

# Usamos la segunda función para cambiar el espacio por 'A'
resultado_new = filtradonuevo(resultado)
print("Después de filtrar nuevo (espacio -> A):", resultado_new)

numeros = [1,2,3]

for numero in numeros:
    numero_nuevo = numeros + numero
    return numero_nuevo

      