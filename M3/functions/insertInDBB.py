import pymysql
#ESTABLECE CONEXION
conn = pymysql.connect(host='localhost', user='Unai', password='admin123', db='BDDPROYECTOENERO')

def insertarUsuario(user, password):
    cur = conn.cursor()
    sql = f"insert into USER (user_name, password, user_create, create_date) values('{user}','{password}', 'current_user()', curdate())"

    cur.execute(sql)
    conn.commit()

    print("Se ha creado correctamente el usuario: {} con password: {}".format(user, password))
    conn.close()

def insertCurrentGame(idCharacter,idUser,idAdventure):
    cur = conn.cursor()
    sql = f"insert into GAME (id_character, id_user, id_adventure, user_create, create_date, date) values('{idCharacter}','{idUser}', '{idAdventure}',current_user(), curdate(), curdate())"
    cur.execute(sql)
    conn.commit()

    print("Se ha creado correctamente el Game en la base de datos")
    conn.close()
