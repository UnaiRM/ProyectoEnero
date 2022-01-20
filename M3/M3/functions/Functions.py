import pymysql
<<<<<<< HEAD

=======
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0
#ESTABLECE CONEXION
conn = pymysql.connect(host='52.178.107.50', user='xavi', password='12345678', db='BDDPROYECTOENERO')

#Diccionario Usuarios
def DictUsers():
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
<<<<<<< HEAD
=======
    print(crearListaUsuarios())
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0


#Diccionario personajes
def DictCharacters():
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
<<<<<<< HEAD
=======
    print(crearListaPersonajes())
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0



#Diccionario Aventuras
def DictAdventures():
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

<<<<<<< HEAD
=======
    print(crearListaAventuras())



#Diccionario Steps
def DictSteps():
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


>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0

#Diccionario Options
def DictOptions():
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

<<<<<<< HEAD

def InsertUser(user, password):
    cur = conn.cursor()
    sql = f"insert into USER (user_name, password, user_create, create_date) values('{user}','{password}', 'current_user()', current_time())"
=======
    print(crearListaOptions())

def InsertUser(user, password):
    cur = conn.cursor()
    sql = f"insert into USER (user_name, password, user_create, create_date) values('{user}','{password}', 'current_user()', curdate())"
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0

    cur.execute(sql)
    conn.commit()

    print("Se ha creado correctamente el usuario: {} con password: {}".format(user, password))
<<<<<<< HEAD

def insertCurrentGame(idCharacter,idUser,idAdventure):
    cur = conn.cursor()
    sql = f"insert into GAME (id_character, id_user, id_adventure, user_create, create_date, date) values('{idCharacter}','{idUser}', '{idAdventure}',current_user(), current_time(), current_time())"
=======
    conn.close()

def insertCurrentGame(idCharacter,idUser,idAdventure):
    cur = conn.cursor()
    sql = f"insert into GAME (id_character, id_user, id_adventure, user_create, create_date, date) values('{idCharacter}','{idUser}', '{idAdventure}',current_user(), curdate(), curdate())"
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0
    cur.execute(sql)
    conn.commit()

    print("Se ha creado correctamente el Game en la base de datos")
<<<<<<< HEAD
=======
    conn.close()
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0

#FUNCIONES DICCIONARIOS

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


#Diccionario personajes / get_characters()
def get_characters():
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

#Diccionario Aventuras / get_adventures_with_chars()?
<<<<<<< HEAD
def get_adventures_with_chars(id_character):
=======
def get_adventures_with_chars():
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0
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




#Diccionario Steps
<<<<<<< HEAD
def DictSteps():
=======
def crearListaSteps():
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0
    cur = conn.cursor()
    query = 'select * from STEP'
    cur.execute(query)
    rows = cur.fetchall()
    steps = {}
    for id in range(1,len(rows)+1):
        infoStep = []
        for item in rows[id-1]:
            infoStep.append(item)
        steps[id] = infoStep
    return steps

<<<<<<< HEAD
=======

>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0
#Diccionario Steps
def crearListaHistorial():
    cur = conn.cursor()
    query = 'select * from BDDPROYECTOENERO.HISTORY'
    cur.execute(query)
    rows = cur.fetchall()
    history = {}
    for id in range(1,len(rows)+1):
        infoGame = []
        for item in rows[id-1]:
            infoGame.append(item)
        history[id] = infoGame
    return history


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
<<<<<<< HEAD
        options[id] = infoOption

    return options
print(crearListaOptions())
=======
        options[id] = infoOption[1:]

    return options

>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0

#Diccionario Games
def crearListaGames():
    cur = conn.cursor()
    query = 'select * from BDDPROYECTOENERO.GAME'
    cur.execute(query)
    rows = cur.fetchall()

    games = {}
    for id in range(1,len(rows)+1):
        infoGame = []
        for item in rows[id-1]:
            infoGame.append(item)
        games[id] = infoGame[1:]

    return games


def get_id_bystep_adventure(id_adventure):
    idAnswers_ByStep_Adventure = {}
<<<<<<< HEAD
    pasos = DictSteps()
=======
    pasos = crearListaSteps()
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0
    for step in range(1,len(pasos)+1):
        paso = pasos[step]
        if paso[1] == id_adventure:
            idAnswers_ByStep_Adventure[len(idAnswers_ByStep_Adventure)+1] = paso
    return idAnswers_ByStep_Adventure




def get_answers_bystep_adventure(id_adventure):
    listaStepsDeAventura = get_id_bystep_adventure(id_adventure)
    listaDeOpciones = crearListaOptions()
    listaIdSteps = []
    listaOpcionesEnAventura = []
    for step in range(1,len(listaStepsDeAventura)+1):
        listaIdSteps.append((listaStepsDeAventura[step][0]))
    for idStep in listaIdSteps:
        for idOption in range(1,len(listaDeOpciones)+1):
            if idStep == listaDeOpciones[idOption][1]:
                listaOpcionesEnAventura.append(listaDeOpciones[idOption])
    return listaOpcionesEnAventura

<<<<<<< HEAD
print(get_answers_bystep_adventure(1))

=======
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0


def get_first_step_adventure(id_adventure):
    pasos = get_id_bystep_adventure(id_adventure)
    primerPaso = pasos[1]
    return primerPaso

<<<<<<< HEAD
=======

>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0
def getChoices(id_relife):
    history = crearListaHistorial()
    partida = []
    for idHistory in range(1,len(history)+1):
        if history[idHistory][1] == id_relife:
            step = history[idHistory][3]
            option = history[idHistory][2]
            tupla = (step,option)
            partida.append(tupla)
    partida = tuple(partida)
    return partida


def getIdGames():
    listaIdGames = []
    listaDeGames = crearListaGames()
    for id in range(1,len(listaDeGames)+1):
        listaIdGames.append(listaDeGames[id][0])
    return listaIdGames


def getUsers():
    diccionarioUsuarios = crearListaUsuarios()
    usuarios = {}
    for user in range(1,len(diccionarioUsuarios)+1):
        usuarios[diccionarioUsuarios[user][0]] = {'password':diccionarioUsuarios[user][1], 'idUser':user}
    return usuarios

def getHeader(texto):
    print("")
    print('*'*70)
    print(str(texto).center(70,'='))
    print('*'*70)

def nicknameList():
    users = DictUsers()
    listaNombreUsuarios = []
    for username in range(1,len(users)+1):
        listaNombreUsuarios.append(users[username][0])
    return listaNombreUsuarios
def passwordList():
    passwords = DictUsers()
    listaPasswords = []
    for password in range(1, len(passwords) + 1):
        listaPasswords.append(passwords[password][1])
    return listaPasswords
def userExists(user):
    listaNombreUsuarios = nicknameList()
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

def gameTitle():
    print("**********************************************************************")
    print("                 #######                                              ")
    print("                 #       #      #  ####  ######                       ")
    print("                 #       #      # #    # #                            ")
    print("                 #####   #      # #      #####                        ")
    print("                 #       #      # #  ### #                            ")
    print("                 #       #      # #    # #                            ")
    print("                 ####### ###### #  ####  ######                       ")
    print("                                                                      ")
    print("                           ##### #    #                               ")
    print("                             #   #    #                               ")
    print("                             #   #    #                               ")
    print("                             #   #    #                               ")
    print("                             #   #    #                               ")
    print("                             #    ####                                ")
    print("                                                                      ")
    print("             #    # #  ####  #####  ####  #####  #   ##               ")
    print("             #    # # #        #   #    # #    # #  #  #              ")
    print("             ###### #  ####    #   #    # #    # # #    #             ")
    print("             #    # #      #   #   #    # #####  # ######             ")
    print("             #    # # #    #   #   #    # #   #  # #    #             ")
    print("             #    # #  ####    #    ####  #    # # #    #             ")
    print("**********************************************************************")

<<<<<<< HEAD
def GetOpt(textOpts,inputOptText="",rangeList=[],exceptions=[]):
    while True:
        print()
        for texto in textOpts:
            print(" ".rjust(31)+str(texto))
        opc = input(inputOptText)
=======
def GetOpt(textOpts="",inputOptText="",rangeList=[],exceptions=[]):
    while True:
        print(textOpts)
        opc = (input(inputOptText))
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0
        if opc not in rangeList and opc not in exceptions:
            print("*"*5,"Invalid Option","*"*5)
            input("Press enter to continue")
        else:
            return opc

def checkUserbdd(user,password):
    listaUsuarios = nicknameList()
    for i in getUsers():
        if user in listaUsuarios:
            if password == getUsers()[user]["password"]:
                return 1
            else:
                return -1
        else:
            return 0
<<<<<<< HEAD
def character_list():
    characters = get_characters()
    for character in characters:
        print("{}) {}".format(character,characters[character][0]))


def character_ID_list():
    characters = get_characters()
    listaID = []
    for character in characters:
        listaID.append(str(character))
    return listaID


def Dict_Char_Adv():
    cur = conn.cursor()
    query = 'select * from CHARACTER_ADVENTURE'
    cur.execute(query)
    rows = cur.fetchall()

    characterInAdventure = {}
    for id in range(1,len(rows)+1):
        infoCharInAdv = []
        for item in rows[id-1]:
            infoCharInAdv.append(item)
        characterInAdventure[id] = infoCharInAdv
    return characterInAdventure


def adventuresForCharacter(id_character):
    aventuras = DictAdventures()
    aventurasParaCaracter = Dict_Char_Adv()
    for item in range(1,len(aventurasParaCaracter)+1):
        if id_character == aventurasParaCaracter[item][0]:
            print('{}) {}'.format(aventurasParaCaracter[item][1],aventuras[aventurasParaCaracter[item][1]][0]))

def adventuresIdForCharacter(id_character):
    aventurasParaCaracter = Dict_Char_Adv()
    listaAventuras = []
    for item in range(1, len(aventurasParaCaracter) + 1):
        if id_character == aventurasParaCaracter[item][0]:
            listaAventuras.append(aventurasParaCaracter[item][1])
    return listaAventuras


def selectUserID(username):
    usuarios = DictUsers()
    for IDuser in range(1,len(usuarios)+1):
        if username == usuarios[IDuser][0]:
            id_user = IDuser
    return id_user



def getOptionsForStep(id_step):
    options = crearListaOptions()
    optionList = []
    for id_option in range(1, len(options)):
        if options[id_option][2] == id_step:
            print('{}) {}'.format(options[id_option][0], options[id_option][3]))
            optionList.append(options[id_option][0])
    return optionList

print(getOptionsForStep(1))



=======
>>>>>>> b094fd17872c6aa3f40a759b7d4b6e176a98e1c0
