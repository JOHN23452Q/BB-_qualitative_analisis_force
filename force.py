import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de la página
st.set_page_config(page_title="Ley de Newton", page_icon="🍎", layout="centered")



# 2. Crear las columnas para los controles (Sliders)
# CAMBIO AQUÍ: Ahora los inputs son Masa y Aceleración
col1, col2 = st.columns(2)

with col1:
    masa = st.slider("Masa (kg)", min_value=0.1, max_value=120.0, value=5.0, step=0.1)

with col2:
    # Se cambia el slider de Fuerza por el de Aceleración
    aceleracion = st.slider("Aceleración (m/s²)", min_value=0.0, max_value=20.0, value=4.0, step=0.1)

# 3. Cálculos
# CAMBIO AQUÍ: Se despeja F en lugar de a
fuerza = masa * aceleracion

# 4. Mostrar resultados numéricos destacados
st.divider() # Línea divisoria
c1, c2, c3 = st.columns(3)
# El orden visual sigue siendo el mismo, pero los valores se actualizan según el nuevo cálculo
c1.metric("Fuerza Resultante (Output)", f"{fuerza:.1f} N", delta_color="normal")
c2.metric("Masa (Input)", f"{masa:.1f} kg")
c3.metric("Aceleración (Input)", f"{aceleracion:.1f} m/s²")
st.divider()

# 5. Generar la gráfica
fig, ax = plt.subplots(figsize=(10, 5))

# Datos matemáticos para la línea de tendencia
# CAMBIO AQUÍ: Generamos el rango del eje X (Aceleración) y calculamos el Y (Fuerza)
# Usamos un rango un poco mayor al del slider (hasta 25) para que la gráfica respire
a_linea = np.linspace(0, 25, 100)
f_linea = masa * a_linea

# Dibujar
# La línea representa la masa constante (la pendiente)
ax.plot(a_linea, f_linea, label=f'Pendiente (Masa) = {masa} kg', color='#1f77b4', linewidth=2)
# El punto rojo es el estado actual seleccionado por los sliders (X=aceleración, Y=fuerza)
ax.scatter([aceleracion], [fuerza], color='#d62728', s=200, zorder=5, label='Tu selección actual')

# Estética
ax.set_xlabel('Aceleración ($m/s^2$) - [Eje X]')
ax.set_ylabel('Fuerza (N) - [Eje Y]')
ax.set_title('Gráfica Fuerza vs. Aceleración')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# CAMBIO AQUÍ: Ajustar límites fijos para acomodar los nuevos rangos máximos
# (Max Fuerza posible = 20kg * 20m/s² = 400N)
ax.set_xlim(0, 25)
ax.set_ylim(0, 2500)

# Mostrar la gráfica en la web
st.pyplot(fig)








