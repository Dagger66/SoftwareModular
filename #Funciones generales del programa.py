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

#Listados menú Hotel
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
        dni = input("Buscar ficha por DNI: ")

        encontrar_cliente = False
        for client in lista_clientes:
            if client["dni"] == dni:
                encontrar_cliente = True
                # Muestra la informacion del cliente
                MenuClientes.mostrar_datos_cliente(dni)

                #Procede a registrar la reserva
                habitacion = input("Asignar habitación: ")
                numero_personas = input("Número de personas a ingresar: ")
                observacion = input("Observación: ")
                print(f"Cargado con éxito en hab.{habitacion}")
                limpiar_terminal(segundos=2)
                break

        if not encontrar_cliente:
            # Si no encuentra ficha del cliente, pregunta si quieres crear una nueva.
            crear_ficha = input(f"El cliente con DNI {dni} no tiene ficha creada. ¿Desea crear una? (S/N): ").upper()
            if crear_ficha == "S":
                #Llama a agregar cliente para crear una nueva ficha
                MenuClientes.agregar_cliente()
            else:
                print("Volviendo al menú anterior...")
                limpiar_terminal(segundos=1)
                return  #Retorna al menú anterior

    def mostrar_listado_clientes():
        limpiar_terminal()
        for i in lista_clientes:
            print("-"*50)
            print(f"{Back.BLUE} {i['nombreCompleto'].upper()} /// Telefono: {i['TEL'].title()} /// Observación: {i['observacion'].title()}{Style.RESET_ALL} ///#Fecha de creacion de ficha", end="\n")

    def mostrar_menú_clientes():
        limpiar_terminal()
        "Para volver atrás puse Esc"
        op = int(input("""
        1-Registrar Reserva:
        2-Agregar ficha clientes:
        3-Editar datos de cliente:
        4-Mostrar listado de clientes:
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
