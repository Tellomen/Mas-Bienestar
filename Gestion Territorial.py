# ------------------------- MÓDULO GESTIÓN TERRITORIAL -----------------------
def modulo_gestion_territorial():
    st.markdown("""
    <div class='welcome-box'>
        <h2>📍 Módulo: Gestión Territorial</h2>
        <p>En este espacio encontrarás el material audiovisual y los recursos interactivos para comprender
        el proceso de Gestión Territorial en el marco del programa Más Bienestar.</p>
    </div>
    """, unsafe_allow_html=True)

    # Video
    st.markdown("""
    <div style='display: flex; justify-content: center; margin-top: 10px; margin-bottom: 20px;'>
        <video width="1257" height="732" controls>
            <source src="https://raw.githubusercontent.com/Tellomen/Mas-Bienestar/main/Mas%20Bienestar%20ruralidad.mp4" type="video/mp4">
            Tu navegador no soporta la etiqueta de video.
        </video>
    </div>
    """, unsafe_allow_html=True)

    # Plantilla Genially
    st.markdown("""
    <div style='display: flex; justify-content: center; margin-top: 20px;'>
        <iframe title="Gestión Territorial"
            src="https://view.genially.com/6893e9fda1dcf302e7411d14"
            width="1257"
            height="732"
            style="border: none; box-shadow: 0 0 10px rgba(0,0,0,0.2);">
        </iframe>
    </div>
    """, unsafe_allow_html=True)
