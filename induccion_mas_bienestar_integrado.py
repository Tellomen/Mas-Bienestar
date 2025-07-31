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
    st.markdown("<div class='welcome-box'><h2>🔐 Inicio de Sesión</h2></div>", unsafe_allow_html=True)
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
                    st.success(f"¡Bienvenido {nombre}!")
                else:
                    st.error(f"Tu estado es '{estado}'. Contacta a Talento Humano.")
            else:
                st.error("Contraseña incorrecta.")
        else:
            st.error("Usuario no encontrado en la base de Talento Humano.")

# ------------------------- MÓDULOS POR PERFIL --------------------------------
modulos_perfil = {
    "Gestores": ["Módulo 1", "Módulo 2"],
    "Psicólogos": ["Módulo 1", "Módulo 2"],
    "Enfermeros(as)": ["Módulo 1", "Módulo 2"],
    "Ambiental": ["Módulo 1", "Módulo 2"],
    "Terapeutas": ["Módulo 1", "Módulo 2"],
    "Odontologia": ["Módulo 1", "Módulo 2"],
    "Nutricion": ["Módulo 1", "Módulo 2"],
    "Etnicos": ["Módulo 1", "Módulo 2"],
    "Embera": ["Módulo 1", "Módulo 2"],
    "Auxiliar del cuidado": ["Módulo 1", "Módulo 2"],
    "Medicos": ["Módulo 1", "Módulo 2"]
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
        <p>Es una estrategia integral de atención en salud familiar y comunitaria.</p>
        <ul>
            <li>Trabajo interdisciplinario.</li>
            <li>Articulación con redes institucionales y comunitarias.</li>
            <li>Aplicativo de gestión creado por la Secretaría Distrital de Salud.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='display: flex; justify-content: center; margin-top: 20px;'>
        <video width="1258" height="687" controls>
            <source src="https://raw.githubusercontent.com/Tellomen/Mas-Bienestar/main/Mas%20Bienestar.mp4" type="video/mp4">
            Tu navegador no soporta la etiqueta de video.
        </video>
    </div>
    """, unsafe_allow_html=True)

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

def modulo_plan_cuidado_familiar():
    st.markdown("## PLAN CUIDADO FAMILIAR")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
            <div style="border: 2px solid #ccc; border-radius: 15px; padding: 10px; height: 400px; width: 100%; text-align: center; background-color: #f5f5f5;">
                <p><b>[Video de Bienvenida]</b></p>
                <img src="https://img.icons8.com/ios-filled/100/play-button-circled.png"/>
                <p>Video explicativo del módulo</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("#### Diligenciamiento aplicativo GITAPPS")
        st.write("""
        En el marco de la implementación del Modelo Más Bienestar, este módulo permite abordar integralmente las condiciones de salud, entorno y necesidades sociales de las familias.
        """)

    st.markdown("---")
    st.subheader("Líneas Temáticas del Plan de Cuidado Familiar")

    temas = {
        "Gestantes": "**Embarazadas con Más Bienestar, Ángeles Guardianes**\n\nAcompañamiento a gestantes con enfoque integral.",
        "Infancia": "**Promoción de la Alimentación Saludable**\n\n- Prevención de IRA\n- Lactancia materna\n- Pautas de crianza",
        "Crónicos": "**Condiciones Crónicas**\n\n- Autocuidado\n- Actividad física\n- Seguimiento clínico",
        "Salud Mental": "**Salud Mental Familiar**\n\n- Estrategias de afrontamiento\n- Duelo\n- Pautas de crianza",
        "Salud Bucal": "**Cuidado Bucal**\n\n- Higiene\n- Educación preventiva\n- Autocuidado",
        "Salud Ambiental": "**Ambiente Saludable**\n\n- Vivienda\n- Agricultura urbana\n- Riesgos ambientales",
        "Discapacidad y Cuidadores": "**Rehabilitación Comunitaria**\n\n- Apoyo a cuidadores\n- Inclusión\n- Autonomía funcional"
    }

    for tema, contenido in temas.items():
        with st.expander(f"📌 {tema}", expanded=False):
            st.markdown(contenido)

    st.markdown("---")
    st.caption("Módulo en construcción – Herramienta digital del Modelo Más Bienestar")

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

    opciones = ["Bienvenida y Entorno", "Evaluación", "PLAN DE CUIDADO FAMILIAR"]
    if perfil.upper() == "ADMINISTRADOR":
        opciones += list(modulos_perfil.keys())
    elif perfil in modulos_perfil:
        opciones.append(perfil)

    modulo = st.sidebar.selectbox("Selecciona un módulo:", opciones)

    if modulo == "Bienvenida y Entorno":
        modulo_entorno()
    elif modulo == "Evaluación":
        modulo_evaluacion()
    elif modulo == "PLAN DE CUIDADO FAMILIAR":
        modulo_plan_cuidado_familiar()
    elif modulo in modulos_perfil:
        modulo_perfil(modulo, modulos_perfil[modulo])
