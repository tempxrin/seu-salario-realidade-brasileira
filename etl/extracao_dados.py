# Rendimento mensal habitual de todos os trabalhos para pessoas de 14 anos ou mais de idade 
# (apenas para pessoas que receberam em dinheiro, produtos ou mercadorias em qualquer trabalho)	

# ================================================================================================================================================ #
#                                                                                                                                                  # 
#                                                           IMPORTAÇÃO DAS BIBLIOTECAS                                                             #
#                                                                                                                                                  #
# ================================================================================================================================================ # 

import basedosdados as bd
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from typing import Dict, List, Any
import numpy as np
from urllib.parse import quote_plus
import os
import yaml
import traceback
import logging

from yaml.loader import SafeLoader
from pathlib import Path

# ================================================================================================================================================ #
#                                                                                                                                                  # 
#                                                           EXTRACT                                                                                #
#                                                                                                                                                  #
# ================================================================================================================================================ # 

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
    
billing_id = config['big_query']['projeto']

query = """
  SELECT
    dados.ano AS ano,
    dados.trimestre AS trimestre,
    dados.id_uf AS id_uf,
    dados.sigla_uf AS sigla_uf,
    dados.id_domicilio AS id_domicilio,
    dados.id_pessoa AS id_pessoa,
    dados.VD4019 AS renda,
    dados.V2007 AS sexo,
    dados.V2010 AS raca,
    dados.V2009 AS idade,
    dados.V3009A AS escolaridade
FROM `basedosdados.br_ibge_pnadc.microdados` AS dados
WHERE (dados.ano = 2024 AND dados.VD4019 > 0 AND dados.V2010 <> '9' AND dados.V3009A <> 'None')
"""

pnadc_vd4019 = bd.read_sql(query=query, billing_project_id=billing_id)

# ================================================================================================================================================ #
#                                                                                                                                                  # 
#                                                           TRANSFORM                                                                              #
#                                                                                                                                                  #
# ================================================================================================================================================ # 

escolaridade = pd.DataFrame(
    {
        'escolaridade': ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'],
        'tipo_escolaridade': ['Pré-escola',
                              'Alfabetizado',
                              'Alfabetizado',
                              'Fundamental',
                              'Fundamental',
                              'Fundamental',
                              'Fundamental',
                              'Médio',
                              'Médio',
                              'Médio',
                              'Superior',
                              'Pós-graduação',
                              'Mestrado',
                              'Doutorado']
    }
)

raca = pd.DataFrame(
    {
        'raca': ['1', '2', '3', '4', '5'],
        'tipo_raca': ['Branca', 'Preta', 'Amarela', 'Parda', 'Indígena']
    }
)

sexo = pd.DataFrame(
    {
        'sexo': ['1', '2'],
        'tipo_sexo': ['Homem', 'Mulher']
    }
)

pnadc_vd4019_merge = pnadc_vd4019.merge(sexo, on='sexo', how='left') \
    .merge(raca, on='raca', how='left') \
    .merge(escolaridade, on='escolaridade', how='left')
    
pnadc_vd4019_merge = pnadc_vd4019_merge.sort_values(['id_pessoa', 'trimestre', 'escolaridade'])

pnadc_vd4019_merge = pnadc_vd4019_merge.groupby('id_pessoa').tail(1).reset_index(drop=True)

renda_por_pessoa = pnadc_vd4019_merge.groupby('id_pessoa').agg({
    'renda': 'sum',
    'escolaridade': 'first',
    'tipo_escolaridade': 'first',
    'raca': 'first',
    'tipo_raca': 'first',
    'sexo': 'first',
    'tipo_sexo': 'first',
    'sigla_uf': 'first'
}).reset_index()


# ================================================================================================================================================ #
#                                                                                                                                                  # 
#                                                           LOAD                                                                                   #
#                                                                                                                                                  #
# ================================================================================================================================================ # 

renda_por_pessoa.to_parquet('renda_por_pessoa.parquet', engine='pyarrow', index=False)
