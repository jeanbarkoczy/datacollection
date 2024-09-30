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
````


## 3 . Vantagens e Desvantagens
Vantagens do Apache Kafka:
Controle Total sobre a Infraestrutura:

Com Kafka, é possível configurar e customizar tópicos, partições, política de retenção, e gerenciar o cluster como um todo, ajustando conforme a necessidade de latência, volume e segurança.
Baixa Latência e Alta Performance:

O Kafka é otimizado para latências muito baixas (geralmente abaixo de 10 milissegundos), o que é ideal para pipelines de dados que exigem entrega quase em tempo real.
Ecossistema Completo:

Com suporte a ferramentas como Kafka Streams (para processamento de fluxos em tempo real) e Kafka Connect (para integração com outras fontes de dados), o Kafka se destaca como uma plataforma robusta para arquiteturas de microserviços.
Integração com Múltiplos Provedores de Cloud e On-Premises:

O Kafka pode ser autogerenciado on-premises, em qualquer provedor de nuvem, ou como um serviço gerenciado com AWS MSK ou Confluent Cloud, permitindo maior flexibilidade.
Comunidade e Código Aberto:

Por ser uma plataforma open-source, o Kafka possui uma vasta comunidade e suporte a uma grande variedade de integrações.
Suporte a Múltiplas APIs:

Oferece suporte nativo a várias APIs, como Producer API, Consumer API, Streams API e Connect API, além de suporte avançado a transações e controle de fluxo.
Benefícios do Kafka:
Alta escalabilidade para grandes volumes de dados, com suporte nativo a milhares de partições e a capacidade de adicionar brokers para aumentar a capacidade de processamento.
Configuração flexível para otimizar performance e retenção de dados, ajustando conforme a necessidade de casos de uso.
Ideal para pipelines de dados complexos com múltiplos consumidores e produtores simultâneos, permitindo a criação de topologias de processamento robustas.



