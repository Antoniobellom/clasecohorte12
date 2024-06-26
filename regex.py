import re

# Ejemplo de texto con enlaces
texto = """
Visita nuestro sitio web en https://www.ejemplo.com o sigue nuestro blog en http://blog.ejemplo.com. 
También puedes encontrar más información en www.otroe.jemplo.com. Aquí hay un enlace sin www: http://ejemplo.com/path.
"""

# Dos expresiones regulares para encontrar enlaces
patrones = [
    r'https?://(?:www\.)?[\w-]+(?:\.[\w-]+)+(?:/[\w./?%&=-]*)?',
    r'www\.[\w-]+(?:\.[\w-]+)+(?:/[\w./?%&=-]*)?'
]

# Aplicar cada patrón al texto y mostrar resultados
for i, patron in enumerate(patrones):
    print(f"Resultados para el patrón {i + 1}:")
    enlaces = re.findall(patron, texto)
    for enlace in enlaces:
        print(enlace)
    print("\n")

