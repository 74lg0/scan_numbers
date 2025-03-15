import dns.resolver
import smtplib
from colorama import Fore, init

init(autoreset=True)

def check_email_smtp(email):
    # Obtener el dominio del correo electrónico
    domain = email.split('@')[1]
    
    try:
        # Obtener los registros MX del dominio
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_servers = [str(r.exchange) for r in mx_records]

        # Probar cada servidor MX
        for mx_server in mx_servers:
            try:
                # Crear una conexión SMTP al servidor MX
                with smtplib.SMTP(mx_server, timeout=10) as server:
                    server.set_debuglevel(0)
                    server.helo()  # Identificar el cliente al servidor
                    server.mail('you@example.com')  # Dirección de correo del remitente (puede ser cualquier dirección válida)
                    code, message = server.rcpt(email)  # Intentar enviar al destinatario
                    server.quit()

                    # Verificar la respuesta del servidor
                    if code == 250:
                        return True  # El correo electrónico es válido
                    else:
                        return False  # El correo electrónico no es válido

            except Exception as e:
                print(f"Error al conectar con el servidor MX {mx_server}: {e}")

    except Exception as e:
        print(f"Error al obtener registros MX: {e}")
    
    return False  # Si no se pudo verificar la dirección

# Ejemplo de uso
email = input('Email => ')
is_valid = check_email_smtp(email)
if is_valid:
    print(Fore.YELLOW+f"{email}"+Fore.GREEN+" parece ser una dirección de correo válida.")
else:
    print(Fore.RED+f"{email} no parece ser una dirección de correo válida.")
