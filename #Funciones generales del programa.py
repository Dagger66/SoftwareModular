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

#Listados menú clientes
registrar_reserva = []
lista_clientes = []
listado_de_habitaciones = []

class MenuClientes:

    def agregar_cliente():
        cliente = [{
            "nombreCompleto" : str(input("Nombre completo: ")),
            "dni" : str(input("Agregar dni: ")),
            "TEL" : str(input("Agregar telefono: ")),
            "empresa" : str(input("Empresa: ")),
            "observacion" : str(input("Observación (Tipo de factura): ")),
        }
        ]
        lista_clientes.extend(cliente)
        limpiar_terminal()

    def mostrar_datos_cliente(dni):
        for cliente in lista_clientes:
            if cliente["dni"] == dni:
                print(f"DATOS DEL CLIENTE")
                print(f"Nombre completo: {cliente['nombreCompleto']}")
                print(f"Teléfono: {cliente['TEL']}")
                print(f"Empresa: {cliente['empresa']}")
                print(f"Observación: {cliente['observacion']}")
            return True
        else:
            print(f"No se encontró un cliente con DNI {dni}")
            return False

    def registrar_reserva():
    # En caso de que el dni no coincida con uno registrado, deberá mostrar el mensaje de El cliente no cuenta con ficha, ¿desea crear una? S/N.
        dni = input("Buscar ficha por DNI: ")
        for cliente in lista_clientes:
            if dni == cliente.get("dni"):
                MenuClientes.mostrar_datos_cliente(dni)
                habitacion = (input("Asignar habitacion: "))
                (input("Numero de personas a ingresar: "))
                (input("Observación: "))
                print(f"Cargado con éxito en hab.{habitacion}")
                limpiar_terminal(segundos=2)
            else:
                respuesta = input("El cliente no cuenta con ficha, ¿desea crear una? S/N: ")
                if respuesta.upper() == "S":  # Validate user input
                    MenuClientes.agregar_cliente()
                else:
                    print("Registro de cliente cancelado.")  # Or take appropriate action
                    limpiar_terminal()
        #Si la reserva a registrar no tiene una ficha guardada, se debe pedir que se cree una, 
        # luego podrá registrar la reserva. "EL CLIENTE NO CUENTA CON FICHA CREADA, CREAR UNA? SI/NO"
        #En caso de que tenga ficha, antes de agendar la reserva deberá pedir que se revisen los datos 
        # y que deje modificar si es necesario
        #Si los datos con correctos registrar reserva es OK.

    def mostrar_listado_clientes():
        limpiar_terminal()
        for i in lista_clientes:
            print("-"*50)
            print(f"{Back.BLUE} {i['nombreCompleto'].upper()} /// Telefono: {i['TEL'].title()} /// Factura: {i['observacion'].title()}{Style.RESET_ALL}", end="\n")

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
                MenuClientes.registrar_reserva()
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
