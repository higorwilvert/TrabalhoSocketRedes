
import socket

# Configurações do servidor (altere se necessário)
HOST = '127.0.0.1'  
PORT = 65432        

# Cria o socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((HOST, PORT))
print(f"Conectado ao servidor {HOST}:{PORT}")

# Loop de interação
while True:
    mensagem = input("Digite (d para data/hora, q para sair): ")

    client_socket.sendall(mensagem.encode())

    if mensagem.lower() == 'q':
        resposta = client_socket.recv(1024).decode()
        print(f"Servidor: {resposta}")
        break

    resposta = client_socket.recv(1024).decode()
    print(f"Servidor: {resposta}")

# Encerra o socket
client_socket.close()
print("Conexão encerrada.")
