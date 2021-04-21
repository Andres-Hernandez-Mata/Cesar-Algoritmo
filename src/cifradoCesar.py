"""
Uso: Cifrado César
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 19 Abril 2020
"""

import os

os.system("cls")

mensaje = input('Ingresa el mensaje: ')
llave = 3
modo = 'cifrar'
simbolos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
resultado = ''


for simbolo in mensaje:
    if simbolo in simbolos:
        indice_simbolo = simbolos.find(simbolo)
        if modo == 'cifrar':            
            indice_nuevo = indice_simbolo + llave
        elif modo == 'decifrar':
            indice_nuevo = indice_simbolo - llave
            
        if indice_nuevo >= len(simbolos):
            indice_nuevo = indice_nuevo - len(simbolos)
        elif indice_nuevo < 0:
            indice_nuevo = indice_nuevo + len(simbolos)        
        resultado = resultado + simbolos[indice_nuevo]    
    else:
        resultado = resultado + simbolo
    
print(resultado)
        