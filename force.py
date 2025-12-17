import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de la página
st.set_page_config(page_title="Ley de Newton", page_icon="🍎")

st.title("🍎 Laboratorio Virtual: Segunda Ley de Newton")
st.markdown("Interactúa con los parámetros para ver cómo cambia la aceleración según $F = m \cdot a$.")

# 2. Crear las columnas para los controles (Sliders)
col1, col2 = st.columns(2)

with col1:
    masa = st.slider("Masa (kg)", min_value=0.1, max_value=20.0, value=5.0, step=0.1)

with col2:
    fuerza = st.slider("Fuerza (N)", min_value=0.0, max_value=100.0, value=20.0, step=1.0)

# 3. Cálculos
aceleracion = fuerza / masa

# 4. Mostrar resultados numéricos destacados
st.divider() # Línea divisoria
c1, c2, c3 = st.columns(3)
c1.metric("Fuerza Aplicada", f"{fuerza} N")
c2.metric("Masa del Objeto", f"{masa} kg")
c3.metric("Aceleración Resultante", f"{aceleracion:.2f} m/s²", delta_color="normal")
st.divider()

# 5. Generar la gráfica
fig, ax = plt.subplots(figsize=(10, 5))

# Datos matemáticos
f_range = np.linspace(0, 100, 100)
a_range = f_range / masa

# Dibujar
ax.plot(a_range, f_range, label=f'Masa = {masa} kg (Pendiente)', color='#1f77b4', linewidth=2)
ax.scatter([aceleracion], [fuerza], color='#d62728', s=200, zorder=5, label='Estado Actual')

# Estética
ax.set_xlabel('Aceleración ($m/s^2$)')
ax.set_ylabel('Fuerza (N)')
ax.set_title('Gráfica Fuerza vs. Aceleración')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Mostrar la gráfica en la web
st.pyplot(fig)
