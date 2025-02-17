# Log Generator

Apenas um gerador de logs para um futuro projeto de análise de logs.

## Descrição

Este projeto consiste em um script que gera diversos logs simulando eventos de um sistema e os publica em uma fila do RabbitMQ. Os logs serão consumidos posteriormente por outra aplicação, que será desenvolvida em Go, para análise e processamento.

## Objetivo

O objetivo principal é criar um fluxo contínuo de geração e envio de logs para um message broker (RabbitMQ), permitindo que outra aplicação os processe de forma assíncrona. Isso possibilita a análise de padrões, detecção de anomalias e auditoria de eventos em um sistema distribuído.

## Funcionalidades

- Gerar logs automaticamente em diferentes níveis (INFO, WARNING, ERROR, DEBUG, etc.).
- Simular eventos diversos, como acessos de usuários, falhas no sistema e operações de banco de dados. (TODO)
- Publicar os logs em uma fila do RabbitMQ para processamento assíncrono.
- Configuração flexível para definir o volume e frequência da geração dos logs. (TODO)

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Mensageria**: RabbitMQ

## Próximos Passos

- Melhorar formato do log e criar mais tipos de eventos.
- Implementar configuração para definir volume e frequência da geração de logs.
- Criar a aplicação em Go para consumir e processar os logs.
