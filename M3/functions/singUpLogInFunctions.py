import functions.createDictFunctions as dictCreate

users = dictCreate.crearListaUsuarios()
listaNombreUsuarios = []
for username in range(1,len(users)+1):
    listaNombreUsuarios.append(users[username][0])

def userExists(user):
    if user in listaNombreUsuarios:
        return True
    else:
        return False

def checkUser(user):
    nombreUsuarioValido = False
    if len(user) < 6:
        print("El nombre de usuario tiene que contener por lo menos 6 caracteres")
        return nombreUsuarioValido
    if len(user) > 10:
        print("El nombre de usuario no puede contener mas de 10 caracteres")
        return nombreUsuarioValido
    if not user.isalnum():
        print("El nombre de usuario solo puede tener letras y numeros")
        return nombreUsuarioValido
    if userExists(user):
        print("Su nombre de usuario actualmente esta usado, porfavor elija otro")
        return nombreUsuarioValido
    else:
        nombreUsuarioValido = True
        print("Su nombre de usuario es correcto y no esta en la base de datos!")
        return nombreUsuarioValido

def checkPassword(password):
    esNumero = False
    esLetra = False
    esMinuscula = False
    esMayuscula = False
    noEsAlphaNumerico = False
    noEsEspacio = False
    noEsCorta = False
    noEsLarga = False
    passwordValida = False
    if len(password) >= 8:
        noEsCorta = True
    if len(password) <= 12:
        noEsLarga = True
    if password.find(" ") == -1:
        noEsEspacio = True
    for letra in password:
        if letra.isnumeric():
            esNumero = True
        if not letra.isalnum():
            noEsAlphaNumerico = True
        if letra.isalpha():
            esLetra = True
        if letra.isupper():
            esMayuscula = True
        if letra.islower():
            esMinuscula = True
        if (noEsEspacio == True and noEsCorta == True and noEsLarga == True and esMinuscula == True and esMayuscula == True and esLetra == True and noEsAlphaNumerico == True and esNumero == True):
            passwordValida = True
            print("Password correcta, todo en orden!")
            return passwordValida
    if passwordValida == False:
        print("La password escogida no es segura, comprueba que tenga numeros, mayusculas, minusculas, un caracter especial y no tenga espacios, como minimo debe tener 8 caracteres y como maximo 12")
        return passwordValida

