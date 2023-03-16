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
    page_title='Baixominhoaves',
    page_icon=':random:',
    # page_icon=':bird:',
    # page_icon=':owl:',
    layout='wide',
)

# Pomemos el título
st.title("_Buscador De Aves Do Baixo Miño_")
st.caption(
    """
    **Espacio declarado Red Natura 2000 y** 
    **Zona de Especial Protección para las Aves (ZEPA)**.
    https://gl.wikipedia.org/wiki/Rede_Natura_2000  
    **Comarca do Baixo Miño**.
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
    st.write("**_Si no la sabes, sigue las instrucciones:_**")
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
                                                  'Ánade Azulón Hembra',
                                                  'Ánade Azulón Macho',
                                                  'Andarríos Chico',
                                                  'Archibebe Claro',
                                                  'Arrendajo',
                                                  'Avión Común',
                                                  'Azor',
                                                  'Bisbita Común',
                                                  'Buitrón',
                                                  'Camachuelo Común Hembra',
                                                  'Camachuelo Común Macho',
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
                                                  'Curruca Cabecinegra Hembra',
                                                  'Curruca Cabecinegra Macho',
                                                  'Curruca Capirotada Hembra',
                                                  'Curruca Capirotada Macho',
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
                                                  'Faisán Vulgar Hembra',
                                                  'Faisán Vulgar Macho',
                                                  'Focha Común',
                                                  'Fumarel Común',
                                                  'Garceta Común',
                                                  'Garceta Grande',
                                                  'Garcilla Bueyera',
                                                  'Garza Real',
                                                  'Gavilán',
                                                  'Gaviota Argéntea',
                                                  'Gaviota Patiamarilla',
                                                  'Gaviota Reidora',
                                                  'Gaviota Sombría',
                                                  'Golondrina Común',
                                                  'Golondrina Daúrica',
                                                  'Gorrión Común Hembra',
                                                  'Gorrión Común Macho',
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
                                                  'Morito Común',
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
                                                  'Pinzón Real',
                                                  'Pinzón Vulgar Hembra',
                                                  'Pinzón Vulgar Macho',
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
                                                  'Más pequeño que un gorrión',
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
                                                    'Ribera',
                                                    'Urbanos',
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
                            'Rojo',
                            'Verde',
                            ])

    if st.checkbox("Patas color"):
        patasColor = st.selectbox(
            'Elige color patas', ['',
                                  'Amarillo',
                                  'Azul',
                                  'Blanco',
                                  'Crema',
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
# Convertimos el dfFichas en una lista dentro de un archivo que recorremos con for para mostrar las fichas de las aves
# seleccionadas con cada filtro

dfFichas = df.filter(items=['Ficha'])
for valor in dfFichas.values.tolist():
    mifichero = open('./pythonProject/venv/AvesApp/Archivos/Fichas/' + valor[0], 'r', encoding='utf-8')
    texto = mifichero.read()
    mifichero.close()
    if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
            picoGrorsor == picoLongitud == "":
        pass
    else:
        st.image('./pythonProject/venv/AvesApp/Archivos/FotosDef/' + valor[0] + '.png')
        st.caption(texto)
        st.audio('./pythonProject/venv/AvesApp/Archivos/Cantos/' + valor[0] + '.mp3', format='audio/mpeg')
        st.write(
            '**____________________________________________________________________________________________________________**')

# Filtramos el dataframe por la columna Foto en los sucesivos filtros creando una lista
dfImagen = df.filter(items=['Foto'])
# Recorremos la lista dfImagen, si no hay nada seleccionado continuamos y si aparece algo lo mostramos en la línea 333
# para seguir un orden más visual
for valor in dfImagen.values.tolist():
    if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
            picoGrorsor == picoLongitud == "":
        pass

# Filtramos el dataframe por la columna Canto en los sucesivos filtros creando una lista
dfAudio = df.filter(items=['Canto'])
# Cuando no aparecen audios indicamos que hay que volver a seleccionar filtros nuevamente
if dfAudio.empty:
    st.write("_Con los filtros seleccionados no hay ningún ave en la base de datos._"
             " _Inténtalo de nuevo._")
    # Paramos la aplicación para que no aparezca la información de 'Archivos de audios:'
    st.stop()

# Recorremos la lista dfAudio, si no hay nada seleccionado continuamos y si aparece algo lo mostramos en la línea 335
# para seguir un orden  más visual
for valor in dfAudio.values.tolist():
    if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
            picoGrorsor == picoLongitud == "":
        pass

# Convertimos el dfUrlCantos en una lista dentro de un archivo que recorremos con for para mostrar las fichas de las aves
# seleccionadas con cada filtro
dfUrlCantos = df.filter(items=['UrlCanto'])
if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
            picoGrorsor == picoLongitud == "":
    pass
else:
    st.write('Archivos de audios:')
for valor in dfUrlCantos.values.tolist():
    miarchivo = open('./pythonProject/venv/AvesApp/Archivos/UrlCantos/' + valor[0], 'r', encoding='utf-8')
    contenido = miarchivo.read()
    miarchivo.close()
    # Recorremos la lista dfImagen, si no hay nada seleccionado continuamos y si aparece algo lo mostramos
    if nombreAve == tamanoAve == habitatAve == comportamientoAve == colorAve == patasColor == picoColor == picoForma == \
            picoGrorsor == picoLongitud == "":
        pass
    else:
        st.caption(contenido)
    
   
