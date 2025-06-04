
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
historical_df = pd.read_csv("historical_sales.csv", parse_dates=['date'])
prediction_df = pd.read_csv("future_sales_predictions.csv", parse_dates=['date'])

st.set_page_config(page_title="Tablero de Ventas", layout="wide")
st.title("📈 Tablero de Predicción de Ventas")

st.markdown("Este tablero muestra las ventas históricas simuladas y la predicción para los próximos 30 días.")

# Gráfico de ventas históricas
st.subheader("Ventas Históricas")
fig_hist = px.line(historical_df, x='date', y='sales', title='Histórico de Ventas')
st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de predicción futura
st.subheader("Predicción para los Próximos 30 Días")
fig_pred = px.line(prediction_df, x='date', y='predicted_sales', title='Predicción de Ventas Futuras')
st.plotly_chart(fig_pred, use_container_width=True)

# Tablas
with st.expander("Ver tabla de datos históricos"):
    st.dataframe(historical_df.tail(30))

with st.expander("Ver tabla de predicción futura"):
    st.dataframe(prediction_df)

st.markdown("---")
st.markdown("Tablero generado automáticamente con datos simulados para fines demostrativos.")
