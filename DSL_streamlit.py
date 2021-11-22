import streamlit as st

st.title("Primera idea DSL")

st.markdown(
    """
    ### Keywords:
    - Player
    - Team
    - Game
    - Manager
    - Referee
    """)

st.header("Definicion de cada tipo")
st.subheader("Player")
with st.echo():
    player = {
        #required
        'name':"", # str
        'position':"", # DEL, MC, DEF or GK
        'media':"", # int
        #optional
        'age':"", # int
        'potencial':"", # int
        'country':"", # str
        'team':"", # str
        'DEF':"", # int 
        'MC':"", # int
        'DEF':"", # int
        'status':"" # available, injured or sanctioned
    }

st.subheader("Team")
with st.echo():
    team = {
        #required
        'name':"", # str
        'player':"", # list of player
        'manager':"", # manager
        'country':"", # str
        #optional
        'stadium':"", # str
    }

st.subheader("Game")
with st.echo():
    game = {
        #required
        'team1':"", # Team
        'team2':"", # Team
        'stadium':"", # str
        'referee':"", # list of referee
        #optional
        'weather':"", # str
        'date':"", # date
    }

st.subheader("Manager")
with st.echo():
    manager = {
        #required
        'name':"", # str
        'team':"", # str
        'experience':"", # int
        #optional
        'country':"", # str
        'age':"", # int
    }

st.subheader("Referee")
with st.echo():
    referee = {
        #required
        'name':"", # str
        'experience':"", # int
        #optional
        'country':"", # str
        'age':"", # int
    }

st.header("Ejemplo de sintaxis")
st.subheader("Inicializacion:")
st.code(
    """
    #Inicializacion de un player
    player p1 ( args );

    #Inicializacion de un team
    team t1 ( args );

    #Inicializacion de un game
    game g1 ( args );
    """)

st.subheader("Declaracion de listas:")
st.code(
    "player p [ p1, p2, p3, .... ]"
)

st.subheader("Indexacion en listas:")
st.code(
    """
    p[0] # se accede al elemento 0 de la lista p
    #p[-1] devuelve el ultimo elemento del array, si hacemos p[-2] devuelve el penultimo
    #p[23] en este caso hace 23%(p.length) y cae siempre en una posicion dentro del array
    """
)

st.subheader("Asignacion")
st.code(
    """
    p1 -> p2 # se le asigna a p2 el valor de p1
    """
)

st.subheader("Acceso a propiedades")
st.code("player.name # se accede a la propiedad name de player")

st.subheader("for")
st.code(
    """
    for item in t.player:
        ...
    """
)

st.subheader("Filtrar por una propiedad")
st.code(
    """
    filter t.players by (_.age > 20) # devuelve todo los jugadores mayores de 20 años de un equipo
    """
)

st.subheader("Condicionales")
st.code(
    """
    if <condicion> : { }
    if <condicion> : { } else { }
    """
)

st.subheader("Operadores logicos")
st.code("OR AND NOT")

st.subheader("Definicion de funciones")
st.code(
    """
    function type id (args) { }
    #En caso de ser void se representa el type con _
    """
)

st.subheader("Variables constantes")
st.code("const type id")

st.subheader("Equipos predeterminados")
st.code("TEAM.barcelona # devuelve una plantilla con el equipo del barcelona")

