import pymysql
#ESTABLECE CONEXION
conn = pymysql.connect(host='52.178.107.50', user='xavi', password='12345678', db='BDDPROYECTOENERO')



#Diccionario Usuarios

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
print(users)



#Diccionario personajes

query = 'select * from BDDPROYECTOENERO.CHARACTER'
cur.execute(query)
rows = cur.fetchall()

characters = {}
for id in range(1,len(rows)+1):
    infoCharacter = []
    for item in rows[id-1]:
        infoCharacter.append(item)
    characters[id] = infoCharacter[1:]

print(characters)



#Diccionario Aventuras

query = 'select * from ADVENTURE'
cur.execute(query)
rows = cur.fetchall()

adventures = {}
for id in range(1,len(rows)+1):
    infoAdventure = []
    for item in rows[id-1]:
        infoAdventure.append(item)
    adventures[id] = infoAdventure[1:]

print(adventures)



#Diccionario Steps

query = 'select * from STEP'
cur.execute(query)
rows = cur.fetchall()

steps = {}
for id in range(1,len(rows)+1):
    infoStep = []
    for item in rows[id-1]:
        infoStep.append(item)
    steps[id] = infoStep[1:]

print(steps)



#Diccionario Options

query = 'select * from BDDPROYECTOENERO.OPTION'
cur.execute(query)
rows = cur.fetchall()

options = {}
for id in range(1,len(rows)+1):
    infoOption = []
    for item in rows[id-1]:
        infoOption.append(item)
    options[id] = infoOption[1:]

print(options)



#Diccionario