# Calculadora de Cimentação de Poço com Streamlit e Factory Pattern

## Sobre o projeto

Este projeto consiste em uma aplicação web desenvolvida em Python com Streamlit, voltada para o cálculo de volume em processos de cimentação de poços.

A aplicação permite ao usuário selecionar diferentes tipos de cálculo (Simples, Avançado e Personalizado), utilizando o padrão de projeto Factory para definir dinamicamente a lógica aplicada em cada caso.

## Conceitos aplicados

Programação Orientada a Objetos (POO)
Padrão de projeto Factory
Separação de responsabilidades (Model, Controller)
Desenvolvimento de interface com Streamlit

## Tecnologias utilizadas

Python
Streamlit
Pandas

## Funcionalidades

Seleção do tipo de cálculo: Simples, Avançado e Personalizado
Cálculo de volume com base em parâmetros definidos pelo usuário
Aplicação de coeficientes adicionais nos modos avançado e personalizado
Interface interativa acessada via navegador

## Estrutura do projeto

app.py: interface com o usuário (Streamlit)
controller.py: controle da lógica da aplicação
model.py: definição dos cálculos
factory.py: criação dinâmica dos tipos de cálculo

## Funcionamento

O usuário seleciona o tipo de cálculo desejado na interface.

A aplicação utiliza uma Factory para instanciar o objeto correspondente ao tipo escolhido: CalculoSimples, CalculoAvancado ou CalculoPersonalizado.

Cada classe implementa sua própria lógica de cálculo, garantindo melhor organização e escalabilidade do sistema.

## Como executar

Instalar dependências:

```
pip install streamlit pandas
```

Executar a aplicação:

```
streamlit run app.py
```

Acessar no navegador:

```
http://localhost:8501
```

## Aprendizados

Aplicação prática do padrão Factory
Organização de projetos em camadas
Separação entre interface e lógica de negócio
Desenvolvimento de aplicações web com Streamlit

## Melhorias futuras

Adição de novos tipos de cálculo
Implementação de validação de dados
Persistência de histórico de cálculos
Integração com API

## Observação

Projeto desenvolvido com fins educacionais para prática de conceitos de programação e arquitetura de software.
