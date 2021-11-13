import streamlit as st

st.title("Primera idea DLS")

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
        'DEF':"" # int
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

st.header("Ejemplo de sintaxis")
st.code(
    """
    #Inicializacion de un player
    player a ( args);

    #Inicializacion de un team
    team a ( args);

    #Inicializacion de un game
    game eq1 vs eq2
    in std1
    referee [r1, r2, r3, r4]
    weather w;
    """)


