import pymysql
# #ESTABLECE CONEXION
conn = pymysql.connect(host='52.178.107.50', user='xavi', password='12345678', db='BDDPROYECTOENERO')
#
# #CONSULTA
# cur = conn.cursor()
# query = 'select * from ADVENTURE'
#
# cur.execute(query)
#
# #FETCHALL
# rows = cur.fetchall()
# print(type(rows))
# print(rows)

# #FETCHONE
# row1 = cur.fetchone()
# print(type(row1))
# print(row1)

user_name = input('Enter username: ')
passwrd = input('Enter password: ')
cur = conn.cursor()
sql = f"insert into USER (user_name, password, user_create, create_date) values('{user_name}',{passwrd}', current_user(), curdate())"

cur.execute(sql)
conn.commit()

print(cur.rowcount, "record inserted")
conn.close()

nombreusuario = False
while nombreusuario == False:
    usuario = input("Escribe tu nombre de usuario: "))
    if len(usuario) < 6:
        print("El nom de usuari ha de contenir almenys 6 caràcters")
    if len(usuario) > 12:
        print("El nom de usuari no pot contenir més de 12 caràcters")
    if usuario.isalnum() == False:
        print("El nom d'usuari pot contenir només lletres i números")
    if usuario.isalnum() == True and len(usuario)>=6 and len(usuario)<=12:
        print("Tu nombre de usuario es correcto")
        nombreusuario = True