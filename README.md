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
