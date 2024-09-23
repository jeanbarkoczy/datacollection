# Projeto da Disciplina Data Collection e Storage
### Implantação de um Kafka com Armazenamento Local

## 1. Desenho de Arquitetura

### 1.1 Fluxo de Dados:

- **1.1.1** O Producer envia mensagens para o Kafka Cluster, que podem ser roteadas para qualquer um dos brokers.
  
- **1.1.2** Os brokers distribuem as mensagens entre si para garantir replicação e alta disponibilidade.
  
- **1.1.3** O Consumer lê as mensagens do Kafka Cluster. Ele pode se conectar a qualquer broker para consumir dados de um tópico específico.
  
- **1.1.4** O Zookeeper coordena a atividade dos brokers, mantendo a integridade do cluster.

![kafka](https://github.com/user-attachments/assets/fa5c8826-af05-471e-9312-86ad77d44005)

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


