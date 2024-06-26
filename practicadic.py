def filtrar(palabra):
    palabra_nueva = palabra.replace('a'," ")
    return palabra_nueva

palabra = input('ingresa la palabra')
resultado = filtrar(palabra)   
print(resultado)






