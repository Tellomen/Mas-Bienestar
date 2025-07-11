import streamlit as st
import streamlit.components.v1 as components  # Para incrustar Genially

# Configuración de página
st.set_page_config(page_title="Inducción Más Bienestar", layout="wide")

# URL directa a la imagen desde GitHub (ajusta si es necesario)
background_url = "https://drive.google.com/uc?export=view&id=16GSPB6SYsuXgPyMDyq_eGjPOjTXgAjlP"

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .welcome-box {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 25px;
        border-radius: 12px;
        text-align: left;
        color: white;
        margin-top: 30px;
        margin-bottom: 30px;
    }}
    </style>
""", unsafe_allow_html=True)

# Mensaje de bienvenida
st.markdown("""
<div class='welcome-box'>
    <h1>¡Bienvenido(a) a la Inducción del Programa Más Bienestar!</h1>
    <p style='font-size:18px;'>Conoce el entorno, tus funciones y aprende a usar el aplicativo institucional según tu rol profesional.</p>
</div>
""", unsafe_allow_html=True)

# Iniciar recorrido
if st.button("🚀 Iniciar recorrido"):
    st.session_state["modulo"] = "Bienvenida y Entorno"

# Menú lateral
st.sidebar.title("Menú de Inducción")
modulo = st.sidebar.selectbox("Selecciona un módulo:", [
    "Bienvenida y Entorno", "Gestores", "Psicólogos", "Enfermeros(as)", "Evaluación"
])

# Diccionario por perfil
modulos_perfil = {
    "Gestores": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Toma de Medidas", "Tamizaje Apgar"],
    "Psicólogos": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Enfermeros(as)": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"]
}

# Funciones de módulo
def modulo_entorno():
    st.markdown("""
    <div class='welcome-box'>
        <h2>🌍 Bienvenida y Descripción del Entorno</h2>
        <p><b>Bienvenido(a) al proceso de inducción del programa Más Bienestar.</b></p>
        <p>Es una estrategia integral de atención en salud familiar y comunitaria.</p>
        <ul>
            <li>Trabajo interdisciplinario.</li>
            <li>Articulación con redes institucionales y comunitarias.</li>
            <li>Aplicativo de gestión creado por la Secretaría Distrital de Salud.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

def modulo_perfil(nombre, modulos):
    st.markdown(f"<div class='welcome-box'><h2>🧑‍💼 Inducción para {nombre}</h2></div>", unsafe_allow_html=True)
    subtitulo = st.selectbox("Selecciona un módulo a revisar:", modulos)
    st.markdown(f"""
    <div class='welcome-box'>
        <h3>📘 Módulo: {subtitulo}</h3>
        <ul>
            <li><b>¿Qué es?</b> Descripción del propósito.</li>
            <li><b>¿Cómo diligenciarlo?</b> Paso 1, 2 y 3.</li>
            <li><b>Errores comunes</b> y recomendaciones.</li>
        </ul>
        <p>✅ Al finalizar, puedes realizar un quiz de refuerzo.</p>
    </div>
    """, unsafe_allow_html=True)

def modulo_evaluacion():
    st.markdown("""
    <div class='welcome-box'>
        <h2>🧠 Evaluación - Juego Interactivo en Genially</h2>
        <p>Explora el siguiente juego para reforzar tus conocimientos sobre el programa Más Bienestar.</p>
    </div>
    """, unsafe_allow_html=True)

    # Incrustar Genially con iframe
    components.html(
        """
        <iframe title="ESCAPE GAME APLICATIVO" frameborder="0"
            width="100%" height="600"
            src="https://view.genial.ly/687159b48ee96fa859ffd0a4"
            type="text/html" allowscriptaccess="always" allowfullscreen="true"
            scrolling="yes" allownetworking="all"
            style="border:none;"></iframe>
        """,
        height=600
    )

# Lógica principal
if modulo == "Bienvenida y Entorno":
    modulo_entorno()
elif modulo == "Evaluación":
    modulo_evaluacion()
elif modulo in modulos_perfil:
    modulo_perfil(modulo, modulos_perfil[modulo])
