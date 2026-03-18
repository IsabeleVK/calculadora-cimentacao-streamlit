import streamlit as st
from controller import calcular_volume
import pandas as pd

st.set_page_config(
    page_title="Calculadora de Cimentação",
    layout="wide"
)

st.title("Calculadora de Cimentação de Poço")

st.sidebar.header("Configurações")

tipo_calculo = st.sidebar.selectbox(
    "Tipo de cálculo",
    ["Simples", "Avançado", "Personalizado"]
)

st.sidebar.info(
    "Escolha o tipo de cálculo e preencha os dados."
)

st.subheader("Entrada de dados")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "Área do poço (m²)",
        min_value=0.0,
        step=0.1
    )

with col2:
    altura = st.number_input(
        "Altura do poço (m)",
        min_value=0.0,
        step=0.1
    )

dados = {
    "area": area,
    "altura": altura
}

if tipo_calculo == "Personalizado":
    coef = st.number_input(
        "Coeficiente de ajuste",
        min_value=0.0,
        step=0.1
    )
    dados["coef"] = coef

st.divider()

if st.button("Calcular Volume"):

    if area == 0 or altura == 0:
        st.warning("Preencha área e altura.")
    else:

        resultado = calcular_volume(tipo_calculo, dados)

        st.subheader("Resultado")

        col1, col2, col3 = st.columns(3)

        col1.metric("Área", f"{area} m²")
        col2.metric("Altura", f"{altura} m")
        col3.metric("Volume", f"{resultado:.2f} m³")

        st.success(f"Volume calculado: **{resultado:.2f} m³**")