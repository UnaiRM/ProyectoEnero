import pymysql
#ESTABLECE CONEXION
conn = pymysql.connect(host='localhost', user='Unai', password='admin123', db='BDDPROYECTOENERO')

#Diccionario Usuarios
def crearListaUsuarios():
    cur = conn.cursor()
    query = 'select * from USER'
    cur.execute(query)
    rows = cur.fetchall()

    users = {}
    for id in range(1,len(rows)+1):
        infoUsuario = []
        for item in rows[id-1]:
            infoUsuario.append(item)
        users[id] = infoUsuario[1:]
    return users


#Diccionario personajes / get_characters()
def crearListaPersonajes():
    cur = conn.cursor()
    query = 'select * from BDDPROYECTOENERO.CHARACTER'
    cur.execute(query)
    rows = cur.fetchall()

    characters = {}
    for id in range(1,len(rows)+1):
        infoCharacter = []
        for item in rows[id-1]:
            infoCharacter.append(item)
        characters[id] = infoCharacter[1:]

    return characters

#Diccionario Aventuras / get_adventures_with_chars()?
def crearListaAventuras():
    cur = conn.cursor()
    query = 'select * from ADVENTURE'
    cur.execute(query)
    rows = cur.fetchall()

    adventures = {}
    for id in range(1,len(rows)+1):
        infoAdventure = []
        for item in rows[id-1]:
            infoAdventure.append(item)
        adventures[id] = infoAdventure[1:]

    return adventures




#Diccionario Steps
def crearListaSteps():
    cur = conn.cursor()
    query = 'select * from STEP'
    cur.execute(query)
    rows = cur.fetchall()
    steps = {}
    for id in range(1,len(rows)+1):
        infoStep = []
        for item in rows[id-1]:
            infoStep.append(item)
        steps[id] = infoStep
    return steps


#Diccionario Steps
def crearListaHistorial():
    cur = conn.cursor()
    query = 'select * from BDDPROYECTOENERO.HISTORY'
    cur.execute(query)
    rows = cur.fetchall()
    history = {}
    for id in range(1,len(rows)+1):
        infoGame = []
        for item in rows[id-1]:
            infoGame.append(item)
        history[id] = infoGame
    return history


#Diccionario Options
def crearListaOptions():
    cur = conn.cursor()
    query = 'select * from BDDPROYECTOENERO.OPTION'
    cur.execute(query)
    rows = cur.fetchall()

    options = {}
    for id in range(1,len(rows)+1):
        infoOption = []
        for item in rows[id-1]:
            infoOption.append(item)
        options[id] = infoOption[1:]

    return options


#Diccionario Games
def crearListaGames():
    cur = conn.cursor()
    query = 'select * from BDDPROYECTOENERO.GAME'
    cur.execute(query)
    rows = cur.fetchall()

    games = {}
    for id in range(1,len(rows)+1):
        infoGame = []
        for item in rows[id-1]:
            infoGame.append(item)
        games[id] = infoGame[1:]

    return games


def get_id_bystep_adventure(id_adventure):
    idAnswers_ByStep_Adventure = {}
    pasos = crearListaSteps()
    for step in range(1,len(pasos)+1):
        paso = pasos[step]
        if paso[1] == id_adventure:
            idAnswers_ByStep_Adventure[len(idAnswers_ByStep_Adventure)+1] = paso
    return idAnswers_ByStep_Adventure




def get_answers_bystep_adventure(id_adventure):
    listaStepsDeAventura = get_id_bystep_adventure(id_adventure)
    listaDeOpciones = crearListaOptions()
    listaIdSteps = []
    listaOpcionesEnAventura = []
    for step in range(1,len(listaStepsDeAventura)+1):
        listaIdSteps.append((listaStepsDeAventura[step][0]))
    for idStep in listaIdSteps:
        for idOption in range(1,len(listaDeOpciones)+1):
            if idStep == listaDeOpciones[idOption][1]:
                listaOpcionesEnAventura.append(listaDeOpciones[idOption])
    return listaOpcionesEnAventura



def get_first_step_adventure(id_adventure):
    pasos = get_id_bystep_adventure(id_adventure)
    primerPaso = pasos[1]
    return primerPaso


def getChoices(id_relife):
    history = crearListaHistorial()
    partida = []
    for idHistory in range(1,len(history)+1):
        if history[idHistory][1] == id_relife:
            step = history[idHistory][3]
            option = history[idHistory][2]
            tupla = (step,option)
            partida.append(tupla)
    partida = tuple(partida)
    return partida


def getIdGames():
    listaIdGames = []
    listaDeGames = crearListaGames()
    for id in range(1,len(listaDeGames)+1):
        listaIdGames.append(listaDeGames[id][0])
    return listaIdGames


def getUsers():
    diccionarioUsuarios = crearListaUsuarios()
    usuarios = {}
    for user in range(1,len(diccionarioUsuarios)+1):
        usuarios[diccionarioUsuarios[user][0]] = {'password':diccionarioUsuarios[user][1], 'idUser':user}
    return usuarios



