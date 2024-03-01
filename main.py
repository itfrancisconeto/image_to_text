import streamlit as st
from PIL import Image
import pytesseract
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Swiss Army Knife",
    page_icon=""
)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: black;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image('avatar.jpg')
    selected = option_menu(
        menu_title = None,
        options=["Imagem > Texto"],
        icons=["list-task"],
        styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "white", "font-size": "15px"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "gray"},
            },
    )

if selected == "Imagem > Texto":    
    sc1, sc2, sc3 = st.columns([4,1,4])
    text = ''
    with sc1:
        st.markdown("<h1 style='text-align: center; color: white;'>Imagem</h1>", unsafe_allow_html=True)
        upload = st.file_uploader('Extrair texto da imagem:', type=['jpg'])
        if upload:   
            image = Image.open(upload)
            sc1.image(image)    
            text = pytesseract.image_to_string( image )
            text = text.strip("\n")
    with sc3:        
        st.markdown("<h1 style='text-align: center; color: white;'>Texto</h1>", unsafe_allow_html=True)
        sc3.text(text)
