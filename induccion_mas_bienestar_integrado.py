import streamlit as st
import streamlit.components.v1 as components

def modulo_entorno():
    st.markdown("""
    <div class='welcome-box'>
        <h2>🌍 Bienvenida y Descripción del Entorno</h2>
        <p><b>Bienvenido(a) al proceso de inducción del programa Más Bienestar.</b></p>
    </div>
    """, unsafe_allow_html=True)

    # Video justo debajo del texto principal
    st.markdown("""
    <div style='display: flex; justify-content: center; margin-top: 10px; margin-bottom: 20px;'>
        <video width="1257" height="732" controls>
            <source src="https://raw.githubusercontent.com/Tellomen/Mas-Bienestar/main/Mas%20Bienestar.mp4" type="video/mp4">
            Tu navegador no soporta la etiqueta de video.
        </video>
    </div>
    """, unsafe_allow_html=True)

    # Continúa el resto del texto debajo del video
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

    # Avatar animado
    st.markdown("""
    <div style='display: flex; justify-content: center; margin-top: 20px;'>
        <img src='https://media.tenor.com/lPZZzG9NPuoAAAAi/avatar-speaking.gif' width='180'>
    </div>
    """, unsafe_allow_html=True)

    # Botón que abre Genially en una nueva pestaña
    st.markdown("""
    <div style='text-align: center; margin-top: 40px;'>
        <a href="https://view.genially.com/68913d5fcb9d97c53e1192d6" target="_blank">
            <button style="font-size:18px; padding: 12px 30px; background-color: #4CAF50; color: white; border: none; border-radius: 8px; cursor: pointer;">
                Siguiente
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
def modulo_genially():
    st.markdown("## 🧩 Módulo Interactivo - Plantilla")
    st.markdown("A continuación, puedes explorar la plantilla interactiva:")

    # Genially embebido
    components.html("""
    <div style="display: flex; justify-content: center; margin-top: 30px;">
        <iframe title="Modulo de Bienvenida"
            src="https://view.genially.com/68913d5fcb9d97c53e1192d6"
            width="1257"
            height="732"
            style="border: none; box-shadow: 0 0 10px rgba(0,0,0,0.2);"
            allowfullscreen="true"
            scrolling="yes"
            allowscriptaccess="always"
            allownetworking="all">
        </iframe>
    </div>
    """, height=800)

# ---------------------- LÓGICA DE NAVEGACIÓN -------------------------

# Inicializa el estado si no existe
if 'entorno_pagina' not in st.session_state:
    st.session_state.entorno_pagina = "bienvenida"

# Muestra la sección correspondiente
if st.session_state.entorno_pagina == "bienvenida":
    modulo_entorno()
elif st.session_state.entorno_pagina == "genially":
    modulo_genially()
