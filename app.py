import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='AlergoMed | Transformación Digital', page_icon='🩺', layout='wide')
st.markdown('''<style>
.block-container{padding-top:1.5rem;padding-bottom:3rem;max-width:1400px}
[data-testid="stMetric"]{background:#f7f9fb;border:1px solid #e7ebef;padding:14px;border-radius:14px}
.hero{padding:1.2rem 1.4rem;border:1px solid #e7ebef;border-radius:18px;background:#fbfcfd;margin-bottom:1rem}
.note{font-size:.92rem;color:#667085}.step{padding:.75rem 1rem;border-left:4px solid #98a2b3;background:#f8fafc;border-radius:8px;margin:.45rem 0}
</style>''', unsafe_allow_html=True)

DATA=[
['ENE–FEB',234,15.64,75.27,22.98,1.75,84.88,15.12,28.1,59.07,'Lunes','10:00, 11:00, 3:00 p. m.','Martes','Lunes / Miércoles / Viernes'],
['FEB–MAR',261,24.59,70.61,27.70,1.69,87.60,12.40,17.5,30.37,'Lunes','10:00, 2:00 p. m., 11:00','Lunes','Lunes / Miércoles / Martes'],
['MAR–ABR',258,21.68,71.65,26.78,1.57,85.70,14.30,20.4,34.20,'Lunes','10:00, 11:00, 2:00 p. m.','Lunes','Martes / Lunes / Miércoles'],
['ABR–MAY',247,20.61,71.07,27.20,1.72,83.02,16.18,23.6,32.24,'Jueves','10:00, 11:00, 2:00 p. m.','Jueves','Miércoles / Martes / Jueves'],
['MAY–JUN',234,18.74,76.12,22.60,1.28,83.40,15.20,25.7,37.53,'Lunes','10:00 a. m., 11:00 a. m., 2:00 p. m.','Lunes','Miércoles / Jueves / Lunes'],
['JUN–JUL',269,21.35,72.74,26.06,1.19,81.26,18.63,27.7,35.37,'Miércoles','10:00 a. m., 11:00 a. m., 2:00 p. m.','Jueves','Miércoles / Lunes / Martes'],
['JUL–AGO',261,22.59,74.71,23.74,1.56,82.00,18.00,24.4,35.54,'Jueves','10:00 a. m., 11:00 a. m., 2:00 p. m.','Jueves','Jueves / Miércoles'],
['AGO–SEP',259,19.55,73.36,24.39,2.25,89.00,11.00,18.5,32.17,'Lunes','10:00 a. m., 2:00 p. m., 11:00 a. m.','Lunes','Miércoles / Jueves']]
COLS=['Periodo','Total atendidas','Promedio diario','Completadas %','Canceladas %','Ausencias %','Subsecuentes %','Nuevos %','Antelación días','Duración min','Mayor agendamiento','Horarios destacados','Mayor cancelación','Ausencias frecuentes']
df=pd.DataFrame(DATA,columns=COLS)

st.markdown('<div class="hero"><h1>🩺 AlergoMed · Transformación digital basada en datos</h1><p>Portafolio interactivo 2026 · Del dato a la decisión, del aprendizaje a la mejora continua</p></div>',unsafe_allow_html=True)
page=st.sidebar.radio('Explorar',['Inicio','Dashboard ejecutivo','Análisis temporal','Agenda y demanda','Hallazgos','Pivotes','Acceso y uso de datos','Agilidad operativa','Del dato a la decisión','Hoja de ruta','Aprendizajes'])
st.sidebar.markdown('---'); st.sidebar.caption('Datos operativos reales disponibles: enero–septiembre 2026. Las propuestas futuras se identifican explícitamente.')

if page=='Inicio':
 st.header('Una historia de transformación, no solo un dashboard')
 st.write('Esta aplicación acompaña el Portafolio AlergoMed y organiza los datos reales de la consulta, los hallazgos y los aprendizajes de los pivotes de transformación digital en una herramienta interactiva de gestión.')
 st.info('**Evolución del proyecto:** Datos → Visualización → Análisis → Decisión → Intervención → Medición → Aprendizaje → Mejora continua')
 a,b,c,d=st.columns(4); a.metric('Períodos analizados',len(df)); b.metric('Mayor volumen',f"{df['Total atendidas'].max():.0f} citas"); c.metric('Cancelaciones',f"{df['Canceladas %'].min():.1f}–{df['Canceladas %'].max():.1f}%"); d.metric('Seguimiento','>80 % subsecuentes')
 st.subheader('Propósito del producto digital')
 st.write('Pasar de observar lo ocurrido a formular mejores preguntas, identificar brechas de información y orientar decisiones pequeñas, medibles y progresivas, sin comprometer la seguridad ni la calidad clínica.')

elif page=='Dashboard ejecutivo':
 st.header('Dashboard ejecutivo')
 periodo=st.selectbox('Seleccione un período',df.Periodo,index=len(df)-1); r=df[df.Periodo==periodo].iloc[0]
 c=st.columns(5); vals=[('Total',f"{r['Total atendidas']:.0f}"),('Promedio/día',f"{r['Promedio diario']:.2f}"),('Completadas',f"{r['Completadas %']:.2f}%"),('Canceladas',f"{r['Canceladas %']:.2f}%"),('Ausencias',f"{r['Ausencias %']:.2f}%")]
 for x,(k,v) in zip(c,vals): x.metric(k,v)
 c=st.columns(4); vals=[('Subsecuentes',f"{r['Subsecuentes %']:.2f}%"),('Nuevos',f"{r['Nuevos %']:.2f}%"),('Antelación',f"{r['Antelación días']:.1f} días"),('Duración',f"{r['Duración min']:.2f} min")]
 for x,(k,v) in zip(c,vals): x.metric(k,v)
 trend=df.melt('Periodo',['Completadas %','Canceladas %','Ausencias %'],var_name='Estado',value_name='Porcentaje'); st.plotly_chart(px.line(trend,x='Periodo',y='Porcentaje',color='Estado',markers=True,title='Estado de las citas'),use_container_width=True)
 st.markdown(f"**Lectura operativa de {periodo}:** mayor agendamiento: **{r['Mayor agendamiento']}** · mayor cancelación: **{r['Mayor cancelación']}** · ausencias frecuentes: **{r['Ausencias frecuentes']}**.")

elif page=='Análisis temporal':
 st.header('Análisis temporal')
 c1,c2=st.columns(2); c1.plotly_chart(px.bar(df,x='Periodo',y='Total atendidas',title='Volumen por período'),use_container_width=True); c2.plotly_chart(px.line(df,x='Periodo',y='Promedio diario',markers=True,title='Promedio diario'),use_container_width=True)
 c1,c2=st.columns(2); c1.plotly_chart(px.line(df,x='Periodo',y='Antelación días',markers=True,title='Antelación de la cita'),use_container_width=True); c2.plotly_chart(px.line(df,x='Periodo',y='Duración min',markers=True,title='Duración promedio'),use_container_width=True)
 mix=df.melt('Periodo',['Subsecuentes %','Nuevos %'],var_name='Tipo',value_name='Porcentaje'); st.plotly_chart(px.line(mix,x='Periodo',y='Porcentaje',color='Tipo',markers=True,title='Perfil de consultas'),use_container_width=True)
 st.info('La lectura longitudinal permite observar variaciones que un valor aislado no muestra: volumen, composición de pacientes, antelación y duración cambian entre períodos y deben interpretarse en conjunto.')

elif page=='Agenda y demanda':
 st.header('Agenda y demanda')
 st.write('Los datos permiten reconocer cuándo se concentra la demanda y en qué días aparecen con mayor frecuencia cancelaciones o ausencias.')
 show=df[['Periodo','Mayor agendamiento','Horarios destacados','Mayor cancelación','Ausencias frecuentes']].copy(); st.dataframe(show,use_container_width=True,hide_index=True)
 st.success('Patrón transversal identificado en los períodos con horario disponible: **10:00–11:00 a. m. y 2:00 p. m.** aparecen recurrentemente entre los horarios de mayor agendamiento.')
 st.caption('Los horarios destacados son clasificaciones reportadas, no cantidades absolutas por franja.')

elif page=='Hallazgos':
 st.header('Hallazgos que orientan decisiones')
 st.markdown('''- **Seguimiento predominante:** las consultas subsecuentes permanecen por encima del 80 % en todos los períodos.
- **Cancelaciones como oportunidad operativa:** oscilan aproximadamente entre 22 % y 28 %, muy por encima de las ausencias.
- **Demanda concentrada:** existen días y horarios recurrentes de mayor agendamiento.
- **Antelación variable:** el tiempo de programación fluctúa y desciende hacia septiembre.
- **El dato genera nuevas preguntas:** conocer cuántas citas se cancelan llevó a preguntar cuántos espacios pueden recuperarse.''')
 st.subheader('Lectura de gestión')
 st.write('El valor del dashboard no está únicamente en describir el desempeño. Su utilidad aumenta cuando permite reconocer patrones, priorizar problemas y decidir qué información adicional debe comenzar a recopilarse.')

elif page=='Pivotes':
 st.header('Pivotes de transformación digital')
 piv=[
 ('Acceso y uso de datos','Organizar información operativa y convertirla en evidencia para decidir.','El dashboard transforma registros cotidianos en indicadores comparables y visibles.'),
 ('Innovación centrada en el cliente','Comprender necesidades y diseñar desde la experiencia del paciente.','Los indicadores dejan de verse solo como eficiencia interna y se conectan con acceso, comunicación y experiencia.'),
 ('Agilidad operativa','Experimentar, medir y ajustar preservando procesos críticos.','Se propone utilizar cancelaciones y confirmaciones como espacio de microexperimentación medible.'),
 ('Ecosistemas colaborativos','Reconocer que la transformación puede apoyarse en actores, capacidades y conexiones externas.','Amplía la mirada más allá de la clínica como sistema aislado.'),
 ('Alineamiento dinámico','Conectar datos, prioridades y objetivos organizacionales.','Los KPIs adquieren valor cuando orientan decisiones coherentes con el propósito de AlergoMed.'),
 ('Cultura y liderazgo digital','Entender que la transformación depende de personas, aprendizaje y liderazgo.','La tecnología funciona como habilitador; la adopción y el cambio requieren acompañamiento y propósito.')]
 for t,a,b in piv:
  with st.expander(t): st.markdown(f'**Aprendizaje:** {a}\n\n**Aplicación en AlergoMed:** {b}')
 st.info('La app mantiene una arquitectura modular para incorporar el último pivote de la especialización sin rehacer el proyecto.')

elif page=='Acceso y uso de datos':
 st.header('Acceso y uso de datos: del registro a la decisión')
 st.write('Este pivote profundiza en cómo los registros operativos de AlergoMed se organizan en productos de datos útiles, comparables y accesibles para la gestión, respetando la confidencialidad del paciente.')
 st.info('**Cadena de valor:** Registro operativo → Consolidación agregada → Validación → Indicadores → Interpretación → Decisión → Nueva medición')
 st.subheader('Dominios y productos de datos')
 dominios=pd.DataFrame([
  ['Pacientes','Composición de atención','Nuevos, subsecuentes, registros no clasificados','Continuidad y captación'],
  ['Citas','Estado de agenda','Completadas, canceladas, ausentes','Utilización y reprogramación'],
  ['Actividad','Volumen de consulta','Atendidos, promedio diario, duración','Planificación de capacidad'],
  ['Accesibilidad','Tiempo de agendamiento','Antelación en días','Acceso oportuno'],
  ['Demanda','Patrones de agenda','Días y horarios más solicitados','Distribución de oferta'],
  ['Calidad del dato','Completitud de clasificación','Porcentaje no completado','Confiabilidad del análisis']
 ],columns=['Dominio','Producto de datos','Variables disponibles','Uso estratégico'])
 st.dataframe(dominios,use_container_width=True,hide_index=True)
 st.subheader('Explorar los datos agregados')
 periodos=st.multiselect('Períodos para analizar',df['Periodo'].tolist(),default=df['Periodo'].tolist())
 filtrado=df[df['Periodo'].isin(periodos)].copy()
 if filtrado.empty:
  st.warning('Seleccione al menos un período para visualizar indicadores.')
 else:
  k1,k2,k3=st.columns(3)
  k1.metric('Períodos seleccionados',len(filtrado))
  k2.metric('Antelación mínima',f"{filtrado['Antelación días'].min():.1f} días")
  k3.metric('Cancelación máxima',f"{filtrado['Canceladas %'].max():.2f}%")
  g1,g2=st.columns(2)
  g1.plotly_chart(px.line(filtrado,x='Periodo',y='Antelación días',markers=True,title='Accesibilidad: antelación de agenda'),use_container_width=True)
  g2.plotly_chart(px.line(filtrado,x='Periodo',y='Canceladas %',markers=True,title='Cancelaciones por período (%)'),use_container_width=True)
  st.dataframe(filtrado[['Periodo','Total atendidas','Promedio diario','Completadas %','Canceladas %','Ausencias %','Subsecuentes %','Nuevos %','Antelación días','Duración min']],use_container_width=True,hide_index=True)
 st.subheader('Calidad del dato: clasificación de pacientes')
 incompletos={'ENE–FEB':0.0,'FEB–MAR':0.0,'MAR–ABR':0.0,'ABR–MAY':0.80,'MAY–JUN':1.40,'JUN–JUL':0.11,'JUL–AGO':0.0,'AGO–SEP':0.0}
 calidad=pd.DataFrame({'Periodo':df['Periodo'],'No completado %':df['Periodo'].map(incompletos)})
 st.plotly_chart(px.bar(calidad,x='Periodo',y='No completado %',title='Registros sin clasificación completa (%)'),use_container_width=True)
 st.caption('Los porcentajes son los reportados para la clasificación nuevo/subsecuente; no equivalen a una auditoría de todas las variables.')
 st.subheader('Acceso responsable y arquitectura de información')
 st.markdown('**Fuente:** métricas operativas de citas. **Transformación:** consolidación por ventanas móviles bimensuales. **Producto:** indicadores y visualizaciones agregadas. **Uso:** revisión clínica-administrativa y decisiones de mejora. **Publicación:** únicamente datos agregados, sin identificadores personales.')
 st.warning('Las ventanas se superponen: no se deben sumar sus volúmenes como si fueran pacientes únicos. Los rankings de horarios no permiten calcular tasas por franja sin denominadores. Las propuestas de mejora no se presentan como intervenciones ya implementadas.')
 st.subheader('Del dato a la decisión')
 st.markdown('**Dato:** cancelaciones entre 22,60 % y 27,70 %.  \n**Pregunta:** ¿cuántos espacios cancelados se pueden reasignar?  \n**Nuevo producto de datos propuesto:** registro de cancelación, antelación y reasignación.  \n**Indicador futuro:** porcentaje de espacios cancelados recuperados.  \n**Decisión:** probar y evaluar un proceso de confirmación y reasignación.')
 st.success('Aprendizaje: el acceso a los datos solo genera valor cuando los registros son comprensibles, seguros y utilizados para tomar decisiones verificables.')

elif page=='Agilidad operativa':
 st.header('Agilidad operativa: aprender rápido sin perder estabilidad')
 st.write('El caso DB Vertrieb refuerza una idea central: la agilidad no significa cambiar todo continuamente, sino equilibrar capacidad de adaptación con estabilidad en los procesos críticos.')
 st.info('**Ciclo ágil propuesto:** Datos → Patrón → Decisión → Intervención → Medición → Aprendizaje → Ajuste')
 st.subheader('Microexperimento propuesto'); st.markdown('**Problema:** las cancelaciones representan una proporción relevante de las citas.\n\n**Hipótesis:** una confirmación más cercana a la consulta podría identificar cancelaciones antes y aumentar la posibilidad de reutilizar espacios.\n\n**Intervención:** probar una confirmación reforzada durante un período definido y comparar resultados.')
 st.warning('Es una propuesta académica: no se presenta como implementada ni medida.')
 st.subheader('Brecha de datos descubierta')
 st.markdown('- **% de espacios cancelados recuperados o reasignados**\n- **Tiempo promedio para recuperar un espacio cancelado**\n- **% de cancelaciones con suficiente antelación para permitir reasignación**')
 st.caption('Estos indicadores no tienen valores actuales porque AlergoMed todavía no registra de forma estructurada esa información.')
 st.subheader('¿Qué puede cambiar y qué debe permanecer estable?'); c1,c2=st.columns(2); c1.markdown('**Procesos adaptables**\n- Agenda y horarios\n- Confirmaciones y recordatorios\n- Reasignación de espacios\n- Seguimiento de indicadores'); c2.markdown('**Procesos críticos**\n- Seguridad del paciente\n- Documentación clínica\n- Confidencialidad\n- Tratamientos y protocolos\n- Cumplimiento normativo')

elif page=='Del dato a la decisión':
 st.header('Del dato a la decisión')
 steps=[('1 · Dato real','Las cancelaciones se sitúan aproximadamente entre 22 % y 28 % según el período.'),('2 · Hallazgo','Existe una oportunidad relevante para optimizar la gestión de agenda.'),('3 · Nueva pregunta','¿Qué ocurre con el espacio después de una cancelación?'),('4 · Brecha de datos','Actualmente no se registra de forma estructurada si el espacio cancelado fue reasignado.'),('5 · Indicador propuesto','Porcentaje de espacios cancelados recuperados o reasignados.'),('6 · Intervención futura','Microexperimento de confirmación y reasignación.'),('7 · Aprendizaje','Medir nuevamente y decidir si mantener, ajustar o descartar la intervención.')]
 for a,b in steps: st.markdown(f'<div class="step"><b>{a}</b><br>{b}</div>',unsafe_allow_html=True)
 st.success('Este recorrido muestra la madurez del proyecto: el dato no termina en un gráfico; genera preguntas, decisiones y nuevas necesidades de medición.')

elif page=='Hoja de ruta':
 st.header('Hoja de ruta')
 st.markdown('''**Ahora**  
Datos reales enero–septiembre 2026 + dashboard + análisis temporal + hallazgos + pivotes + propuesta de agilidad operativa.

**Siguiente fase**  
Profundizar los pivotes pendientes y mantener alineados README, dashboard y app.

**Madurez de datos**  
Comenzar a registrar, cuando sea factible, los datos necesarios para medir recuperación de espacios cancelados y otras preguntas que surjan de la gestión.

**Cierre**  
Integrar el proyecto en una sola narrativa: **dato → información → decisión → experimento → medición → aprendizaje → mejora continua**.''')
 st.success('La app está preparada para crecer sin reconstruir el proyecto desde cero.')

else:
 st.header('Aprendizajes')
 st.write('La construcción del portafolio permitió comprender que la transformación digital no comienza con la tecnología, sino con la capacidad de formular mejores preguntas, escuchar a las personas, organizar los datos y convertirlos en decisiones con propósito.')
 st.markdown('''**Sobre AlergoMed:** la clínica genera información valiosa de manera cotidiana, pero su valor aumenta cuando se estructura, compara y vincula con objetivos concretos.

**Sobre los datos:** disponer de información no equivale a gestionarla estratégicamente; también es importante reconocer qué datos faltan.

**Sobre la agilidad:** mejorar no implica cambiar todo. En salud, la experimentación debe convivir con estabilidad, seguridad, confidencialidad y calidad clínica.

**Sobre el liderazgo digital:** el dashboard es una herramienta; la transformación ocurre cuando las personas utilizan la evidencia para aprender y actuar.''')
 st.info('**Visión final:** que el dashboard y la app sean una herramienta de gestión y transformación digital de AlergoMed, con una historia clara desde el dato hasta la decisión y la mejora continua.')
