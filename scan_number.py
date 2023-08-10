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
