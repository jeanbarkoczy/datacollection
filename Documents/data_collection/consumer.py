# Função para ler mensagens do arquivo
def ler_mensagens_arquivo():
    arquivo_mensagens = '/tmp/mensagens_produzidas.txt'  # O mesmo caminho usado pelo produtor
    try:
        with open(arquivo_mensagens, 'r') as f:  # Abrir o arquivo para leitura
            for linha in f:
                print(f"Mensagem lida do arquivo: {linha.strip()}")
    except FileNotFoundError:
        print(f"Arquivo {arquivo_mensagens} não encontrado. Certifique-se de que o produtor o criou corretamente.")

# Iniciar o consumo das mensagens do arquivo
if __name__ == "__main__":
    ler_mensagens_arquivo()