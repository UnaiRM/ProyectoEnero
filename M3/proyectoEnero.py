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