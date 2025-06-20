# 🔗 Projeto Socket TCP em Python

Este projeto implementa uma comunicação simples via **socket TCP**, simulando a interação entre um servidor e um terminal de chão de fábrica.

---

## 🧠 Funcionamento

O servidor responde aos seguintes comandos enviados pelo cliente:

- 🕐 **`d`** → Retorna a **data e hora atual** do servidor.
- ❌ **`q`** → Encerra a conexão.
- ❓ Qualquer outro → Responde **`what?`**.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python 3.x**
- 📡 **Sockets (TCP/IP)**

---

## 📁 Estrutura do Projeto

```
.
├── servidor.py    # Código do servidor TCP
├── cliente.py     # Código do cliente TCP
└── README.md      # Documentação do projeto
```

---

## 🛠️ Como Executar

### ✅ Passo 1: Clone o repositório

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### ✅ Passo 2: Execute o servidor

Abra um terminal e rode:

```bash
python servidor.py
```

Saída esperada:

```
Servidor TCP aguardando conexão na porta 65432...
```

### ✅ Passo 3: Execute o cliente

Em outro terminal (ou outra aba do terminal):

```bash
python cliente.py
```

### 🗣️ No terminal do cliente, envie comandos:

- `d` → Recebe a data/hora atual do servidor.
- `q` → Encerra a conexão.
- Qualquer outro → Resposta "what?".

---

## 🎯 Exemplo de Execução

### ✔️ Servidor:

```
Servidor TCP aguardando conexão na porta 65432...
Conectado por ('127.0.0.1', 55672)
Recebido: d
Recebido: x
Recebido: q
Servidor encerrado.
```

### ✔️ Cliente:

```
Conectado ao servidor 127.0.0.1:65432
Digite (d para data/hora, q para sair): d
Servidor: 2025-06-17 10:33:21
Digite (d para data/hora, q para sair): x
Servidor: what?
Digite (d para data/hora, q para sair): q
Servidor: Encerrando conexão...
Conexão encerrada.
```

---

## 🐍 Requisitos

- Python 3.x instalado  
  (Só isso, não precisa instalar biblioteca nenhuma além da padrão)

---

## 🔧 Configurações

Se quiser alterar o IP ou porta, edite as seguintes linhas nos arquivos:

- **servidor.py**:

```python
HOST = '0.0.0.0'  # Escuta todas as interfaces
PORT = 65432      # Porta
```

- **cliente.py**:

```python
HOST = '127.0.0.1'  # IP do servidor
PORT = 65432        # Porta do servidor
```

---

## 👨‍💻 Autor

Desenvolvido por **Higor Wilvert** ✌️  
Se quiser, me acha no GitHub, LinkedIn 😎

---

## 🚀 Licença

Este projeto é livre para fins acadêmicos, estudo e zoeira saudável 🤝
