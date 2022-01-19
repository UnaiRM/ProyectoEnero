import pymysql
#ESTABLECE CONEXION
conn = pymysql.connect(host='52.178.107.50', user='xavi', password='12345678', db='BDDPROYECTOENERO')
import functions.Functions as func
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
def getUsers():
    diccionarioUsuarios = crearListaUsuarios()
    usuarios = {}
    for user in range(1,len(diccionarioUsuarios)+1):
        usuarios[diccionarioUsuarios[user][0]] = {'password':diccionarioUsuarios[user][1], 'idUser':user}
    return usuarios
print(getUsers())



def checkUserbdd(user,password):
    listaUsuarios = func.nicknameList()
    for i in getUsers():
        if user in listaUsuarios:
            if password == getUsers()[user]["password"]:
                return 1
            else:
                return -1
        else:
            return 0

print(checkUserbdd("Unai", "124345"))