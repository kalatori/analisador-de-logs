import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

PASTA = Path(__file__).parent
CAMINHO_BANCO = PASTA / "logs_teste.db"

st.title("Analisador de Logs")

if not CAMINHO_BANCO.exists():
    st.error(f"Não encontrei o banco em: {CAMINHO_BANCO}")
    st.stop()

conexao = sqlite3.connect(CAMINHO_BANCO)

eventos = pd.read_sql_query("SELECT * FROM eventos", conexao)

falhas = pd.read_sql_query(
    """
    SELECT ip, COUNT(*) AS total
    FROM eventos
    WHERE evento = 'LOGIN_FALHOU'
    GROUP BY ip
    ORDER BY total DESC
    """,
    conexao,
)

conexao.close()

st.subheader("Falhas de login por IP")
st.bar_chart(falhas.set_index("ip"))

limite = st.slider("Alertar a partir de quantas falhas?", 1, 10, 3)

suspeitos = falhas[falhas["total"] >= limite]
if len(suspeitos) > 0:
    for _, linha in suspeitos.iterrows():
        st.error(f"ALERTA: o IP {linha['ip']} falhou {linha['total']} vezes!")
else:
    st.success("Nenhum IP suspeito.")

st.subheader("Todos os eventos")
st.dataframe(eventos)