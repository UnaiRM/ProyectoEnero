import functions.singUpLogInFunctions as logSign
import functions.insertInDBB as ins

def createUser():
    passwordValida = False
    nombreUsuarioValido = False
    while nombreUsuarioValido == False:
        user = input("Dime tu nombre de usuario")
        nombreUsuarioValido = logSign.checkUser(user)
    while passwordValida == False:
        password = input("Dime tu password")
        passwordValida = logSign.checkPassword(password)
    ins.insertarUsuario(user,password)

createUser()




