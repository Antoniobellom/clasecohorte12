import re

# Ejemplo de texto con enlaces
texto = """
Visita nuestro sitio web en https://www.ejemplo.com o sigue nuestro blog en http://blog.ejemplo.com. 
También puedes encontrar más información en www.otroe.jemplo.com.
"""
numeros = """ asdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdf
asdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdf
asdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfvvasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfvasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfvvasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfvvasdfasdfasdf 17.804.111-9 17.804.333-7 17.123.456-6 asasdfasdfv """



# Expresión regular para encontrar enlaces
#patron = r'https?://(?:www\.)?[\w-]+(?:\.[\w-]+)+(?:/[\w./?%&=-]*)?|www\.[\w-]+(?:\.[\w-]+)+(?:/[\w./?%&=-]*)?'
patron = r'https:\/\/www\.ejemplo\.com(\/[^\s]*)?'
patron_numeros = r'\d{1,2}\.\d{3}\.\d{3}-[\dkK]'


# Encontrar todos los enlaces en el texto
enlaces = re.findall(patron, texto) # tiene que recibir el patron y el texto
rut_encontrados =re.findall(patron_numeros,numeros)
# Imprimir los enlaces encontrados
print("Enlaces encontrados:")
for enlace in enlaces:
    print(f'https://www.ejemplo.com{enlace}')

# Imprimir los RUT encontrados y almacenarlos en una lista nueva
print("\nRUT encontrados:")
rut_nuevos = []
for rut in rut_encontrados:
    print(rut)
    rut_nuevos.append(rut)

print("\nLista de RUT nuevos:")
print(rut_nuevos)
