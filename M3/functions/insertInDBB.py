import pymysql
#ESTABLECE CONEXION
conn = pymysql.connect(host='localhost', user='Unai', password='admin123', db='BDDPROYECTOENERO')

def insertarUsuario(user, password):
    cur = conn.cursor()
    sql = f"insert into USER (user_name, password, user_create, create_date) values('{user}','{password}', current_user(), curdate())"

    cur.execute(sql)
    conn.commit()

    print("Se ha creado correctamente el usuario: {} con password: {}".format(user, password))
    conn.close()