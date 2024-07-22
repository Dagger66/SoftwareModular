#Funciones generales del programa
def fecha():
    """Devuelve la fecha en formato dd/mm/aaaa y la hora en hh:mm"""
    return datetime.datetime.now().strftime("%d/%m/%Y  %H:%M")

def limpiar_terminal(segundos = 0):
    """Limpia la terminal después de una espera opcional."""
    if segundos > 0:
        time.sleep(segundos)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Inicializadores para funciones generales
import os  
import time
import datetime
from colorama import Back, Fore, init, Style
import json

#Menú clientes
lista_clientes = []

class MenuClientes:

    def agregar_cliente():

        cliente = [{
            "nombre" : str(input("Agregar nombre: ")),
            "apellido" : str(input("Agregar apellido: ")),
            "dni" : float(input("Agregar dni: ")),
            "TEL" : float(input("Agregar telefono: ")),
            "factura" : str(input("Requiere factura?: ")),
            "empresa" : str(input("Empresa: ")),
            "abona" : str(input("Abona: ")),
            "observacion" : str(input("Observación: "))
        }
        ]
        lista_clientes.extend(cliente)
        limpiar_terminal()

    def mostrar_listado_clientes():
        limpiar_terminal()
        for i in lista_clientes:
            print("-"*25)
            print(f"{Back.BLUE} {i['apellido'].upper()} {i['nombre'].title()}{Style.RESET_ALL}", end="\n")

    def mostrar_menú_clientes():
        limpiar_terminal()
        "Para volver atrás puse Esc"
        op = int(input(""" 
        1-Registrar reserva.
            #Buscar cliente. #para buscar por DNI
                #DNI no registrado en sistema < volver atrás automaticamente
        2-Agregar cliente nuevo. #Para que quede en una base de datos
        3-Editar datos de cliente
        4-Mostrar listado de clientes.
    """))
        match op:
            case 1:
                limpiar_terminal()
            case 2:
                limpiar_terminal()
                MenuClientes.agregar_cliente()
            case 3:
                limpiar_terminal()
            case 4:
                limpiar_terminal()
                MenuClientes.mostrar_listado_clientes()

#Menú principal
class MenuPrincipal:
    def mostrar_menu_principal():
        print()
        op = int(input("""Seleccione que acciones desea realizar: 
        1-Menú Clientes.
        2-Menú Hotel.
        3-Salir
        """))
        match op:
            case 1:
                MenuClientes.mostrar_menú_clientes()
            case 2:
                print("Desplega menú Hotel")
            case _:
                limpiar_terminal()
                False

while True:

    MenuPrincipal.mostrar_menu_principal()
