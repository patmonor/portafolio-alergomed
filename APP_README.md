# App AlergoMed

Aplicación interactiva del Portafolio AlergoMed 2026.

## Archivos
- `app.py`: aplicación principal.
- `requirements.txt`: dependencias para desplegar en Streamlit Community Cloud.

## Ejecutar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Publicación
Suba `app.py` y `requirements.txt` a la raíz del repositorio de GitHub. Luego cree una app en Streamlit Community Cloud seleccionando el repositorio y `app.py` como archivo principal.

Los datos incluidos corresponden a los períodos reales disponibles de enero–septiembre 2026. Los indicadores de recuperación/reasignación de cancelaciones se muestran únicamente como propuestas futuras porque todavía no se dispone de esos datos.


## Profundización del pivote: Acceso y uso de datos

Este avance continúa el portafolio de transformación digital de **AlergoMed**, sin sustituir los pivotes anteriores. Su propósito es mostrar cómo los datos reales de citas dejan de ser registros aislados y se convierten en información confiable para tomar decisiones de gestión centradas en el paciente.

### Organización y trazabilidad de la información

Los datos proceden de métricas operativas de citas y se consolidaron en **ocho ventanas móviles bimensuales, de enero a septiembre de 2026**. Cada fila representa un período y las columnas describen volumen, estado de las citas, composición de pacientes, antelación y duración. Los períodos se superponen y **no deben sumarse como cohortes independientes**.

**Registro operativo → Consolidación agregada → Verificación → Indicadores → Análisis → Decisión → Nueva medición.**

### Dominios y productos de datos

| Dominio | Producto de datos | Variables | Decisión que apoya |
|---|---|---|---|
| Pacientes | Composición de atención | Nuevos, subsecuentes y no completados | Continuidad y captación |
| Citas | Estado de agenda | Completadas, canceladas y ausentes | Confirmación y reprogramación |
| Actividad asistencial | Capacidad de atención | Atendidos, promedio diario y duración | Organización de agenda |
| Accesibilidad | Tiempo de agendamiento | Antelación promedio | Disponibilidad de citas |
| Demanda | Patrones de agenda | Días y horarios destacados | Adaptar la oferta |
| Calidad del dato | Completitud de clasificación | Porcentaje no completado | Mejorar confiabilidad |

### Evidencia real y uso estratégico

| Evidencia observada | Interpretación prudente | Decisión o pregunta de gestión |
|---|---|---|
| Cancelaciones entre 22,60 % y 27,70 % | Las cancelaciones son más frecuentes que las ausencias | ¿Qué proporción de espacios cancelados puede reasignarse? |
| Antelación entre 17,5 y 28,1 días | La accesibilidad medida por anticipación varía entre períodos | ¿Conviene revisar la distribución de horarios? |
| Más de 80 % de consultas subsecuentes en cada período | Predomina la atención de seguimiento | ¿Cómo facilitar los próximos controles? |
| 10:00 a. m. fue el horario más solicitado en los ocho períodos | Preferencia recurrente en los rankings reportados | ¿La disponibilidad responde a la demanda? |
| Registros no completados de 0 % a 1,40 % | La calidad de la clasificación también debe vigilarse | ¿Cómo mejorar la consistencia del registro? |

### Acceso, calidad y protección de los datos

El acceso a datos útiles exige definiciones consistentes, registros completos y responsabilidades claras. Para el portafolio y la aplicación Streamlit utilizamos **datos agregados sin información identificable de pacientes**. La publicación de estos resultados no implica publicar expedientes clínicos ni habilitar acceso a datos personales.

La arquitectura de trabajo del prototipo es: **fuente operativa de citas → consolidación agregada → tabla de indicadores → visualización en Streamlit → interpretación gerencial**. Este flujo describe el prototipo analítico y no supone integraciones automáticas que no se hayan verificado.

### Brecha de datos y propuesta de mejora

Los indicadores actuales muestran cuánto se cancela, pero no si un espacio cancelado pudo recuperarse. Propongo incorporar en una etapa futura un producto de datos de **reasignación de espacios**, que registre de forma segura el momento de cancelación y si la cita fue ocupada nuevamente. Con ello se podría medir el **porcentaje de espacios cancelados recuperados**, siempre que se disponga del numerador y denominador correspondientes.

### Reflexión personal

Este pivote me permitió comprender que disponer de información no equivale a utilizarla estratégicamente. En AlergoMed ya generamos datos valiosos durante la atención cotidiana; el cambio cultural aparece cuando los organizamos, verificamos su calidad, los interpretamos y los usamos para decidir qué mejorar. La transformación digital no comienza con un gráfico: comienza con preguntas relevantes y con el compromiso de convertir los datos en acciones medibles.

> **AlergoMed: del dato a la decisión, y de la decisión a la mejora continua.**



## Profundización del pivote: Ecosistemas colaborativos

Este avance **continúa el mismo portafolio de AlergoMed**, sin reemplazar los pivotes anteriores. El objetivo es comprender cómo la colaboración entre personas y organizaciones puede transformar datos en decisiones coordinadas, siempre centradas en la atención del paciente.

### El dashboard como *Boundary Object*

El dashboard funciona como **objeto frontera**: un punto de referencia compartido que puede ser interpretado por personal clínico, administración y dirección desde sus distintas responsabilidades. No exige que todos tengan los mismos conocimientos, pero sí permite dialogar sobre indicadores comunes y priorizar acciones.

### Actores y oportunidades de colaboración

| Actor | Perspectiva | Datos relevantes | Oportunidad de colaboración |
|---|---|---|---|
| Equipo clínico | Calidad y continuidad asistencial | Pacientes subsecuentes, duración y antelación | Coordinar seguimiento |
| Administración | Agenda y comunicación | Cancelaciones, ausencias y demanda | Mejorar confirmación y reprogramación |
| Dirección | Prioridades y recursos | Indicadores longitudinales | Evaluar decisiones e intervenciones |
| Pacientes y familias | Necesidades y experiencia | Horarios y antelación; voz del paciente futura | Diseñar servicios más convenientes |
| Hospital y especialistas | Continuidad entre servicios | Referencias y contrarreferencias futuras | Explorar coordinación asistencial |
| Soporte tecnológico | Seguridad y calidad del dato | Completitud y trazabilidad | Facilitar visualización y acceso responsable |

**Nota:** estas son oportunidades de colaboración. No afirmo que existan integraciones tecnológicas, acuerdos de intercambio de datos o mediciones que aún no hemos comprobado.

### Evidencia real que puede orientar la colaboración

| Hallazgo de AlergoMed | Lectura colaborativa | Decisión posible |
|---|---|---|
| Cancelaciones entre 22,60 % y 27,70 % | Administración y dirección pueden revisar conjuntamente el proceso | Probar reprogramación anticipada |
| 10:00 a. m. es el horario más solicitado en los ocho períodos | El equipo puede contrastar demanda y disponibilidad | Revisar distribución de horarios |
| Antelación entre 17,5 y 28,1 días | Clínica y administración pueden analizar accesibilidad | Ajustar capacidad según necesidades |
| Pacientes subsecuentes entre 81,26 % y 89 % | La continuidad requiere coordinación clínica-administrativa | Fortalecer programación de controles |

Los datos corresponden a **ventanas móviles bimensuales superpuestas** y no deben sumarse como períodos independientes.

### Indicadores colaborativos propuestos para una etapa futura

| Indicador | Forma de medición propuesta | Valor esperado |
|---|---|---|
| Tiempo de respuesta entre áreas | Horas entre solicitud y respuesta | Mayor agilidad |
| Espacios cancelados recuperados | Citas reasignadas / citas canceladas × 100 | Mejor utilización de agenda |
| Referencias con seguimiento documentado | Referencias cerradas / referencias registradas × 100 | Continuidad asistencial |
| Acciones de mejora conjuntas | Número de acciones implementadas y evaluadas | Aprendizaje organizacional |
| Experiencia de coordinación | Encuesta breve al paciente y equipo | Identificar fricciones |

**Estos indicadores aún no cuentan con valores medidos**. Se presentan como una hoja de ruta para fortalecer el ecosistema de AlergoMed.

### Microproyecto colaborativo propuesto

**Problema:** cancelaciones recurrentes de citas.  
**Actores:** administración, equipo clínico y dirección.  
**Hipótesis:** un proceso coordinado de confirmación y reprogramación anticipada podría facilitar la recuperación de espacios.  
**Acción futura:** implementar un piloto con funciones y responsabilidades definidas.  
**Evaluación:** medir porcentaje de espacios recuperados y tiempo de reasignación.  
**Protección:** compartir solo la información necesaria y mantener la confidencialidad del paciente.

### Impacto en cultura y liderazgo digital

La colaboración no consiste simplemente en conectar sistemas. Implica crear un lenguaje común, distribuir responsabilidades, escuchar perspectivas diferentes y utilizar información confiable para decidir. En AlergoMed, el dashboard puede servir como herramienta de diálogo entre áreas y como base para evaluar acciones compartidas.

### Reflexión personal

Este pivote me ayuda a comprender que los datos no generan todo su valor cuando permanecen dentro de un área. Su potencial aumenta cuando se interpretan de manera conjunta y se convierten en acuerdos de mejora. La transformación digital de AlergoMed requiere tanto herramientas como relaciones de colaboración, confianza, aprendizaje y respeto por la confidencialidad clínica.

> **AlergoMed: del dato a la decisión, y de la decisión a la mejora continua, mediante una colaboración centrada en el paciente.**

