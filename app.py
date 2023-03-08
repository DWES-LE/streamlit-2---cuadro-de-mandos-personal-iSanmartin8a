import io
import time
from bs4 import BeautifulSoup
import pandas as pd
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from googlesearch import search
from PIL import Image
import matplotlib.pyplot as plt

# data

source = "https://www.kaggle.com/datasets/wyattowalsh/basketball?resource=download-directory&select=csv"
player_profile = pd.read_csv("data/PerfilesJugador.csv")
players_stats = pd.read_csv("data/Stats2021pp.csv")
seasons_champs = pd.read_csv("data/Franquicias.csv")

# main menu

with st.sidebar:
    selected = option_menu(
        menu_title="Apartados",
        options=["Inicio", "Jugadores", "Equipos", "Campeonatos", "Acerca de"],
        icons=["house", "person-bounding-box", "bar-chart", "trophy", "info-circle"],
        menu_icon="gear",
        default_index=0,
        orientation="vertical",
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

def show_images_in_table(image_urls):
    num_images = len(image_urls)
    num_cols = 3 # Definir el número de columnas que quieres mostrar

    # Calcular el número de filas necesarias en función del número de imágenes y el número de columnas
    num_rows = num_images // num_cols + (1 if num_images % num_cols != 0 else 0)

    # Crear una tabla de Streamlit con el número de filas y columnas necesarios
    for row in range(num_rows):
        cols = st.columns(num_cols)
        for col in range(num_cols):
            idx = row * num_cols + col
            if idx < num_images:
                # Mostrar la imagen en la tabla
                with cols[col]:
                    st.image(image_urls[idx], width=200)

def get_player_img(query):

    imagenes = []

    for j in search(query, num=9, stop=9, pause=1):
        url = j
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            src = img_tag.get('src')
            if src and src.startswith('http') and src.endswith('.jpg'):
                imagenes.append(src)
    
    show_images_in_table(imagenes)

def progressBarRunning():
    progress_bar = st.progress(0)
    progress_text = st.empty()
    for i in range(101):
        time.sleep(0.1)
        progress_bar.progress(i)
        progress_text.text(f"Progreso: {i}%")
    for i in range(2):
        time.sleep(1)
        progress_bar.empty()
        progress_text.empty()

# content

def main_strengths(player_name):
    promedioPts = players_stats["PTS"].mean()
    promedioAst = players_stats["AST"].mean()
    promedioReb = players_stats["TRB"].mean()

    player = players_stats[players_stats["Player"] == player_name]

    pts = player["PTS"].values[0]
    ast = player["AST"].values[0]
    reb = player["TRB"].values[0]

    maxPts = players_stats["PTS"].max()
    maxAst = players_stats["AST"].max()
    maxReb = players_stats["TRB"].max()

    prPts = pts/maxPts
    prAst = ast/maxAst
    prReb = reb/maxReb

    prTotal = prPts + prAst + prReb

    prPtosStrength = prPts/prTotal
    prAstStrength = prAst/prTotal
    prRebStrength = prReb/prTotal

    labels = ["Puntos", "Asistencias", "Rebotes"]
    sizes = [prPtosStrength, prAstStrength, prRebStrength]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal') 

    st.pyplot(fig1)

    st.markdown(f'Destaca en {prPtosStrength*100:.2f}% en anotación, {prAstStrength*100:.2f}% en asistencias y {prRebStrength*100:.2f}% en rebotes.')

    if prPtosStrength > prAstStrength and prPtosStrength > prRebStrength:
        st.markdown(f'**{player_name}** es anotador.')
    elif prAstStrength > prPtosStrength and prAstStrength > prRebStrength:
        st.markdown(f'**{player_name}** es asistente.')
    elif prRebStrength > prPtosStrength and prRebStrength > prAstStrength:
        st.markdown(f'**{player_name}** es reboteador.')

if selected == "Inicio":
    st.title("Inicio")
    st.markdown("##### Bienvenido a la plataforma de análisis estadístico sobre la NBA.")
    st.markdown("Desde puntos por partido, asistencias, rebotes, triples, etc. hasta estadísticas de equipos, jugadores, entrenadores, etc.")
    st.markdown("*Nota: Esta plataforma ha sido desarrollada por **Alejandro Sanmartín** para la asignatura de Desarrollo Web en Entorno Servidor del Grado Superior Desarrollo de Aplicaciones Web en CPIFP Los Enlaces.*")

    st.subheader("Perfil de jugador")
    st.markdown("*Para empezar a testear la web, selecciona un jugador para ver su perfil.*")

    player_name = st.selectbox("Jugador", player_profile["display_first_last"].unique())

    player_slug = get_player_slug(player_name)
    player = get_player_profile(player_name)

    st.table(player)

    if st.checkbox("Mostrar imágenes del jugador en Google"):
        progressBarRunning()
        get_player_img(player_slug + " nba")

elif selected == "Jugadores":
    st.title("Estadísticas")

    st.markdown("##### Estadísticas de la temporada 2021/22.")
    st.markdown("*Bubble Edition*")

    st.markdown("##### Mejores anotadores.")
    # st.table(players_stats.sort_values(by="PTS", ascending=False).head(10))
    st.bar_chart(players_stats.sort_values(by="PTS", ascending=False).head(10)["PTS"].groupby(players_stats["Player"]).mean())

    st.markdown("##### Mejores reboteadores.")
    st.bar_chart(players_stats.sort_values(by="TRB", ascending=False).head(10)["TRB"].groupby(players_stats["Player"]).mean())

    st.markdown("##### Mejores asistentes.")
    st.bar_chart(players_stats.sort_values(by="AST", ascending=False).head(10)["AST"].groupby(players_stats["Player"]).mean())

    st.markdown("Selecciona un jugador para ver sus fortalezas.")
    player_name = st.selectbox("Jugador", players_stats["Player"].unique())

    main_strengths(player_name)

    apartado = st.radio("Selecciona una estadística para ver el gráfico de puntos por partido.", ("PTS", "AST", "TRB", "STL", "BLK", "TOV", "PF", "FG%", "3P%", "FT%"))
    st.bar_chart(players_stats.sort_values(by=apartado, ascending=False).head(10)[apartado].groupby(players_stats["Player"]).mean())

elif selected == "Equipos":

    equipo = st.selectbox("Selecciona un equipo para ver sus jugadores.", players_stats["Tm"].unique())
    st.table(players_stats[players_stats["Tm"] == equipo])

    if st.checkbox("Mostrar imágenes del equipo en Google"):
        progressBarRunning()
        get_player_img(equipo + " logo nba")

elif selected == "Campeonatos":
    st.title("Campeonatos")
    st.markdown("##### Estadísticas de campeonatos.")

    st.markdown("*Selecciona un año para ver el resultado de la temporada.*")
    year = st.selectbox("Año", seasons_champs["Year"].unique())
    st.table(seasons_champs[seasons_champs["Year"] == year])

    st.markdown("*Selecciona una franquicia para ver sus campeonatos y los resultados.*")
    franquicia = st.selectbox("Franquicia", seasons_champs["NBA Champion"].unique())
    st.table(seasons_champs[seasons_champs["NBA Champion"] == franquicia])

    st.markdown("*Gráfico de barras con el número de campeonatos por franquicia.*")
    st.bar_chart(seasons_champs["NBA Champion"].value_counts())

    st.markdown(f'El equipo más ganador de la NBA es **{seasons_champs["NBA Champion"].value_counts().idxmax()}** con **{seasons_champs["NBA Champion"].value_counts().max()}** campeonatos.')

    labels = seasons_champs["NBA Champion"].value_counts().index
    sizes = seasons_champs["NBA Champion"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

elif selected == "Acerca de":
    st.title("Acerca de")

    st.subheader("Información del proyecto")
    st.markdown("- Desarrollado por Alejandro Sanmartín")
    st.markdown("- Grado Superior Desarrollo de Aplicaciones Web")
    st.markdown("- CPIFP Los Enlaces")

    st.subheader("Desarrollo del trabajo")

    st.markdown("La idea principal era comentar y analizar los datos de la NBA, pero al final decidí crear una plataforma web para poder mostrar los datos de una forma más visual y atractiva.")
    st.markdown("Comenzamos elaborando un menú de navegación para poder acceder a las diferentes secciones de la plataforma. Esto se realizó a través de la herramienta streamlit-option-menu.")
    st.markdown("Una vez hecho esto, decidí crear una sección de inicio para dar la bienvenida al usuario y explicarle un poco el funcionamiento de la plataforma.")
    st.markdown("La siguiente sección que decidí crear fue la de jugadores, donde se muestran los datos de los jugadores de la NBA. Se hace uso de un dataset de Kaggle para obtener los datos de los jugadores y se muestra una tabla con los datos de los mismos.")
    st.markdown("En la siguiente sección, se muestran las estadísticas de la temporada 2021/22. Se muestran los mejores anotadores, reboteadores y asistentes de la temporada. También se puede seleccionar un jugador para ver sus fortalezas y un gráfico de barras con las estadísticas de la temporada.")
    st.markdown("La siguiente sección es la de equipos, donde se muestran los jugadores de cada equipo.")
    st.markdown("La última sección es la de campeonatos, donde se muestran los campeonatos de la NBA y los resultados de cada temporada. Puedes filtrar por año o franquicia para ver los resultados.")
    st.markdown("Por último, se ha creado una sección de acerca de, donde se muestra información sobre el proyecto.")

    st.markdown("##### *Tecnologías utilizadas*")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Python")
        st.write("Streamlit")
    with col2:
        st.write("Pandas")
        st.write("Matplotlib")
    with col3:
        st.write("BeautifulSoup")
        st.write("Google Images Search")

    st.markdown("##### *Fuentes de datos*")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("- [Kaggle](https://www.kaggle.com/nathanlauga/nba-games)")
    with col2:
        st.markdown("- [Google Images Search](https://pypi.org/project/google-images-download/)")
