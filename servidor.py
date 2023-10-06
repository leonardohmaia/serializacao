import socket

# Configurações do servidor
endereco_servidor = '127.0.0.1'
porta_servidor = 8888

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((endereco_servidor, porta_servidor))
        s.listen()

        print(f"Servidor ouvindo em {endereco_servidor}:{porta_servidor}")

        while True:
            conn, addr = s.accept()
            print(f"Conexão estabelecida por {addr}")

            # Receber e manipular os dados
            dados_completos = conn.recv(4096).decode()

            formatos = dados_completos.split('\n')

            for formato in formatos:
                formato_dividido = formato.split(':', 1)
                if len(formato_dividido) > 1:
                    formato_nome = formato_dividido[0]
                    formato_dados = formato_dividido[1]

                    print(formato_nome + ":", formato_dados)

            conn.close()

if __name__ == "__main__":
    main()
