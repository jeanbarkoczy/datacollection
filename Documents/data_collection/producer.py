from kafka import KafkaProducer
import time

# Cria o produtor Kafka
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Caminho do arquivo onde as mensagens serão salvas
arquivo_mensagens = '/tmp/mensagens_produzidas.txt'  # Altere o caminho conforme necessário

# Função para enviar mensagens
def enviar_mensagens():
    with open(arquivo_mensagens, 'a') as f:  # Abrir o arquivo para escrita
        for i in range(10):
            mensagem = f"Mensagem {i} - Teste de Kafka"
            f.write(f"{mensagem}\n")  # Salvar a mensagem no arquivo
            producer.send('macklake-topic', mensagem.encode('utf-8'))  # Enviar a mensagem para o Kafka
            print(f"Mensagem enviada e salva: {mensagem}")
            time.sleep(1)  # Atraso para visualizar o envio gradual das mensagens

# Enviar as mensagens
if __name__ == "__main__":
    enviar_mensagens()

# Fecha o produtor
producer.flush()
producer.close