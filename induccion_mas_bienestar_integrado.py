import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from io import BytesIO
from PIL import Image

# ------------------------- CONFIGURACIÓN DE PÁGINA --------------------------
st.set_page_config(page_title="Inducción Más Bienestar", layout="wide")

# URL del Google Sheet exportado como CSV
CSV_URL = "https://docs.google.com/spreadsheets/d/1sHq2UATtF5q_IINt82C0X_ah_m-ac5Et/export?format=csv"

# ------------------------- CARGAR BASE DE TALENTO HUMANO ---------------------
@st.cache_data(ttl=60)
def cargar_talento_humano():
    df = pd.read_csv(CSV_URL)
    df.columns = df.columns.str.strip().str.lower()
    return df

talento_humano = cargar_talento_humano()

# ------------------------- IMAGEN DE FONDO ----------------------------------
background_url = "https://raw.githubusercontent.com/Tellomen/Mas-Bienestar/e1210f110835eda506a064861da58aa4d1357e84/Toma%20Territorial.png"

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

# ------------------------- LOGIN --------------------------------------------
def login():
    st.markdown("""
    <style>
    .custom-success {
        background-color: #000000;
        color: white;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        margin-top: 20px;
        font-size: 18px;
        box-shadow: 0 0 10px rgba(0,0,0,0.4);
    }
    </style>
    <div class='welcome-box'><h2>🔐 Inicio de Sesión</h2></div>
    """, unsafe_allow_html=True)

    usuario = st.text_input("Usuario (Documento)")
    password = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        user_row = talento_humano[talento_humano['usuario'].astype(str) == usuario]
        if not user_row.empty:
            estado = user_row['estado'].values[0]
            nombre = user_row['nombre'].values[0]
            perfil_unificado = user_row['perfil unificado'].values[0]

            if perfil_unificado.upper() == "ADMINISTRADOR":
                acceso_correcto = (password == usuario)
            else:
                acceso_correcto = (password == "riesgo2020+")

            if acceso_correcto:
                if estado.upper() == "ACTIVO":
                    st.session_state["autenticado"] = True
                    st.session_state["usuario"] = usuario
                    st.session_state["nombre"] = nombre
                    st.session_state["perfil"] = perfil_unificado
                    st.markdown(f"""
                        <div class='custom-success'>
                            ¡Bienvenido {nombre}!
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"Tu estado es '{estado}'. Contacta a Talento Humano.")
            else:
                st.error("Contraseña incorrecta.")
        else:
            st.error("Usuario no encontrado en la base de Talento Humano.")
            
# ------------------------- MÓDULOS POR PERFIL --------------------------------
modulos_perfil = {
    "Gestores": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Toma de Medidas", "Tamizaje Apgar"],
    "Psicólogos": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Enfermeros(as)": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Ambiental": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Terapeutas": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Odontologia": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Nutricion": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Etnicos": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Embera": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Auxiliar del cuidado": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Medicos": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"]
}

modulos_vsp = [
    "CRONICOS", "OTROS CASOS PRIORIZADOS"
]

# ------------------------- FUNCIONES DE MÓDULO ------------------------------
def modulo_entorno():
    st.markdown("""
    <div class='welcome-box'>
        <h2>🌍 Bienvenida y Descripción del Entorno</h2>
        <p><b>Bienvenido(a) al proceso de inducción del programa Más Bienestar.</b></p>
    </div>
    """, unsafe_allow_html=True)

    # Video
    st.markdown("""
    <div style='display: flex; justify-content: center; margin-top: 10px; margin-bottom: 20px;'>
        <video width="1257" height="732" controls>
            <source src="https://raw.githubusercontent.com/Tellomen/Mas-Bienestar/main/Mas%20Bienestar.mp4" type="video/mp4">
            Tu navegador no soporta la etiqueta de video.
        </video>
    </div>
    """, unsafe_allow_html=True)

    # Plantilla Genially embebida centrada
    st.markdown("""
    <div style='display: flex; justify-content: center; margin-top: 20px;'>
        <iframe title="Modulo de Bienvenida"
            src="https://view.genial.ly/68913d5fcb9d97c53e1192d6"
            width="1257"
            height="732"
            style="border: none; box-shadow: 0 0 10px rgba(0,0,0,0.2);'>
        </iframe>
    </div>
    """, unsafe_allow_html=True)

    # Texto adicional debajo del video
    st.markdown("""
    <div class='welcome-box'>
        <p>Es una estrategia integral de atención en salud familiar y comunitaria.</p>
        <ul>
            <li>Trabajo interdisciplinario.</li>
            <li>Articulación con redes institucionales y comunitarias.</li>
            <li>Aplicativo de gestión creado por la Secretaría Distrital de Salud.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # Avatar
    st.markdown("""
    <div style='display: flex; justify-content: center; margin-top: 20px;'>
        <img src='https://media.tenor.com/lPZZzG9NPuoAAAAi/avatar-speaking.gif' width='180'>
    </div>
    """, unsafe_allow_html=True)
    
def modulo_perfil(nombre, modulos):
    st.markdown(f"<div class='welcome-box'><h2>🧑‍💼 Inducción para {nombre}</h2></div>", unsafe_allow_html=True)
    subtitulo = st.selectbox("Selecciona un módulo a revisar:", modulos)

    if subtitulo == "Eventos VSP":
        subtitulo_vsp = st.selectbox("Selecciona un sub-módulo de Eventos VSP:", modulos_vsp)
        st.markdown(f"<div class='welcome-box'><h3>📘 Submódulo: {subtitulo_vsp}</h3></div>", unsafe_allow_html=True)
    else:
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
    components.html("""
        <iframe title="ESCAPE GAME APLICATIVO" frameborder="0"
            width="100%" height="600"
            src="https://view.genial.ly/687159b48ee96fa859ffd0a4"
            allowfullscreen="true"></iframe>
    """, height=600)

# ------------------------- CONTROL DE SESIÓN --------------------------------
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    login()
else:
    perfil = st.session_state["perfil"]
    st.sidebar.title(f"👤 {st.session_state['nombre']} ({perfil})")

    if st.sidebar.button("Cerrar Sesión"):
        st.session_state["autenticado"] = False
        st.experimental_rerun()

    opciones = ["Bienvenida y Entorno", "Evaluación"]
    if perfil.upper() == "ADMINISTRADOR":
        opciones += list(modulos_perfil.keys())
    elif perfil in modulos_perfil:
        opciones.append(perfil)

    modulo = st.sidebar.selectbox("Selecciona un módulo:", opciones)

    if modulo == "Bienvenida y Entorno":
        modulo_entorno()
    elif modulo in modulos_perfil:
        modulo_perfil(modulo, modulos_perfil[modulo])
    elif modulo == "Evaluación":
        modulo_evaluacion()
