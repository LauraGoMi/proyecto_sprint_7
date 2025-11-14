import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Análisis de Vehículos", layout="wide")

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.header('📊 Dashboard de Análisis de Vehículos Usados')
st.write('Explora los datos de anuncios de venta de coches mediante visualizaciones interactivas')

# Crear columnas para los controles
col1, col2 = st.columns(2)

with col1:
    # Botón para construir histograma
    hist_button = st.button('Construir histograma', use_container_width=True)

with col2:
    # Botón para construir gráfico de dispersión
    scatter_button = st.button(
        'Construir gráfico de dispersión', use_container_width=True)

# Casilla de verificación
show_data = st.checkbox('Mostrar tabla de datos', value=False)

# Separador
st.divider()

# Mostrar histograma si se hace clic en el botón
if hist_button:
    st.subheader('Histograma: Distribución del Odómetro')
    st.write('Visualización de la distribución de kilometraje de los vehículos')

    # Crear histograma
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        nbins=50,
        title="Distribución del Kilometraje (Odómetro)",
        labels={'odometer': 'Kilometraje', 'count': 'Frecuencia'},
        color_discrete_sequence=['#4f46e5']
    )

    # Actualizar diseño
    fig_hist.update_layout(
        xaxis_title="Kilometraje",
        yaxis_title="Cantidad de Vehículos",
        showlegend=False
    )

    # Mostrar gráfico
    st.plotly_chart(fig_hist, use_container_width=True)

# Mostrar gráfico de dispersión si se hace clic en el botón
if scatter_button:
    st.subheader('Gráfico de Dispersión: Precio vs Kilometraje')
    st.write('Relación entre el precio y el kilometraje de los vehículos')

    # Crear gráfico de dispersión
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Relación entre Precio y Kilometraje",
        labels={'odometer': 'Kilometraje', 'price': 'Precio ($)'},
        color='condition',
        opacity=0.6,
        hover_data=['model_year', 'model']
    )

    # Actualizar diseño
    fig_scatter.update_layout(
        xaxis_title="Kilometraje",
        yaxis_title="Precio ($)"
    )

    # Mostrar gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)

# Mostrar tabla de datos si la casilla está marcada
if show_data:
    st.subheader('📋 Datos del Dataset')
    st.write(f'Total de registros: {len(car_data)}')
    st.dataframe(car_data.head(100), use_container_width=True)

    # Mostrar estadísticas básicas
    st.subheader('📈 Estadísticas Descriptivas')
    st.write(car_data.describe())

# Información adicional en el sidebar
st.sidebar.header('ℹ️ Información del Dataset')
st.sidebar.write(f'**Total de vehículos:** {len(car_data)}')
st.sidebar.write(f'**Columnas:** {len(car_data.columns)}')
st.sidebar.write('**Variables principales:**')
st.sidebar.write('- Odómetro (kilometraje)')
st.sidebar.write('- Precio')
st.sidebar.write('- Condición')
st.sidebar.write('- Año del modelo')
st.sidebar.write('- Modelo')
