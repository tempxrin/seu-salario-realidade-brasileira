import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Seu Salário na Realidade Brasileira",
    page_icon="🇧🇷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>
    
     /* Header - Fundo */
    header[data-testid="stHeader"] {
        background-color: #ffffff !important;
        border-bottom: 1px solid #dee2e6 !important;
    }
    
    /* Container do header */
    div[data-testid="stHeader"] {
        background-color: #ffffff !important;
    }
    
    /* Barra superior do Streamlit */
    .stApp > header {
        background-color: #ffffff !important;
        border-bottom: 1px solid #dee2e6 !important;
    }
    
    /* Elementos dentro do header */
    header[data-testid="stHeader"] * {
        background-color: transparent !important;
    }
    
    /* Menu hambúrguer e outros elementos do header */
    header[data-testid="stHeader"] button {
        color: #000000 !important;
    }
    
    /* Forçar todo o container superior */
    .stApp > div:first-child {
        background-color: #ffffff !important;
    }
    
    /* Caso específico para o header fixo */
    div[data-testid="stHeader"] > div {
        background-color: #ffffff !important;
    }
    
    /* Toolbar do Streamlit */
    .stToolbar {
        background-color: #ffffff !important;
    }
    
    /* Container principal da aplicação */
    .stApp {
        background-color: #ffffff !important;
    }
    
    /* Caso haja um elemento de navegação superior */
    nav {
        background-color: #ffffff !important;
    }
    
    /* Forçar qualquer elemento de cabeçalho */
    .css-1d391kg, .css-1lcbmhc {
        background-color: #ffffff !important;
    }
    
    .main * {
        color: #000000 !important;
    }
    
    .block-container * {
        color: #000000 !important;
    }
    
    /* Headers principais */
    .main-header {
        font-size: 2.8rem;
        font-weight: 600;
        text-align: center;
        color: #000000 !important;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-size: 1.1rem;
        text-align: center;
        color: #333333 !important;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    .result-text {
        font-size: 1.8rem;
        font-weight: 600;
        text-align: center;
        color: #000000 !important;
        margin: 2rem 0;
        line-height: 1.4;
    }
    
    .filters-note {
        background-color: #f8f9fa;
        padding: 0.8rem 1.2rem;
        border-radius: 8px;
        font-size: 0.9rem;
        color: #000000 !important;
        margin: 1rem 0;
        border-left: 4px solid #3498db;
    }
    
    .filters-note strong {
        color: #000000 !important;
        font-weight: 600;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 0.5rem;
        border-left: 4px solid #3498db;
    }
    
    .metric-card h3 {
        color: #000000 !important;
        font-size: 1rem;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    .metric-card h2 {
        color: #000000 !important;
        font-size: 1.8rem;
        margin: 0;
        font-weight: 600;
    }
    
    /* Elementos do Streamlit */
    .stSelectbox > div > div {
        background-color: white;
        border: 1px solid #ddd;
        color: #000000 !important;
    }
    
    .stSelectbox label {
        color: #000000 !important;
        font-weight: 500;
    }
    
    .stSelectbox div[data-baseweb="select"] > div {
        color: #000000 !important;
    }
    
    .stSelectbox div[data-baseweb="select"] span {
        color: #000000 !important;
    }
    
    .stNumberInput label {
        color: #000000 !important;
        font-weight: 500;
    }
    
    .stNumberInput input {
        color: #000000 !important;
    }
    
    .stMarkdown p {
        color: #000000 !important;
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
        color: #000000 !important;
    }
    
    .stMarkdown strong {
        color: #000000 !important;
    }
    
    .stMarkdown em {
        color: #000000 !important;
    }
    
    .stMarkdown ul, .stMarkdown ol {
        color: #000000 !important;
    }
    
    .stMarkdown li {
        color: #000000 !important;
    }
    
    .stMetric label {
        color: #000000 !important;
        font-size: 0.9rem;
    }
    
    .stMetric [data-testid="metric-value"] {
        color: #000000 !important;
        font-size: 1.5rem;
    }
    
    .stMetric [data-testid="metric-delta"] {
        color: #000000 !important;
    }
    
    .stButton button {
        color: #ffffff !important;
        background-color: #3498db !important;
        border: none !important;
        font-weight: 500 !important;
    }
    
    .stButton button:hover {
        background-color: #2980b9 !important;
    }
    
    .stInfo {
        color: #000000 !important;
    }
    
    .stError {
        color: #000000 !important;
    }
    
    .stSuccess {
        color: #000000 !important;
    }
    
    .stWarning {
        color: #000000 !important;
    }
    
    /* SIDEBAR - Seletores mais específicos e modernos */
    
    /* Fundo da sidebar */
    section[data-testid="stSidebar"] {
        background-color: #2c3e50 !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background-color: #2c3e50 !important;
    }
    
    /* Labels e textos da sidebar em branco */
    section[data-testid="stSidebar"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    /* Títulos dos selectbox especificamente */
    section[data-testid="stSidebar"] .stSelectbox label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox > label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    /* Força todos os labels de formulário */
    section[data-testid="stSidebar"] div[data-testid*="stSelectbox"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    section[data-testid="stSidebar"] div[data-testid*="stNumberInput"] label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    /* Força qualquer texto de label na sidebar */
    section[data-testid="stSidebar"] [class*="label"] {
        color: #ffffff !important;
    }
    
    /* Markdown da sidebar */
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3,
    section[data-testid="stSidebar"] .stMarkdown h4 {
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] .stMarkdown p {
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] .stMarkdown strong {
        color: #ffffff !important;
    }
    
    /* Força qualquer texto na sidebar que não seja de input */
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* Exceto os inputs que devem ser pretos */
    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] select,
    section[data-testid="stSidebar"] div[data-baseweb="select"] span,
    section[data-testid="stSidebar"] div[data-baseweb="select"] div {
        color: #000000 !important;
    }
    
    /* Inputs da sidebar */
    section[data-testid="stSidebar"] input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ddd !important;
    }
    
    /* Number input específico da sidebar */
    section[data-testid="stSidebar"] .stNumberInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ddd !important;
        font-weight: 500 !important;
    }
    
    /* Label do number input */
    section[data-testid="stSidebar"] .stNumberInput label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }
    
    /* Botões de incremento/decremento */
    section[data-testid="stSidebar"] .stNumberInput button {
        background-color: #f8f9fa !important;
        color: #000000 !important;
        border: 1px solid #ddd !important;
    }
    
    section[data-testid="stSidebar"] .stNumberInput button:hover {
        background-color: #e9ecef !important;
    }
    
    /* Sinais dos botões +/- em preto */
    section[data-testid="stSidebar"] .stNumberInput button svg {
        fill: #000000 !important;
        color: #000000 !important;
    }
    
    /* Selectbox na sidebar */
    section[data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ddd !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox span {
        color: #000000 !important;
    }
    
    /* REMOÇÃO TOTAL DO ÍCONE DO SELECTBOX - Abordagem mais agressiva */
    
    /* Esconder TODOS os SVGs dentro de selectbox */
    section[data-testid="stSidebar"] .stSelectbox * svg {
        visibility: hidden !important;
        display: none !important;
        width: 0 !important;
        height: 0 !important;
        opacity: 0 !important;
    }
    
    /* Esconder elementos com role button que podem conter o ícone */
    section[data-testid="stSidebar"] .stSelectbox *[role="button"] *::after {
        display: none !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox *[role="button"] *::before {
        display: none !important;
    }
    
    /* Forçar remoção de qualquer ícone ou seta */
    section[data-testid="stSidebar"] .stSelectbox *[data-baseweb*="select"] *::after {
        content: none !important;
        display: none !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox *[data-baseweb*="select"] *::before {
        content: none !important;
        display: none !important;
    }
    
    /* Remover qualquer elemento filho que possa ser o ícone */
    section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div > div:last-child {
        display: none !important;
    }
    
    /* Ajustar padding para compensar espaço do ícone removido */
    section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        padding-right: 0 !important;
    }
    
    /* Força largura específica para remover espaço extra */
    section[data-testid="stSidebar"] .stSelectbox > div > div {
        width: 100% !important;
        box-sizing: border-box !important;
    }
    
    /* Esconder overflow que pode mostrar ícones */
    section[data-testid="stSidebar"] .stSelectbox {
        overflow: hidden !important;
    }
    
    section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] {
        overflow: hidden !important;
    }
    
    /* Botão na sidebar */
    section[data-testid="stSidebar"] .stButton button {
        background-color: #3498db !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: 500 !important;
    }
    
    section[data-testid="stSidebar"] .stButton button:hover {
        background-color: #2980b9 !important;
    }
    
    /* Principais containers */
    .main { 
        background-color: #ffffff !important; 
        color: #000000 !important;
    }
    
    .block-container { 
        background-color: #ffffff !important; 
        color: #000000 !important;
    }
    
    /* Texto geral */
    p, div, span, label, input, select, textarea {
        color: #000000 !important;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
    }
    
    /* Links */
    a {
        color: #3498db !important;
    }
    
    /* Inputs */
    input, select, textarea {
        background-color: #ffffff !important;
        border: 1px solid #ddd !important;
        color: #000000 !important;
    }
    
    /* DROPDOWNS GLOBAIS - Quando abre qualquer selectbox */
    
    /* Container do dropdown */
    div[data-baseweb="popover"] {
        background-color: #ffffff !important;
        border: 1px solid #ddd !important;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    }
    
    /* Lista de opções */
    ul[role="listbox"] {
        background-color: #ffffff !important;
        border: none !important;
    }
    
    /* Cada opção individual */
    li[role="option"] {
        background-color: #ffffff !important;
        color: #000000 !important;
        padding: 8px 12px !important;
        border: none !important;
    }
    
    /* Hover nas opções */
    li[role="option"]:hover {
        background-color: #e6f3ff !important;
        color: #000000 !important;
    }
    
    /* Opção selecionada */
    li[role="option"][aria-selected="true"] {
        background-color: #3498db !important;
        color: #ffffff !important;
    }
    
    /* Texto dentro das opções */
    li[role="option"] div {
        color: inherit !important;
        background: transparent !important;
    }
    
    /* Forçar texto das opções */
    div[data-baseweb="popover"] * {
        color: #000000 !important;
    }
    
    li[role="option"]:hover * {
        color: #000000 !important;
    }
    
    li[role="option"][aria-selected="true"] * {
        color: #ffffff !important;
    }
    
    /* Plotly charts - garantir que os títulos sejam pretos */
    .js-plotly-plot .plotly .main-svg .gtitle {
        fill: #000000 !important;
    }
    
    .js-plotly-plot .plotly .main-svg .xtitle {
        fill: #000000 !important;
    }
    
    .js-plotly-plot .plotly .main-svg .ytitle {
        fill: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Extrai os dados
@st.cache_data
def load_data():
    try:
        df = pd.read_parquet('renda_por_pessoa.parquet')
        return df
    except FileNotFoundError:
        st.error("Arquivo nao encontrado")
        st.stop()

# Função para calcular percentil
def calcular_percentil(renda_usuario, df_filtrado):
    if len(df_filtrado) == 0:
        return 0
    pessoas_com_renda_menor = len(df_filtrado[df_filtrado['renda'] < renda_usuario])
    total_pessoas = len(df_filtrado)
    percentil = (pessoas_com_renda_menor / total_pessoas) * 100
    return min(percentil, 99.0) 

# Cria o gráfico de barras percentual 
def criar_grafico_percentil(percentil, renda_usuario):
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=[percentil],
        y=[''],
        orientation='h',
        marker_color='#3498db',
        showlegend=False,
        textposition='outside',
        textfont=dict(color='#000000', size=18, family="Arial Black"),
        hoverinfo='skip'
    ))
    
    fig.update_layout(
        yaxis_title='',
        height=120,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=200, r=200, t=20, b=50),
        xaxis=dict(
            range=[0, 110], 
            ticksuffix='%',
            tickfont=dict(color='#000000'),
            title=dict(font=dict(color='#000000'))
        ),
        yaxis=dict(
            showticklabels=False,
            tickfont=dict(color='#000000'),
            title=dict(font=dict(color='#000000'))
        ),
        font=dict(color='#000000'),
        dragmode=False
    )
    
    return fig

# Cria gráficos da "Comparação por categorias"
def criar_grafico_comparativo_moderno(df):
    fig = make_subplots(
        rows=4, cols=1,
        subplot_titles=('Renda Média por Sexo', 'Renda Média por Escolaridade', 'Renda Média por UF', 'Renda Média por Raça'),
        specs=[[{"type": "bar"}],
               [{"type": "bar"}],
               [{"type": "bar"}],
               [{"type": "bar"}]],
        vertical_spacing=0.05,
        row_heights=[0.08, 0.45, 0.90, 0.20] 
    )
    
    # Por sexo
    renda_sexo = df.groupby('tipo_sexo')['renda'].mean().sort_values(ascending=True)
    fig.add_trace(go.Bar(
        y=renda_sexo.index, 
        x=renda_sexo.values, 
        orientation='h',
        marker_color='#3498db',
        showlegend=False,
        text=[f'R$ {val:,.0f}' for val in renda_sexo.values],
        textposition='outside',
        textfont=dict(color='#000000', size=12),
        hoverinfo='skip'
    ), row=1, col=1)
    
    renda_escolaridade = df.groupby('tipo_escolaridade')['renda'].mean().sort_values(ascending=True)
    
    fig.add_trace(go.Bar(
        y=renda_escolaridade.index, 
        x=renda_escolaridade.values, 
        orientation='h',
        marker_color='#3498db',
        showlegend=False,
        text=[f'R$ {val:,.0f}' for val in renda_escolaridade.values],
        textposition='outside',
        textfont=dict(color='#000000', size=12),
        hoverinfo='skip'
        ), row=2, col=1)
    
    # Por UF
    if 'sigla_uf' in df.columns:
        renda_uf = df.groupby('sigla_uf')['renda'].mean().sort_values(ascending=True)
        fig.add_trace(go.Bar(
            y=renda_uf.index,
            x=renda_uf.values,
            orientation='h',
            marker_color='#3498db',
            showlegend=False,
            text=[f'R$ {val:,.0f}' for val in renda_uf.values],
            textposition='outside',
            textfont=dict(color='#000000', size=12),
            hoverinfo='skip'
        ), row=3, col=1)
    
    # Por raça
    renda_raca = df.groupby('tipo_raca')['renda'].mean().sort_values(ascending=True)
    fig.add_trace(go.Bar(
        y=renda_raca.index, 
        x=renda_raca.values, 
        orientation='h',
        marker_color='#3498db',
        showlegend=False,
        text=[f'R$ {val:,.0f}' for val in renda_raca.values],
        textposition='outside',
        textfont=dict(color='#000000', size=12),
        hoverinfo='skip'
    ), row=4, col=1)
    
    fig.update_layout(
        height=3000, 
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=20, r=20, t=80, b=20),
        font=dict(color='#000000'),
        width=100,
        yaxis3=dict(
            tickfont=dict(size=12), 
            automargin=True
        ),
        dragmode=False
        )
    
    fig.update_xaxes(
        tickfont=dict(color='#000000'), 
        title=dict(font=dict(color='#000000', size=16)),
        showgrid=False,
        showline=False,
        zeroline=False
    )
    fig.update_yaxes(
        tickfont=dict(color='#000000'), 
        title=dict(font=dict(color='#000000', size=16)),
        showgrid=False,
        showline=False,
        zeroline=False
    )
    
    # Atualizar títulos dos gráficos
    for annotation in fig['layout']['annotations']:
        annotation['font'] = dict(color='#000000', size=16)
    
    return fig

# Função para gerar texto descritivo
def gerar_texto_resultado(percentil, sexo, raca, escolaridade, uf, renda_usuario):
    partes = []
    
    if sexo != 'Todos':
        if sexo == 'Homem':
            partes.append("homens")
        else:
            partes.append("mulheres")
    
    if raca != 'Todos':
        if raca == 'Branca':
            partes.append("brancos")
        elif raca == 'Preta':
            partes.append("pretos")
        elif raca == 'Parda':
            partes.append("pardos")
        else:
            partes.append(raca.lower())
    
    if escolaridade != 'Todos':
        partes.append(f"com {escolaridade.lower()}")
    
    if uf != 'Todos':
        partes.append(f"do estado {uf}")
    
    if partes:
        descricao = ", ".join(partes)
        return f"Você ganha mais do que {percentil:.1f}% dos brasileiros {descricao}"
    else:
        return f"Você ganha mais do que {percentil:.1f}% dos brasileiros"

# Carregar dados
df = load_data()

# Cabeçalho
st.markdown('<h1 class="main-header">Seu salário diante da realidade brasileira</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Descubra como sua renda se compara com o restante da população</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("### Configure sua análise")

# Input da renda
renda_usuario = st.sidebar.number_input(
    "Qual é sua renda mensal?",
    min_value=0,
    max_value=100000,
    value=3000,
    step=100,
    format="%d"
)

st.sidebar.markdown("### Filtros")

# Filtros ordenados
sexo_valores = ['Todos'] + sorted(df['tipo_sexo'].unique())
sexo_selecionado = st.sidebar.selectbox("Sexo", sexo_valores)

raca_valores = ['Todos'] + sorted([x for x in df['tipo_raca'].unique() if pd.notna(x)])
raca_selecionada = st.sidebar.selectbox("Raça/Cor", raca_valores)

# Escolaridade com ordem hierárquica
escolaridade_ordem = [
    'NA', 'Pré-escola', 'Classe de alfabetização - CA', 'Alfabetização de jovens e adultos',
    'Antigo primário (elementar)', 'Antigo ginásio (médio 1º ciclo)', 
    'Regular do ensino fundamental ou do 1º grau', 'Educação de jovens e adultos (EJA) ou supletivo do 1º grau',
    'Antigo científico, clássico, etc. (médio 2º ciclo)', 'Regular do ensino médio ou do 2º grau',
    'Educação de jovens e adultos (EJA) ou supletivo do 2º grau', 'Superior - graduação',
    'Especialização de nível superior', 'Mestrado', 'Doutorado'
]

escolaridade_opcoes = ['Todos']
for nivel in escolaridade_ordem:
    if nivel in df['tipo_escolaridade'].values:
        escolaridade_opcoes.append(nivel)

escolaridade_selecionada = st.sidebar.selectbox("Escolaridade", escolaridade_opcoes)

if 'sigla_uf' in df.columns:
    uf_valores = ['Todos'] + sorted([x for x in df['sigla_uf'].unique() if pd.notna(x)])
    uf_selecionada = st.sidebar.selectbox("Estado", uf_valores)
else:
    uf_selecionada = 'Todos'

# Botão de análise
if st.sidebar.button("Calcular", type="primary", use_container_width=True):
    # Aplicar filtros
    df_filtrado = df.copy()
    
    if sexo_selecionado != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['tipo_sexo'] == sexo_selecionado]
    
    if raca_selecionada != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['tipo_raca'] == raca_selecionada]
    
    if escolaridade_selecionada != 'Todos':
        df_filtrado = df_filtrado[df_filtrado['tipo_escolaridade'] == escolaridade_selecionada]
    
    if uf_selecionada != 'Todos' and 'sigla_uf' in df.columns:
        df_filtrado = df_filtrado[df_filtrado['sigla_uf'] == uf_selecionada]
    
    if len(df_filtrado) == 0:
        st.error("Nenhum dado encontrado com os filtros selecionados. Tente outras combinações.")
        st.stop()
    
    # Nota sobre filtros aplicados
    if any(x != 'Todos' for x in [sexo_selecionado, raca_selecionada, escolaridade_selecionada, uf_selecionada]):
        filtros_ativos = []
        if sexo_selecionado != 'Todos': filtros_ativos.append(f"Sexo: {sexo_selecionado}")
        if raca_selecionada != 'Todos': filtros_ativos.append(f"Raça: {raca_selecionada}")
        if escolaridade_selecionada != 'Todos': filtros_ativos.append(f"Escolaridade: {escolaridade_selecionada}")
        if uf_selecionada != 'Todos': filtros_ativos.append(f"Estado: {uf_selecionada}")
        
        st.markdown(f"""
        <div class="filters-note">
            <strong>Filtros aplicados:</strong> {' | '.join(filtros_ativos)} <strong>
        </div>
        """, unsafe_allow_html=True)
    
    # Calcular percentil
    percentil = calcular_percentil(renda_usuario, df_filtrado)
    
    # Texto principal do resultado
    texto_resultado = gerar_texto_resultado(percentil, sexo_selecionado, raca_selecionada, escolaridade_selecionada, uf_selecionada, renda_usuario)
    
    st.markdown(f'<div class="result-text">{texto_resultado}</div>', unsafe_allow_html=True)
    
    # Gráfico de barra de percentil
    fig_percentil = criar_grafico_percentil(percentil, renda_usuario)
    st.plotly_chart(fig_percentil, use_container_width=True)
    
    # Card com métricas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Renda Média</h3>
            <h2>R$ {df_filtrado['renda'].mean():,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        diferenca_media = ((renda_usuario / df_filtrado['renda'].mean()) - 1) * 100
        sinal = "+" if diferenca_media > 0 else ""
        st.markdown(f"""
        <div class="metric-card">
            <h3>Diferença da Média</h3>
            <h2>{sinal}{diferenca_media:.1f}%</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>Desvio Padrão</h3>
            <h2>R$ {df_filtrado['renda'].std():,.0f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("## Comparação por categorias")
    
    fig_comp = criar_grafico_comparativo_moderno(df)
    st.plotly_chart(fig_comp, use_container_width=True)

else:
    # Tela inicial (antes de calcular)
    st.info("Configure sua renda e filtros na barra lateral e clique em 'Calcular'")
    
    # Estatísticas gerais
    st.markdown("---")
    st.markdown("## Dados gerais da população brasileira")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Renda Média Nacional", f"R$ {df['renda'].mean():,.0f}")
    
    with col2:
        st.metric("10% mais rico ganha acima de", f"R$ {df['renda'].quantile(0.90):,.0f}")

    with col3:
        st.metric("1% mais rico ganha acima de", f"R$ {df['renda'].quantile(0.99):,.0f}")

# Metodologia
st.markdown("---")
st.markdown("## Metodologia")

st.markdown("**Fonte dos dados:** Os dados utilizados nesta calculadora são provenientes da Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua) do IBGE, referentes ao ano de 2024.")

st.markdown("**Variável analisada:** Utilizamos a variável VD4019, que representa o rendimento mensal habitual de todos os trabalhos para pessoas de 14 anos ou mais de idade (considerando apenas aqueles que receberam em dinheiro, produtos ou mercadorias).")

st.markdown("**Processamento:** Os dados foram processados utilizando Python com as bibliotecas pandas e basedosdados para acesso ao BigQuery. Para cada pessoa, consideramos apenas o último registro disponível no ano de 2024, garantindo que não haja duplicatas.")

# Rodapé
st.markdown("---")

st.markdown("""
<style>
    .footer {
        position: relative;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f8f9fa;
        color: #000000;
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 1px solid #dee2e6;
    }
    
    .footer-content {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    
    .footer-text {
        font-size: 1rem;
        color: #000000 !important;
        margin: 0;
        font-weight: 500;
    }
    
    .footer-buttons {
        display: flex;
        gap: 0.5rem;
        align-items: center;
    }
    
    .footer-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.5rem 1rem;
        background-color: #ffffff;
        border: 2px solid #3498db;
        color: #3498db !important;
        text-decoration: none !important;
        border-radius: 25px;
        font-weight: 500;
        transition: all 0.3s ease;
        min-width: 120px;
    }
    
    .footer-btn:hover {
        background-color: #3498db;
        color: #ffffff !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(52, 152, 219, 0.3);
        text-decoration: none !important;
    }
    
    .footer-btn svg {
        margin-right: 0.5rem;
        width: 20px;
        height: 20px;
    }
    
    .linkedin-btn {
        border-color: #0077b5;
        color: #0077b5 !important;
    }
    
    .linkedin-btn:hover {
        background-color: #0077b5;
        color: #ffffff !important;
    }
    
    .portfolio-btn {
        border-color: #2c3e50;
        color: #2c3e50 !important;
    }
    
    .portfolio-btn:hover {
        background-color: #2c3e50;
        color: #ffffff !important;
    }
    
    @media (max-width: 768px) {
        .footer-content {
            flex-direction: column;
            gap: 1rem;
        }
        
        .footer-buttons {
            flex-direction: row;
            gap: 0.5rem;
        }
        
        .footer-btn {
            min-width: 100px;
            font-size: 0.9rem;
        }
    }
</style>

<div class="footer">
    <div class="footer-content">
        <p class="footer-text">Desenvolvido por João Daniel Temporin</p>
        <div class="footer-buttons">
            <a href="https://www.linkedin.com/in/joao-temporin/" target="_blank" class="footer-btn linkedin-btn">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
                </svg>
                LinkedIn
            </a>
            <a href="https://tempxrin.github.io" target="_blank" class="footer-btn portfolio-btn">
                <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/>
                </svg>
                Portfólio
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)