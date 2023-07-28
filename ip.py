from socket import socket, AF_INET, SOCK_DGRAM
from servidor import escreve_servidor
from banco import escreve_banco
from pathlib import Path

# Paths
apache_path = Path(R'C:\xampp\apache\conf\httpd.conf')
mysql_path = Path(R"C:\xampp\mysql\bin\my.ini")
system_path_js = Path(R"C:\xampp\htdocs\Suits\urlbase.js")
system_path_php = Path(R"C:\xampp\htdocs\Suits\urlbase.php")
navegador_path = Path(R"C:\Suits\dependencias\host\site.txt")

# IP
s = socket(AF_INET, SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

# Write
servidor = escreve_servidor(s.getsockname()[0])
database = escreve_banco(s.getsockname()[0])
navegador = f"http://{s.getsockname()[0]}/suits/"

with open(apache_path, "w") as file:
    file.write(servidor)
    file.close()

with open(mysql_path, "w") as file:
    file.write(database)
    file.close()

with open(system_path_js, "w") as file:
    file.write(f'export var url = "http://{s.getsockname()[0]}/"')
    file.close()

with open(system_path_php, "w") as file:
    file.write(f'<?php\n$url = "http://{s.getsockname()[0]}";')
    file.close()

with open(navegador_path, "w") as file:
    file.write(navegador)
    file.close()
