import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# sidebar menu

selected = option_menu(
    menu_title=None,
    options=["Inicio", "Análisis general", "Acerca de"],
    icons=["house", "bar-chart", "info-circle"],
    menu_icon="gear",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"background-color": "#585C86"},
        "icon": {"color": "#bde0fe"},
        "nav-link": {"--hover-color": "#414464"},
        "nav-link-selected": {"background-color": "#2b2d42"},
    }
)

# main menu

if selected == "Inicio":
    st.title("Inicio")

elif selected == "Análisis general":
    st.title("Análisis coyuntural")

elif selected == "Acerca de":
    st.title("Acerca de")
