import streamlit as st

def aplicativo_gitapps():
    st.markdown("""
    
    <div class='welcome-box'>
        <h2>🧩 APLICATIVO GITAPPS</h2>
        <p>Selecciona uno de los submódulos para continuar.</p>
    </div>

    """, unsafe_allow_html=True)

    submodulo = st.selectbox("Selecciona un submódulo:", [
        "Caracterización",
        "Plan de Cuidado",
        "Compromisos",
        "Alertas",
        "Tamizajes"
    ])

    if submodulo == "Caracterización":
        mostrar_caracterizacion()
    elif submodulo == "Plan de Cuidado":
        mostrar_plan_cuidado()
    elif submodulo == "Compromisos":
        mostrar_compromisos()
    elif submodulo == "Alertas":
        mostrar_alertas()
    elif submodulo == "Tamizajes":
        mostrar_tamizajes()

def mostrar_caracterizacion():
    st.markdown("""
    <div class='welcome-box'>
        <h3>📌 Submódulo: Caracterización</h3>
        <ul>
            <li><b>¿Qué es?</b> Descripción del propósito.</li>
            <li><b>¿Cómo diligenciarlo?</b> Paso 1, 2 y 3.</li>
            <li><b>Errores comunes</b> y recomendaciones.</li>
        </ul>
        <p>✅ Al finalizar, puedes realizar un quiz de refuerzo.</p>
    </div>
    """, unsafe_allow_html=True)

def mostrar_plan_cuidado():
    st.markdown("""
    <div class='welcome-box'>
        <h3>📝 Submódulo: Plan de Cuidado</h3>
        <p>Aquí se diseña el plan de cuidado para la familia o el paciente.</p>
    </div>
    """, unsafe_allow_html=True)

def mostrar_compromisos():
    st.markdown("""
    <div class='welcome-box'>
        <h3>🤝 Submódulo: Compromisos</h3>
        <p>Aquí se registran los compromisos adquiridos entre el equipo y la familia.</p>
    </div>
    """, unsafe_allow_html=True)

def mostrar_alertas():
    st.markdown("""
    <div class='welcome-box'>
        <h3>🚨 Submódulo: Alertas</h3>
        <p>Aquí se identifican y gestionan alertas clínicas o sociales.</p>
    </div>
    """, unsafe_allow_html=True)

def mostrar_tamizajes():
    st.markdown("""
    <div class='welcome-box'>
        <h3>🔍 Submódulo: Tamizajes</h3>
        <p>Aquí se presentan los resultados de tamizajes aplicados.</p>
    </div>
    """, unsafe_allow_html=True)
