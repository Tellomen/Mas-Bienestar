import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# ------------------------- CONFIGURACIÓN DE PÁGINA --------------------------
st.set_page_config(page_title="Inducción Más Bienestar", layout="wide")

# URL del Google Sheet exportado como CSV
CSV_URL = "https://docs.google.com/spreadsheets/d/1sHq2UATtF5q_IINt82C0X_ah_m-ac5Et/export?format=csv"

# ------------------------- CARGAR BASE DE TALENTO HUMANO ---------------------
@st.cache_data(ttl=60)  # Cache por 60 segundos
def cargar_talento_humano():
    df = pd.read_csv(CSV_URL)
    df.columns = df.columns.str.strip().str.lower()
    return df

talento_humano = cargar_talento_humano()

# ------------------------- IMAGEN DE FONDO ----------------------------------
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

            # Condición de contraseña según perfil
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
    "Gestores": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Toma de Medidas", "Tamizaje Apgar"],
    "Psicólogos": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"],
    "Enfermeros(as)": ["Caracterización Familiar", "Plan de Cuidado Familiar", "Compromisos Concertados", "Toma de Alertas", "Tamizaje Apgar", "Eventos VSP"]
}

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

# ------------------------- CONTROL DE SESIÓN --------------------------------
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    login()
else:
    perfil = st.session_state["perfil"]
    st.sidebar.title(f"👤 {st.session_state['nombre']} ({perfil})")

    # Botón de Cerrar Sesión
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state["autenticado"] = False
        st.experimental_rerun()

    # Menú dinámico según el perfil
    opciones = ["Bienvenida y Entorno", "Evaluación"]

    if perfil.upper() == "ADMINISTRADOR":
        opciones += list(modulos_perfil.keys())
    elif perfil in modulos_perfil:
        opciones.append(perfil)

    modulo = st.sidebar.selectbox("Selecciona un módulo:", opciones)

    if modulo == "Bienvenida y Entorno":
        modulo_entorno()
    elif modulo == "Evaluación":
        modulo_evaluacion()
    elif modulo in modulos_perfil:
        modulo_perfil(modulo, modulos_perfil[modulo])
