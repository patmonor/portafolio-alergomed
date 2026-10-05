import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='AlergoMed | Transformación Digital', page_icon='🩺', layout='wide')

st.markdown('''
<style>
.block-container {padding-top: 2rem; padding-bottom: 3rem;}
[data-testid="stMetric"] {background: #f7f9fb; border: 1px solid #e7ebef; padding: 14px; border-radius: 14px;}
.small-note {color:#667085; font-size:0.92rem;}
</style>
''', unsafe_allow_html=True)

DATA = [
    ['ENE–FEB',234,15.64,75.27,22.98,1.75,84.88,15.12,28.1,59.07,'Lunes','Martes','Lunes / Miércoles / Viernes'],
    ['FEB–MAR',261,24.59,70.61,27.70,1.69,87.60,12.40,17.5,30.37,'Lunes','Lunes','Lunes / Miércoles / Martes'],
    ['MAR–ABR',258,21.68,71.65,26.78,1.57,85.70,14.30,20.4,34.20,'Lunes','Lunes','Martes / Lunes / Miércoles'],
    ['ABR–MAY',247,20.61,71.07,27.20,1.72,83.02,16.18,23.6,32.24,'Jueves','Jueves','Miércoles / Martes / Jueves'],
    ['MAY–JUN',234,18.74,76.12,22.60,1.28,83.40,15.20,25.7,37.53,'Lunes','Lunes','Miércoles / Jueves / Lunes'],
    ['JUN–JUL',269,21.35,72.74,26.06,1.19,81.26,18.63,27.7,35.37,'Miércoles','Jueves','Miércoles / Lunes / Martes'],
    ['JUL–AGO',261,22.59,74.71,23.74,1.56,82.00,18.00,24.4,35.54,'Jueves','Jueves','Jueves / Miércoles'],
    ['AGO–SEP',259,19.55,73.36,24.39,2.25,89.00,11.00,18.5,32.17,'Lunes','Lunes','Miércoles / Jueves'],
]
COLS = ['Periodo','Total atendidas','Promedio diario','Completadas %','Canceladas %','Ausencias %','Subsecuentes %','Nuevos %','Antelación días','Duración min','Mayor agendamiento','Mayor cancelación','Ausencias frecuentes']
df = pd.DataFrame(DATA, columns=COLS)

st.title('🩺 AlergoMed · Transformación Digital')
st.caption('Del dato a la decisión, del aprendizaje a la mejora continua · Portafolio académico 2026')

page = st.sidebar.radio('Explorar', ['Inicio','Dashboard','Hallazgos','Pivotes','Agilidad operativa','Hoja de ruta'])
st.sidebar.markdown('---')
st.sidebar.caption('Datos operativos reales disponibles: enero–septiembre 2026. Los indicadores futuros se identifican explícitamente como propuestas.')

if page == 'Inicio':
    st.header('Una herramienta de gestión, no solo un conjunto de gráficos')
    st.write('Esta aplicación acompaña el Portafolio AlergoMed y convierte los datos operativos de la consulta en una experiencia interactiva para visualizar, analizar y apoyar decisiones de mejora.')
    st.info('**Ciclo del proyecto:** Datos → Visualización → Análisis → Decisión → Intervención → Medición → Mejora continua')
    a,b,c = st.columns(3)
    a.metric('Períodos analizados', len(df))
    b.metric('Mayor volumen', f"{int(df['Total atendidas'].max())} citas")
    c.metric('Subsecuentes', '≥ 80 % en todos los períodos')
    st.subheader('Propósito')
    st.write('Integrar el dashboard, los hallazgos y los pivotes de transformación digital en un producto que pueda evolucionar conforme se incorporen nuevos datos y aprendizajes.')

elif page == 'Dashboard':
    st.header('Dashboard operativo')
    periodo = st.selectbox('Seleccione un período', df['Periodo'].tolist(), index=len(df)-1)
    r = df[df['Periodo']==periodo].iloc[0]
    cols = st.columns(5)
    cols[0].metric('Total atendidas', int(r['Total atendidas']))
    cols[1].metric('Promedio diario', f"{r['Promedio diario']:.2f}")
    cols[2].metric('Completadas', f"{r['Completadas %']:.2f}%")
    cols[3].metric('Canceladas', f"{r['Canceladas %']:.2f}%")
    cols[4].metric('Ausencias', f"{r['Ausencias %']:.2f}%")
    cols2 = st.columns(4)
    cols2[0].metric('Subsecuentes', f"{r['Subsecuentes %']:.2f}%")
    cols2[1].metric('Nuevos', f"{r['Nuevos %']:.2f}%")
    cols2[2].metric('Antelación', f"{r['Antelación días']:.1f} días")
    cols2[3].metric('Duración', f"{r['Duración min']:.2f} min")

    trend = df.melt(id_vars='Periodo', value_vars=['Completadas %','Canceladas %','Ausencias %'], var_name='Estado', value_name='Porcentaje')
    fig = px.line(trend, x='Periodo', y='Porcentaje', color='Estado', markers=True, title='Evolución del estado de las citas')
    st.plotly_chart(fig, use_container_width=True)
    c1,c2 = st.columns(2)
    c1.plotly_chart(px.line(df, x='Periodo', y='Antelación días', markers=True, title='Antelación de la cita'), use_container_width=True)
    c2.plotly_chart(px.line(df, x='Periodo', y='Duración min', markers=True, title='Duración promedio'), use_container_width=True)
    st.caption(f"En {periodo}: mayor agendamiento = {r['Mayor agendamiento']}; mayor cancelación = {r['Mayor cancelación']}; ausencias frecuentes = {r['Ausencias frecuentes']}.")

elif page == 'Hallazgos':
    st.header('Hallazgos que orientan decisiones')
    st.markdown('''
- Las consultas subsecuentes se mantienen por encima del **80 %**, mostrando una población con seguimiento frecuente.
- Los horarios de mayor agendamiento se concentran recurrentemente alrededor de **10:00–11:00 a. m. y 2:00 p. m.**
- Las cancelaciones se sitúan aproximadamente entre **22 % y 28 %**, constituyendo una oportunidad operativa relevante.
- Las ausencias son bajas en comparación con las cancelaciones, aunque requieren seguimiento.
- La antelación de las citas fluctúa y muestra una reducción hacia septiembre.
''')
    st.plotly_chart(px.bar(df, x='Periodo', y='Total atendidas', title='Volumen atendido por período'), use_container_width=True)

elif page == 'Pivotes':
    st.header('Pivotes de transformación digital')
    pivots = [
        ('Acceso y uso de datos','Convertir información operativa dispersa en evidencia útil para decidir.'),
        ('Innovación centrada en el cliente','Diseñar mejoras desde las necesidades y experiencia del paciente.'),
        ('Agilidad operativa','Experimentar a pequeña escala, medir y ajustar sin comprometer procesos críticos.'),
        ('Ecosistemas colaborativos','Reconocer el valor de conexiones, actores y capacidades externas.'),
        ('Alineamiento dinámico','Conectar indicadores, prioridades y decisiones con los objetivos de la organización.'),
        ('Cultura y liderazgo digital','Impulsar transformación mediante personas, aprendizaje y liderazgo, no solo tecnología.'),
    ]
    for title, desc in pivots:
        with st.expander(title): st.write(desc)
    st.info('La arquitectura de la app permite incorporar el último pivote y actualizar esta sección sin reconstruir el dashboard.')

elif page == 'Agilidad operativa':
    st.header('Agilidad operativa')
    st.write('El dashboard puede apoyar un ciclo de mejora ágil: **Datos → Patrón → Decisión → Intervención → Medición → Aprendizaje → Ajuste**.')
    st.subheader('Microexperimento propuesto')
    st.write('**Problema:** las cancelaciones representan una proporción relevante de las citas programadas.')
    st.write('**Hipótesis:** una confirmación más cercana a la consulta podría identificar cancelaciones antes y aumentar la posibilidad de reutilizar espacios liberados.')
    st.write('**Intervención propuesta:** probar una estrategia de confirmación reforzada durante un período definido y comparar los resultados.')
    st.warning('Esta intervención es una propuesta académica. No se presenta como implementada ni medida.')
    st.subheader('Indicadores futuros propuestos')
    st.markdown('''
- **% de espacios cancelados recuperados o reasignados.**
- **Tiempo promedio para recuperar un espacio cancelado.**
- **% de cancelaciones con suficiente antelación para permitir reasignación.**
''')
    st.caption('Actualmente no se dispone de los datos necesarios para calcular estos indicadores; se incluyen como una brecha de datos identificada y una oportunidad futura de medición.')

else:
    st.header('Hoja de ruta')
    st.markdown('''
**Versión actual**  
Dashboard con datos reales enero–septiembre 2026 + hallazgos + pivotes + propuesta de agilidad operativa.

**Próxima actualización**  
Incorporar el último pivote de la especialización manteniendo la misma estructura modular.

**Cierre del proyecto**  
Integrar portafolio, dashboard y app en una sola narrativa de transformación digital: **dato → decisión → intervención → aprendizaje → mejora continua**.
''')
    st.success('La app está preparada para crecer sin rehacer el proyecto desde cero.')
