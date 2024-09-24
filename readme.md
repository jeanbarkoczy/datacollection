# Projeto da Disciplina Data Collection e Storage
### Implantação de um Kafka com Armazenamento Local

## 1. Desenho de Arquitetura

### 1.1 Fluxo de Dados:

- **1.1.1** O Producer envia mensagens para o Kafka Cluster, que podem ser roteadas para qualquer um dos brokers.
  
- **1.1.2** Os brokers distribuem as mensagens entre si para garantir replicação e alta disponibilidade.
  
- **1.1.3** O Consumer lê as mensagens do Kafka Cluster. Ele pode se conectar a qualquer broker para consumir dados de um tópico específico.
  
- **1.1.4** O Zookeeper coordena a atividade dos brokers, mantendo a integridade do cluster.

![kafka](https://github.com/user-attachments/assets/fa5c8826-af05-471e-9312-86ad77d44005)

## 2. O que é o Kafka 

- *** O Apache Kafka é uma plataforma de streaming distribuída que permite a criação de pipelines de dados em tempo real e aplicações de streaming.

## 2. Manual do Sistema

### Passo a Passo para o Desenvolvimento:

1. Instale os pré-requisitos e ferramentas necessárias para rodar o Kafka localmente.
   
   **Pré-requisitos**:
   - Xcode
   - Java
   - Acesso elevado na máquina

2. Para instalar o Kafka via Homebrew, execute o seguinte comando:

   ```bash
   brew install kafka

3. Inicializar Zookeeper
    ```bash
    bin/zookeeper-server-start.sh config/zookeeper.properties

4. Inicializar o Kafka
   ```bash
   bin/kafka-server-start.sh config/server.properties
5. Criar tópico no Kafka
   ```bash
   bin/kafka-topics.sh --create --topic macklake-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 17
6. Criado um produtor em Python
   ```python
   from kafka import KafkaProducer
    import time

    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    #  caminho do arquivo onde as mensagens produzidas serão salvas
    arquivo_mensagens = '/tmp/mensagens_produzidas.txt' 


    # Função para enviar mensagens
   def enviar_mensagens():
    with open(arquivo_mensagens, 'a') as f:  
        for i in range(10):
            mensagem = f"Mensagem {i} - Teste de mensagem Kafka"   # Mensagem a ser enviada
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
7. Criado um consumidor em Python
   ```python
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
    ler_mensagens_arquivo()gi
