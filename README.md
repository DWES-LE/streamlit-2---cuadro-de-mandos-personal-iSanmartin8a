# 📈 Cuadro de mandos personal 📊
 
> Usa este repositorio para crear un cuadro de mandos personal con Streamlit. Documenta los siguientes apartados del README.
> Incluye en tu README la url de donde has publicado tu aplicación. Pon la `url` también en el `About` de tu repositorio.

## Objetivo
Diseño de un cuadro de mandos personal para visualización e interacción con un conjunto de datos.

He creado un cuadro de mandos personal para visualizar los datos de la NBA. En él podemos observar los datos de los jugadores de la NBA, como su altura, peso, posición, etc. También podemos observar los datos de los equipos de la NBA, como son sus jugadores en la temporada 2021/2022. Hay una sección en la que poder ver qué jugador serías en función de tu dominio en los puntos, rebotes y asistencias.

También puedes observar el campeón y los finalistas por año, o por otra parte el número de campeonatos por cada franquicia. También hago un scrapeo a la API de Google de donde extraigo imágenes según el parámetro (string) que selecciones.

## Los datos
Elige un conjunto de datos que te interese: educación, deportes, trabajo, música, econocomía, etc.

El conjunto de datos elegido es el de la NBA. En él podemos observar los datos de los jugadores de la NBA, como su altura, peso, posición, etc. También podemos observar los datos de los equipos de la NBA, como son sus jugadores en la temporada 2021/2022. Por último, tenemos un dataset con los datos de los campeonatos de la NBA por año y por franquicia.

## Búsqueda de los datos
Busca una fuente para tus datos. Puedes usar una API de un portal de datos abiertos, un conjunto ya publicado, recopilar personalmente datos por scraping, etc.

Hemos usado como fuente una web de datasets públicos como es Kaggle. En ella hemos encontrado el dataset de la NBA. También hemos usado la API de Google para hacer un scrapeo de imágenes.

## Documentación de los datos
Documenta los datos que vas a usar y su origen. De dónde los has sacado, fuentes, etc. Describe los campos, los valores, las unidades, etc.

Los datos de la NBA los hemos sacado de Kaggle.

Tenemos tres datasets:
    - Franquicias.csv: Contiene los datos de las franquicias de la NBA. Campeonatos por franquicia y por año, también nos da datos como los finalistas o los MVPs.
    - PerfilesJugador.csv: Contiene los datos de los jugadores de la NBA. Altura, peso, posición, etc.
    - Stats2021pp.csv: Contiene los datos de los jugadores de la NBA en la temporada 2021/2022. Estadísticas de los jugadores por partido como puntos, rebotes, asistencias, etc.

## Prepara tu aplicación.
La aplicación se llamará `app.py`. Añade un `requirements.txt` con las dependencias de tu aplicación. Ve actualizándolo a medida que vayas añadiendo librerías.

Nuestra aplicación se llama como corresponde y hemos ido haciendo 'pip freeze > requirements.txt' para ir añadiendo las librerías que hemos ido necesitando.

## Carga y análisis de conjunto de dato con pandas
Carga el conjunto de datos en un dataframe de pandas y realiza un análisis exploratorio de los datos.

Hemos leído los datos con pandas y hemos hecho un análisis exploratorio de los datos. Hemos visto que los datos están en varios datasets así que los hemos almacenado en varios DataFrames diferentes.

## Visualización de los datos
Prepara visualizaciones diferentes del dataframe en texto (tablas) o gráficas (histogramas, barras, etc.). Puedes usar matplotlib, seaborn, plotly, etc.

Hemos usado matplotlib para hacer gráficas de tarta y también hemos utilizado los gráficos de barras y sliders de streamlit.

## Diseña la interacción que van a tener tus datos
Qué inputs y outputs tendrán tus datos.

Hemos hecho una interacción con los datos de los jugadores de la NBA. Podemos ver los datos de los jugadores, filtrarlos por nombre o por equipo. También podemos ver los datos de los equipos de la NBA y filtrarlos por nombre o por franquicia. Los campeonatos de la NBA los podemos ver por franquicia o por año. También podemos ver qué jugador seríamos en función de nuestro dominio en los puntos, rebotes y asistencias a través de sliders.

## Prepara la aplicación (cuadro de mandos) con Streamlit
Prepara y prueba la aplicación.

Hemos preparado la aplicación con streamlit y hemos probado que todo funciona correctamente.

## Publica la aplicación.
Publica la aplicación en Streamlit Cloud, en Heroku o en el servicio que prefieras https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app

Hemos publicado la aplicación en Streamlit Cloud.