def calcular_subredes(direccion_red, mascara_subred):
    direccion_red_octetos = direccion_red.split('.')
    mascara_subred_octetos = mascara_subred.split('.')

    print(f"Dirección de red: {direccion_red}")
    print(f"Máscara de subred: {mascara_subred}")

    primera_subred = f"{direccion_red_octetos[0]}.{direccion_red_octetos[1]}.{direccion_red_octetos[2]}.0"
    segunda_subred = f"{direccion_red_octetos[0]}.{direccion_red_octetos[1]}.{direccion_red_octetos[2]}.128"

    print(f"Primera subred: {primera_subred} - Rango de IP: {primera_subred[:-1]}1 a {primera_subred[:-1]}126")
    print(f"Segunda subred: {segunda_subred} - Rango de IP: {segunda_subred[:-1]}129 a {segunda_subred[:-1]}254")

direccion_red = "192.168.1.0"
mascara_subred = "255.255.255.128"

calcular_subredes(direccion_red, mascara_subred)
