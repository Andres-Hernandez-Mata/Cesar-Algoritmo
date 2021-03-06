"""
Uso: Cifrado César
Creador: Andrés Hernández Mata
Version: 2.7.0
Python: 3.9.1
Fecha: 19 Abril 2020
"""

import os
from colorama import Fore
from colorama import Style
import pyfiglet as header
from termcolor import colored

os.system("cls")

banner = header.figlet_format("       CESAR").upper()
print(colored(banner.rstrip("\n"), 'blue', attrs=['bold']))
print(colored("By Andrés Hernández Mata | Versión 2.7.0 | LSTI \n", 'red', attrs=['bold']))

def cesar(cifrar):

    while True:
        try:
            mensaje = input('Ingresa la cadena: ')
            llave = int(input('Asignar valor a la llave: '))
            if mensaje != '':
                break
            print(colored("La cadena es un campo obligatorio", 'red', attrs=['bold']))
        except Exception:
            print(colored("Error, por favor ingresa los valores solicitados correctamente", 'red', attrs=['bold']))

    simbolos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    resultado = ''

    try:
        for simbolo in mensaje:
            if simbolo in simbolos:
                indice_simbolo = simbolos.find(simbolo)
                if cifrar:
                    indice_nuevo = indice_simbolo + llave
                elif not cifrar:
                    indice_nuevo = indice_simbolo - llave

                if indice_nuevo >= len(simbolos):
                    indice_nuevo = indice_nuevo - len(simbolos)
                elif indice_nuevo < 0:
                    indice_nuevo = indice_nuevo + len(simbolos)
                resultado = resultado + simbolos[indice_nuevo]
            else:
                resultado = resultado + simbolo
    except Exception as error:
        print(colored(error, 'red', attrs=['bold']))

    return resultado

def select():

    correcto = False
    num = 0

    while(not correcto):
        try:
            num = int(input("Elige una opción: "))
            correcto = True
        except Exception:
            print(colored("Error, introduce un numero entero", 'red', attrs=['bold']))

    return num

salir = False
opcion = 0

try:
    while not salir:
        print ("1. Cifrar")
        print ("2. Decifrar")
        print ("3. Salir")
        opcion = select()
        cifrar = bool()

        if opcion == 1:
            cifrar = True
            resultado = cesar(cifrar)
            os.system("cls")
            print(colored(resultado, 'red', attrs=['bold']))
        elif opcion == 2:
            cifrar = False
            resultado = cesar(cifrar)
            os.system("cls")
            print(colored(resultado, 'red', attrs=['bold']))
        elif opcion == 3:
            salir = True
            print(colored("Bye...", 'red', attrs=['bold']))
        else:
            os.system("cls")
            print(colored("Introduce una opcion valida del menu", 'red', attrs=['bold']))
except Exception as error:
    print(colored(error, 'red', attrs=['bold']))
