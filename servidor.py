
import socket
import datetime

# Configurações do servidor
HOST = '0.0.0.0' 
PORT = 65432   

# Cria o socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind (associa o socket ao host e porta)
server_socket.bind((HOST, PORT))

# Começa a escutar (até 1 conexão na fila)
server_socket.listen(1)
print(f"Servidor TCP aguardando conexão na porta {PORT}...")

# Aceita conexão
conn, addr = server_socket.accept()
print(f"Conectado por {addr}")

# Loop de comunicação
while True:
    data = conn.recv(1024).decode().strip()
    if not data:
        break

    print(f"Recebido: {data}")

    if data.lower() == 'd':
        resposta = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif data.lower() == 'q':
        resposta = "Encerrando conexão..."
        conn.sendall(resposta.encode())
        break
    else:
        resposta = "what?"

    conn.sendall(resposta.encode())

# Encerra a conexão
conn.close()
server_socket.close()
print("Servidor encerrado.")
