import pymysql
#ESTABLECE CONEXION
conn = pymysql.connect(host='52.178.107.50', user='xavi', password='12345678', db='BDDPROYECTOENERO')

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
print(crearListaUsuarios())


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
print(crearListaPersonajes())



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

print(crearListaAventuras())



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

print(crearListaSteps())



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

print(crearListaOptions())



