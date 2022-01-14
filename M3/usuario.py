import pymysql
#ESTABLECE CONEXION
conn = pymysql.connect(host='52.178.107.50', user='xavi', password='12345678', db='BDDPROYECTOENERO')

#CONSULTA
cur = conn.cursor()
query = 'select * from USER'

cur.execute(query)

#FETCHALL
rows = cur.fetchall()

users = {}
for id in range(1,len(rows)+1):
    infoUsuario = []
    for item in rows[id-1]:
        infoUsuario.append(item)
    users[id] = infoUsuario[1:]

print(users[1][0])




