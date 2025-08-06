
import streamlit as st

def aplicativo_gitapps():
    st.markdown("""
    <div style='text-align: center;'>
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
    st.header("📌 Submódulo: Caracterización")
    st.info("Aquí irá el contenido de caracterización familiar o individual.")

def mostrar_plan_cuidado():
    st.header("📝 Submódulo: Plan de Cuidado")
    st.info("Aquí se diseña el plan de cuidado para la familia o el paciente.")

def mostrar_compromisos():
    st.header("🤝 Submódulo: Compromisos")
    st.info("Aquí se registran los compromisos adquiridos entre el equipo y la familia.")

def mostrar_alertas():
    st.header("🚨 Submódulo: Alertas")
    st.info("Aquí se identifican y gestionan alertas clínicas o sociales.")

def mostrar_tamizajes():
    st.header("🔍 Submódulo: Tamizajes")
    st.info("Aquí se presentan los resultados de tamizajes aplicados.")
