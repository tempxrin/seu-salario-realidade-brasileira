# Seu Salário diante da Realidade Brasileira

Este projeto tem como objetivo comparar a sua **renda mensal** com a da população brasileira, utilizando dados oficiais da **PNAD Contínua** (IBGE).  
A aplicação foi desenvolvida em **Python** utilizando **Streamlit** e **Streamlit Cloud**, permitindo uma visualização **interativa** da posição da sua renda em relação a diferentes grupos da população segmentados por **sexo**, **escolaridade**, **raça** e **unidade da federação (UF)**.

🔗 **Acesse o site**:  
[comparesuarenda.streamlit.app](https://comparesuarenda.streamlit.app/)

---

## Sobre os dados

- **Fonte**: Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD-C) — IBGE
- **Variável principal**: `VD4019` — Rendimento mensal habitual de todos os trabalhos para pessoas de 14 anos ou mais
- **Variáveis de segmentação**: sexo, grau de instrução, cor/raça e unidade da federação (UF)

---

## Funcionalidades

- Inserção da sua renda mensal
- Filtros por sexo, escolaridade, raça e estado
- Visualização percentual da sua posição de renda
- Gráficos comparativos entre categorias

---

## Bibliotecas

- streamlit
- basedosdados
- pandas
- plotly
- yaml
- logging

---

## Como executar localmente

### Com Docker

#### Construa a Imagem

```bash
docker build -t salario-br .
```

#### Execute a Imagem

```bash
docker run -p 8501:8501 salario-br
```

### Manualmente

#### 1. Clone o repositório

```bash
git clone https://github.com/tempxrin/seu-salario-realidade-brasileira.git
cd seu-salario-realidade-brasileira
```

#### 2. Crie e ative um ambiente virtual

##### Linux ou Mac

```bash
python -m venv venv
source venv/bin/activate
```

###### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Execute a aplicação

```bash
streamlit run app.py
```
