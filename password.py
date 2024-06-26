import re

# Ejemplo de contraseñas a validar
contrasenas = [
    "Password123.",
    "passw0rd",
    "PASSWORD123.",
    "Pass123.",
    "P@ssw0rd",
    "Valid1Password."
]

# Expresión regular para validar contraseñas
patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*\.)[A-Za-z\d\.]{8,}$'

# Validar cada contraseña
for contrasena in contrasenas:
    if re.match(patron, contrasena):
        print(f"'{contrasena}' es válida")
    else:
        print(f"'{contrasena}' no es válida")
#acabo de cambiar otra vez      
