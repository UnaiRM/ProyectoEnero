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


#Diccionario personajes
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

#Diccionario Aventuras
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
        steps[id] = infoStep[1:]

    return steps



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


def get_answers_bystep_adventure(id_adventure):
    idAnswers_ByStep_Adventure = {}
    pasos = crearListaSteps()
    for step in range(1,len(pasos)+1):
        paso = pasos[step]
        if paso[0] == id_adventure:
            idAnswers_ByStep_Adventure[len(idAnswers_ByStep_Adventure)+1] = paso
    return idAnswers_ByStep_Adventure

print(get_answers_bystep_adventure(1))

