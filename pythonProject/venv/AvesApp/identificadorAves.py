"""Esta aplicación es un intento de facilitar la identificación de aves en Galicia y en el norte de Portugal; y más
concretamente en "O Baixo Miño" y "O Alto Minho".
Está pensada para aquellas personas a las que les gusta la naturaleza y se sienten atraidas por las aves en particular.
Mediante un sistema de filtros, sobre las características de los pájaros, irán acotando la búsqueda hasta dar con
el ave que han visto."""

# Importamos las librerías streamlit con su alias 'st', y pandas con el suyo 'pd'.

import streamlit as st
import pandas as pd

# A la pestaña de la página le damos un título, un icono y modificamos el diseño del área de la página ensanchándola
st.set_page_config(
    page_title='Buscador de Aves do Baixo Miño',
    # page_icon='🪶',
    page_icon=':owl:',
    layout='wide',
)

# Pomemos el título
st.title("_Buscador De Aves Do Baixo Miño_")
st.caption(
    """
    **Espacio declarado Red Natura 2000 y** 
    **Zona de Especial Protección para las Aves (ZEPA)**.
    https://es.wikipedia.org/wiki/Red_Natura_2000  
    **Baixo Miño**.
    https://gl.wikipedia.org/wiki/Comarca_do_Baixo_Mi%C3%B1o
"""
)
# Inicializamos todos los filtros de la barra lateral con una cadena vacía para que al iniciar la aplicación no dé
# ningún error.
nombreAve = tamanoAve = habitatAve = comportamientoAve = colorAve = patasColor = picoColor = picoForma = picoGrorsor = \
    picoLongitud = ""
# Creamos la barra latertal
with st.sidebar:
    # Informamos de los pasos a seguir
    st.subheader('_Uso del buscador:_')
    st.write("**_Si sabes el ave, pincha en la casilla de verificación 'Ave', más abajo, y búscala en "
             "el desplegable._**")
    st.write("**_Si no la sabes, sigue las instruciones:_**")
    st.write(
        "**_1. Para iniciar la identificación elige algún filtro, pincha en la flecha "
        "del cuadro de selección y busca una opción._**")
    st.write("**_2. Con cada filtro elegido vamos cribando el número de aves._**")
    st.write("**_3. Ve eligiendo el filtro que más te convenga._**")
    st.write("**_4. El orden de elección de los filtros no es importante._**")
    st.write(
        "**_5. Si con los filtros elegidos no encuentras tu ave, limpia los filtros y vuelve a empezar._**")
    st.caption("_____________________")
    # Creamos la etiqueta subtítulo 'Filtro'
    st.subheader('Filtros:')
    # Creamos un botón para borrar la selección de filtros de una sola vez
    if st.button("Limpiar Filtros"):
        st.checkbox('Ave:', value=False, key=1)
        st.checkbox('Tamaño:', value=False, key=2)
        st.checkbox('Hábitat:', value=False, key=3)
        st.checkbox('Comportamiento:', value=False, key=4)
        st.checkbox('Color:', value=False, key=5)
        st.checkbox('Patas color:', value=False, key=6)
        st.checkbox('Pico color:', value=False, key=7)
        st.checkbox('Pico forma:', value=False, key=8)
        st.checkbox('Pico grosor:', value=False, key=9)
        st.checkbox('Pico longitud:', value=False, key=10)
        st.stop()
    # Creamos las casillas de verificación y sus opciones correspondientes. La primera opoción son todas las aves para
    # que si el usuario conoce el ave pueda elegirla e ir directamente a la ficha y foto de esa ave.
    # En caso contrario creamos los checkbox de cada filtro de búsqueda en la barra lateral con sus opciones correspondientes y la
    # primera vacía.
    if st.checkbox('Ave:'):
        nombreAve = st.selectbox('Elige un ave', ['',
                                                  'Abubilla',
                                                  'Acentor Común',
                                                  'Agachadiza Chica',
                                                  'Agachadiza Común',
                                                  'Águila Pescadora',
                                                  'Agateador Común',
                                                  'Aguja Colipinta',
                                                  'Alcatraz',
                                                  'Alcotán',
                                                  'Ánade Azulón',
                                                  'Andarríos Chico',
                                                  'Archibebe Claro',
                                                  'Arrendajo',
                                                  'Avión Común',
                                                  'Azor',
                                                  'Bisbita Común',
                                                  'Buitrón',
                                                  'Camachuelo Común',
                                                  'Carbonero Común',
                                                  'Carbonero Garrapinos',
                                                  'Carricerín Cejudo',
                                                  'Cernícalo Vulgar',
                                                  'Charrán Común',
                                                  'Charrán Patinegro',
                                                  'Chochín',
                                                  'Chorlitejo Grande',
                                                  'Chorlitejo Patinegro',
                                                  'Chorlito Gris',
                                                  'Chotacabras Gris',
                                                  'Cigüeña Blanca',
                                                  'Colirrojo Tizón',
                                                  'Cormorán Grande',
                                                  'Cormorán Moñudo',
                                                  'Corneja Negra',
                                                  'Correlimos Común',
                                                  'Correlimos Tridáctilo',
                                                  'Críalo',
                                                  'Cuco',
                                                  'Curruca Cabecinegra',
                                                  'Curruca Capirotada',
                                                  'Curruca Mosquitera',
                                                  'Curruca Rabilarga',
                                                  'Curruca Zarcera',
                                                  'Escribano Cerillo',
                                                  'Escribano Montesino',
                                                  'Escribano Palustre',
                                                  'Escribano Soteño',
                                                  'Espátula',
                                                  'Estornino Negro',
                                                  'Estornino Pinto',
                                                  'Faisán Vulgar',
                                                  'Focha Común',
                                                  'Fumarel Común',
                                                  'Garceta Común',
                                                  'Garceta Grande',
                                                  'Garza Real',
                                                  'Gavilán',
                                                  'Gaviota Argéntea',
                                                  'Gaviota Patiamarilla',
                                                  'Gaviota Reidora',
                                                  'Gaviota Sombría',
                                                  'Golondrina Común',
                                                  'Golondrina Daúrica',
                                                  'Gorrión Común',
                                                  'Gorrión Molinero',
                                                  'Halcón Abejero',
                                                  'Halcón Común',
                                                  'Herrerillo Capuchino',
                                                  'Herrerillo Común',
                                                  'Jilguero',
                                                  'Lavandera Blanca Común',
                                                  'Lavandera Boyera Ibérica',
                                                  'Lavandera Cascadeña',
                                                  'Lechuza Común',
                                                  'Lúgano',
                                                  'Martín Pescador',
                                                  'Milano Negro',
                                                  'Mirlo Común',
                                                  'Mito',
                                                  'Mochuelo Común',
                                                  'Mosquitero Común',
                                                  'Negrón Común',
                                                  'Ostrero',
                                                  'Paloma Torcaz',
                                                  'Papamoscas Cerrojillo',
                                                  'Pardillo Común',
                                                  'Perdiz Común',
                                                  'Petirrojo',
                                                  'Pico de Coral',
                                                  'Pico Menor',
                                                  'Pico Picapinos',
                                                  'Pinzón Vulgar',
                                                  'Pito Real',
                                                  'Polla de Agua',
                                                  'Ratonero Común',
                                                  'Reyezuelo Listado',
                                                  'Reyezuelo Sencillo',
                                                  'Tarabilla Común',
                                                  'Tórtola Común',
                                                  'Tórtola Turca',
                                                  'Urraca',
                                                  'Vencejo Común',
                                                  'Verdecillo',
                                                  'Verderón',
                                                  'Vuelvepiedras',
                                                  'Zarapito Trinador',
                                                  'Zarcero Común',
                                                  'Zorzal Común',
                                                  ])

    if st.checkbox('Tamaño:'):
        tamanoAve = st.selectbox('Elige tamaño', ['',
                                                  'Más pequeño  que un gorrión',
                                                  'Como un gorrión',
                                                  'Entre un gorrión y un mirlo',
                                                  'Como un mirlo',
                                                  'Entre un mirlo y una paloma',
                                                  'Como una paloma',
                                                  'Entre una paloma y un pato',
                                                  'Como un pato',
                                                  'Más grande que un pato',
                                                  ])

    if st.checkbox('Hábitat'):
        habitatAve = st.selectbox('Elige hábitat', ['',
                                                    'Arbustos',
                                                    'Bosque/Árboles',
                                                    'Cortados/Acantilados',
                                                    'Costa',
                                                    'Cultivos',
                                                    'Herbazales',
                                                    'Humedales',
                                                    'Llanuras',
                                                    'Urbanos',
                                                    'Ribera',
                                                    ])

    if st.checkbox("Comportamiento"):
        comportamientoAve = st.selectbox('Elige comportamiento', ['',
                                                                  'Buceando/Nadando',
                                                                  'Caminando',
                                                                  'Cazando/Pescando',
                                                                  'Cerniéndose',
                                                                  'Con otras aves',
                                                                  'En un bando o grupo',
                                                                  'Hurgando en el limo',
                                                                  'Inmóvil',
                                                                  'Moviendo la cola',
                                                                  'Picoteando en el suelo',
                                                                  'Posado en un oteadero',
                                                                  'Saltando',
                                                                  'Volando/Planeando',
                                                                  ])

    if st.checkbox("Color"):
        colorAve = st.selectbox(
            'Elige color', ['',
                            'Amarillo',
                            'Azul',
                            'Blanco',
                            'Crema',
                            'Gris',
                            'Marrón',
                            'Naranja',
                            'Negro',
                            'Pío: blanco y negro',
                            'Rojo',
                            'Verde',
                            ])

    if st.checkbox("Patas color"):
        patasColor = st.selectbox(
            'Elige color patas', ['',
                                  'Amarillo',
                                  'Azul',
                                  'Blanco',
                                  'Gris',
                                  'Marrón',
                                  'Naranja',
                                  'Negro',
                                  'Rojo',
                                  'Rosa',                                  
                                  'Verde',             
                                  ])

    if st.checkbox("Pico color"):
        picoColor = st.selectbox(
            'Elige color pico', ['',
                                 'Amarillo',
                                 'Blanco',
                                 'Crema',
                                 'Gris',
                                 'Marrón',
                                 'Naranja',
                                 'Negro',
                                 'Rosa',                                 
                                 'Rojo',
                                 'Verde',
                                 ])

    if st.checkbox("Pico forma"):
        picoForma = st.selectbox(
            'Elige forma pico', ['',
                                 'Cónico',
                                 'Curvado',
                                 'Ganchudo',
                                 'Pato',
                                 'Puñal',
                                 'Recto',
                                 ])

    if st.checkbox("Pico grosor"):
        picoGrorsor = st.selectbox(
            'Elige grosor pico', ['',
                                  'Fino',
                                  'Medio',
                                  'Grueso',
                                  ])

    if st.checkbox("Pico longitud"):
        picoLongitud = st.selectbox(
            'Elige longitud pico', ['',
                                    'Corto',
                                    'Medio',
                                    'Largo',
                                    ])

# Pomemos el título
# st.title("_Buscador De Aves Do Baixo Miño_")

# Dividimos la página en dos columnas iguales
col1, col2 = st.columns([1, 1], gap="large")
# Podemos hacerla de igual tamaño de esta otra forma:
# col1, col2 = st.columns(2)

# En la columna de la izquierda mostraremos la/s foto/s del/de las ave/s filtrada/s, e informaremos como usar el
# buscador.
with col1:

    # Recorremos el fichero .ods con pd.read_excel.
    # df = pd.read_excel('./Archivos/FichaAvesDefinitiva.ods', engine='odf', usecols='A:N')
    df = pd.read_excel('./pythonProject/venv/AvesApp/Archivos/FichaAvesDefinitiva.ods', engine='odf', usecols='A:N')

    # Implementamos una excepción porque al cargar la página daba un NameError que al inicializar los filtros
    # como cadenas vacías ya no da. No obstante lo dejamos.
    try:
        # Vamos filtrando por cada etiqueta recogiendo la selección anterior
        df = df[df['Ave'].str.contains(nombreAve, case=False)]
        df = df[df['Tamaño'].str.contains(tamanoAve, case=False)]
        df = df[df['Hábitat'].str.contains(habitatAve, case=False)]
        df = df[df['Comportamiento'].str.contains(comportamientoAve, case=False)]
        df = df[df['Color'].str.contains(colorAve, case=False)]
        df = df[df['Patas color'].str.contains(patasColor, case=False)]
        df = df[df['Pico color'].str.contains(picoColor, case=False)]
        df = df[df['Pico forma'].str.contains(picoForma, case=False)]
        df = df[df['Pico grosor'].str.contains(picoGrorsor, case=False)]
        df = df[df['Pico longitud'].str.contains(picoLongitud, case=False)]

    except NameError:
        # Damos información al usuario
        st.write("Para iniciar la identificación hay que elegir algún filtro")

    # Filtramos el dataframe por la columna UrlCantos con los sucesivos filtros
    dfUrlCantos = df.filter(items=['UrlCanto'])
    for valor in dfUrlCantos.values.tolist():
        miarchivo = open('./pythonProject/venv/AvesApp/Archivos/UrlCantos/' + valor[0], 'r', encoding='utf-8')
        contenido = miarchivo.read()
        miarchivo.close()
        if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
                picoGrorsor == picoLongitud == "":
            pass
        else:
            st.write('**_______________________________________________________**')
            #st.write('_Foto:_')
            st.image('./pythonProject/venv/AvesApp/Archivos/FotosDef/' + valor[0] + '.png')
            st.caption(contenido)

    dfImagen = df.filter(items=['Foto'])
    # Convertimos el dfImagen en una lista que recorremos con for para mostrar las fotos de las aves seleccionadas con
    # cada filtro.
    for valor in dfImagen.values.tolist():
        # Si no hay nada seleccionado no se muestra ninguna foto y en caso contrario se muestran las fotos de las
        # aves seleccionadas
        if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
                picoGrorsor == picoLongitud == "":
            pass

    # Sin no hay ningún ave seleccionada se le indica al usuario que con esos filtros no se localiza ningún ave
    if dfImagen.empty:
        st.write("_Con los filtros seleccionados no hay ningún ave en la base de datos._"
                 " _Inténtalo de nuevo._")

# Damos contenido a la columna de la derecha donde irán las fichas de las aves seleccionadas.
with col2:

    # Convertimos el dfFichas en una lista que recorremos con for para mostrar las fichas de las aves seleccionadas con
    # cada filtro
    dfFichas = df.filter(items=['Ficha'])
    for valor in dfFichas.values.tolist():
        # mifichero = open('./Archivos/Fichas/' + valor[0], 'r', encoding='utf-8')
        mifichero = open('./pythonProject/venv/AvesApp/Archivos/Fichas/' + valor[0], 'r', encoding='utf-8')
        texto = mifichero.read()
        mifichero.close()
        # Si no hay nada seleccionado no se muestra ninguna ficha y en caso contrario se muestran las
        # fichas de las aves seleccionadas
        if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
                picoGrorsor == picoLongitud == "":
            pass
        else:
            #st.write('_Ficha:_')
            st.write('**_______________________________________________________**')
            st.caption(texto)
            st.audio('./pythonProject/venv/AvesApp/Archivos/Cantos/' + valor[0] + '.mp3')

    # Filtramos el dataframe por la columna Canto en los sucesivos filtros
    dfAudio = df.filter(items=['Canto'])
    for valor in dfAudio.values.tolist():
        # Si no hay nada seleccionado no se muestra ningun audio y en caso contrario se muestran los audios de las
        # aves seleccionadas
        if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
                picoGrorsor == picoLongitud == "":
            pass
