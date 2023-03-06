from bs4 import BeautifulSoup
import pandas as pd
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from googlesearch import search

# data

source = "https://www.kaggle.com/datasets/wyattowalsh/basketball?resource=download-directory&select=csv"
player_profile = pd.read_csv("data/common_player_info.csv")
players_stats = pd.read_csv("data/nba2021_per_game.csv")

# main menu

selected = option_menu(
    menu_title=None,
    options=["Inicio", "Jugador", "Estadísticas", "Acerca de"],
    icons=["house", "bar-chart", "info-circle"],
    menu_icon="gear",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"background-color": "#585C86", "width": "100%"},
        "icon": {"color": "#bde0fe"},
        "nav-link": {"--hover-color": "#414464"},
        "nav-link-selected": {"background-color": "#2b2d42"},
    }
)

# functions

def get_player_profile(player_name):
    player = player_profile[player_profile["display_first_last"] == player_name]

    heightFt = player["height"].values[0].replace("-", ".")
    heightMt = float(heightFt) * 0.3048
    player["height"] = heightMt

    player["weight"] = player["weight"].values[0] * 0.45359237

    playerInfo = pd.DataFrame({
        "Nombre completo": player["display_first_last"],
        "Posición": player["position"],
        "Altura (mts)": player["height"],
        "Peso (kgs)": player["weight"],
        "Nacimiento": player["birthdate"],
        "Universidad": player["school"]
    })

    return playerInfo

def get_player_slug(player_name):
    player = player_profile[player_profile["display_first_last"] == player_name]
    player_slug = player["player_slug"].values[0]
    return player_slug

def get_player_img(query):
    for j in search(query, num=10, stop=10, pause=1):
        url = j
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            src = img_tag.get('src')
            if src and src.startswith('http') and src.endswith('.jpg'):
                st.image(src)

# content

if selected == "Inicio":
    st.title("Inicio")
    st.markdown("##### Bienvenido a la plataforma de análisis estadístico sobre la NBA.")
    st.markdown("Desde puntos por partido, asistencias, rebotes, triples, etc. hasta estadísticas de equipos, jugadores, entrenadores, etc.")
    st.markdown(f"Datos sacados de [Kaggle]({source}).")
    st.markdown("*Nota: Esta plataforma ha sido desarrollada por **Alejandro Sanmartín** para la asignatura de Desarrollo Web en Entorno Servidor del Grado Superior Desarrollo de Aplicaciones Web en CPIFP Los Enlaces.*")

elif selected == "Jugador":
    st.title("Perfil de jugador")
    st.markdown("##### Selecciona un jugador para ver su perfil.")

    player_name = st.selectbox("Jugador", player_profile["display_first_last"].unique())

    player_slug = get_player_slug(player_name)
    player = get_player_profile(player_name)

    st.table(player)
    get_player_img(player_slug)

elif selected == "Estadísticas":
    st.title("Estadísticas temporada 2020-2021")
    st.markdown("*Bubble Edition*")

    st.markdown("##### Mejores anotadores.")
    # st.table(players_stats.sort_values(by="PTS", ascending=False).head(10))
    st.bar_chart(players_stats.sort_values(by="PTS", ascending=False).head(10)["PTS"].groupby(players_stats["Player"]).sum())

    st.markdown("##### Mejores reboteadores.")
    st.bar_chart(players_stats.sort_values(by="TRB", ascending=False).head(10)["TRB"].groupby(players_stats["Player"]).sum())

    st.markdown("##### Mejores asistentes.")
    st.bar_chart(players_stats.sort_values(by="AST", ascending=False).head(10)["AST"].groupby(players_stats["Player"]).sum())

elif selected == "Acerca de":
    st.title("Acerca de")

    st.markdown("##### Desarrollado por Alejandro Sanmartín")
    st.markdown("##### Grado Superior Desarrollo de Aplicaciones Web")
    st.markdown("##### CPIFP Los Enlaces")

    
