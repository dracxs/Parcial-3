#Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso: El Servicio Nacional del Consumidor (SERNAC), está probando una forma simplificada para registrar y gestionar los reclamos de los consumidores. Para ello utiliza solo cuatro campos de información:

#RUT: Rut del reclamante, con DV.
#Fecha: Fecha del reclamo en formato dd-mm-yyyy HH:MM:SS
#Monto: Valor de la compra en miles de pesos.
#Reclamo: Reseña del reclamo en texto libre, de no más de veinte caracteres.

#Y considera las siguientes funcionalidades:
#1. Registrar Reclamo
#2. Listar Reclamos
#3. Respaldar Reclamos
#4. Salir

#Registrar Reclamo: Permite ingresar RUT, Monto y Reclamo
#Listar Reclamos: Se usa para mostrar todos los reclamos ingresados, incluyendo la fecha
#Respaldar Reclamos: Genera un respaldo en archivo de todos los reclamos ingresados en formato CSV.
#El programa debe funcionar hasta que el usuario decida finalizar el programa.


import csv
import os
import datetime

def registrar_reclamo():
    while True:
        rut = input("Ingrese su rut con un guion para el digito verificador: ")
        print("Ejemplo: 12345678-9")
        if validar_rut(rut):
            break
        else:
            print("Rut inválido. Intente nuevamente.")

    while True:
        try:
            fecha = input("Ingrese la fecha del reclamo en formato dd-mm-yyyy HH:MM:SS: ")
            datetime.datetime.strptime(fecha, "%d-%m-%Y %H:%M:%S")
            break
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")

    while True:
        try:
            monto = float(input("Ingrese el monto de la compra en miles de pesos: "))
            break
        except ValueError:
            print("Monto inválido. Intente nuevamente.")

    while True:
        reclamo = input("Ingrese la reseña del reclamo en texto libre, de no más de veinte caracteres: ")
        if len(reclamo) <= 20:
            break
        else:
            print("Reseña inválida. Intente nuevamente.")

    with open("reclamos.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([rut, fecha, monto, reclamo])

def verificar_digito_verificador(rut):
    rut = rut.replace("-", "")
    dv = rut[-1]
    rut = rut[:-1]
    suma = 0
    multiplicador = 2
    for i in range(len(rut) - 1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2
    resto = suma % 11
    resultado = 11 - resto
    if resultado == 11:
        resultado = 0
    elif resultado == 10:
        resultado = "K"
    return str(resultado) == dv

def validar_rut(rut):
    if "-" not in rut:
        return False
    rut = rut.split("-")
    if len(rut) != 2:
        return False
    if not rut[0].isdigit():
        return False
    if not (rut[1].isdigit() or rut[1].upper() == "K"):
        return False
    return verificar_digito_verificador("-".join(rut))

def listar_reclamos():
    with open("reclamos.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def respaldar_reclamos():
    os.rename("reclamos.csv", f"reclamos_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv")

def main():
    while True:
        print("1. Registrar Reclamo")
        print("2. Listar Reclamos")
        print("3. Respaldar Reclamos")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            registrar_reclamo()
        elif opcion == "2":
            listar_reclamos()
        elif opcion == "3":
            respaldar_reclamos()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()

