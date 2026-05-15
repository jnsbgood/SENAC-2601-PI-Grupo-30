# SENAC-2601-PI-Grupo-30
DESENVOLVIMENTO LOW CODE EM CIÊNCIA DE DADOS

## Tema: Análise do Dataset Credit Card Customers

#### Integrantes:
1. Rodrigo Alan Siqueira dos Santos
2. Janiny Andrade da Nobrega
3. Stephanny da Silva Nascimento
4. Igor da Silva Porto
5. Lucca Novello Santos
6. Johnny Nunes Santos
7. Leonardo Sales Araújo

![COLABORADORES_PROJETO_SENAC](https://github.com/user-attachments/assets/997d1b48-24df-4779-bbc8-41b501a144a4)

## Definição da base de dados e Objetivos:
A base de dados cujo nome é: "Credit Card customers" origina-se da plataforma Kaggle. Esta base apresenta um registro histórico na relação de clientes ativos e inativos de cartões de crédito de uma agência bancária.

Nosso objetivo é realizar o mapeamento do perfil demográfico e comportamental dos clientes propensos ao cancelamento do produto e, a partir da identificação dos mesmos, utilizar de métricas preditivas e estratégias de retenção personalizadas para impedir a queda de usuários da agencia que usaremos como base. A criação deste modelo de inteligência de dados tem como propósito a aplicação em toda a rede bancária.

## Planejamentos das Tarefas:
Dividimos as tarefas em 2 grupos responsáveis:

Primeiro grupo formado por Johnny, Janiny, Leonardo e Rodrigo.
 - Ficaram responsáveis pela análise e desenvolvimento do Dashboard.

Segundo grupo formado por Stephanny, Igor e Lucca.
 - Ficaram responsáveis pelo desenvolvimento do README.

## Cronograma Sugerido
- Semana 1: Entendimento da base e preparação dos dados
- Semana 2: Análise exploratória e primeiras impressões
- Semana 3: Análise de dados prescritiva e definição de estratégias de retenção
- Semana 4: Elaboração do Dashboard e revisão final

## Transformações a Realizar
- Criação de variáveis derivadas (Renda/Limite de Crédito).

## Estrutura Inicial do Dashboard:
Visualizações:
- Distribuição Demográfica: Clientes por idade, faixa salarial e categoria do cartão 
- Comparativo entre clientes ativos x Clientes que cancelaram o cartão

Métricas:
- Acurácia
- Precisão: Percentual de clientes previstos como "churn" que realmente cancelaram o cartão
- Sensibilidade: Percentual de clientes corretamente identificados que realmente cancelaram o cartão

# Como Rodar o Projeto

Abaixo está o passo a passo para rodar o projeto em qualquer computador.

---

## 1. Baixar ou Abrir o Projeto

Abra a pasta do projeto no VS Code.

A pasta principal deve conter os arquivos:

```text
app/
data/
src/
requirements.txt
README.md
```

Confira se o arquivo original está dentro da pasta `data`:

```text
data/BankChurners.csv
```

---

## 2. Abrir o Terminal no VS Code

No VS Code, clique em:

```text
Terminal > New Terminal
```

Ou use o atalho:

```text
Ctrl + Shift + '
```

---

## 3. Criar o Ambiente Virtual

No terminal, digite:

```bash
python -m venv venv
```

Esse comando cria uma pasta chamada `venv`, que será o ambiente isolado do projeto.

---

## 4. Ativar o Ambiente Virtual

### No Windows

Digite:

```bash
venv\Scripts\activate
```

Se funcionar, aparecerá algo parecido com isso no início da linha do terminal:

```bash
(venv)
```

Exemplo:

```bash
(venv) PS C:\Users\SeuNome\Projeto>
```

Isso significa que o ambiente virtual está ativado.

### No Linux ou Mac

Digite:

```bash
source venv/bin/activate
```

---

## 5. Instalar as Dependências

Com o ambiente virtual ativado, digite:

```bash
pip install -r requirements.txt
```

Esse comando instala automaticamente todas as bibliotecas necessárias para o projeto funcionar.

O arquivo `requirements.txt` deve conter:

```txt
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
```

---

## 6. Preparar a Base de Dados

Primeiro, execute o arquivo de preparação da base:

```bash
python src/preparacao_base.py
```

Esse comando cria o arquivo:

```text
python src/preparacao_base.py
```

Depois, execute o ETL:

```bash
python src/etl.py
```

Esse comando adiciona novas colunas importantes na base, como:

- `Status_Cliente`;
- `Faixa_Etaria`;
- `Perfil_Risco`.

---

## 7. Rodar a Análise Exploratória

Para visualizar estatísticas e gráficos simples, execute:

```bash
python src/analise_exploratoria.py
```

Esse arquivo mostra informações iniciais da base, como distribuição de idade e comparação entre clientes ativos e cancelados.

---

## 8. Rodar o Modelo Preditivo

Para executar o modelo de churn, digite:

```bash
python src/modelo.py
```

O terminal deve mostrar a acurácia do modelo, por exemplo:

```text
Acurácia do modelo: 0.85
```

O valor pode variar dependendo dos dados e das variáveis utilizadas.

---

## 9. Rodar o Dashboard

Para abrir o dashboard interativo, execute:

```bash
streamlit run app/dashboard.py
```

Depois disso, o Streamlit abrirá automaticamente uma página no navegador.

Caso não abra sozinho, copie o link que aparecer no terminal e cole no navegador.

Normalmente será algo parecido com:

```text
http://localhost:8501
```

---

# Ordem Correta Para Rodar o Projeto

Sempre rode os arquivos nesta ordem:

```bash
python src/preparacao_base.py
python src/etl.py
python src/analise_exploratoria.py
python src/modelo.py
streamlit run app/dashboard.py
```

---

# O Que Aparece no Dashboard

O dashboard apresenta:

- total de clientes;
- quantidade de clientes cancelados;
- taxa de cancelamento;
- idade média dos clientes;
- gráfico de clientes ativos e cancelados;
- gráfico de perfil de risco;
- cancelamento por faixa etária;
- cancelamento por gênero;
- tabela com os dados filtrados;
- sugestões de estratégias de retenção.

---

# Filtros do Dashboard

Na lateral esquerda do dashboard, é possível filtrar os dados por:

- gênero;
- status do cliente;
- perfil de risco.

Esses filtros permitem visualizar os dados de forma mais específica e interativa.

---

# Estratégias de Retenção

O projeto sugere estratégias simples para clientes com maior risco de cancelamento, como:

- contato preventivo do gerente;
- oferta de benefícios no cartão;
- renegociação de taxas;
- campanhas de fidelização;
- acompanhamento de clientes com baixa movimentação.

---

# O projeto possui testes automatizados utilizando Pytest

Para executar: 

```bash
python -m pytest src/tests/
```

<img width="1045" height="829" alt="image" src="https://github.com/user-attachments/assets/55227b14-d2d2-48fa-bcd2-152d0f6c6392" />
