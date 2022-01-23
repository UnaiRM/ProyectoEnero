import pymysql
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


def InsertUser(user, password):
    cur = conn.cursor()
    sql = f"insert into USER (user_name, password, user_create, create_date) values('{user}','{password}', current_user(), current_time())"

    cur.execute(sql)
    conn.commit()
    print("Se ha creado correctamente el usuario: {} con password: {}".format(user, password))

def insertCurrentGame(idCharacter,idUser,idAdventure):
    cur = conn.cursor()
    sql = f"insert into GAME (id_character, id_user, id_adventure, user_create, create_date, date) values('{idCharacter}','{idUser}', '{idAdventure}',current_user(), current_time(), current_time())"
    cur.execute(sql)
    conn.commit()

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
def get_adventures_with_chars(id_character):
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
        steps[id] = infoStep
    return steps
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
        options[id] = infoOption

    return options

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
        games[id] = infoGame

    return games


def get_id_bystep_adventure(id_adventure):
    idAnswers_ByStep_Adventure = {}
    pasos = DictSteps()
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




def get_first_step_adventure(id_adventure):
    pasos = get_id_bystep_adventure(id_adventure)
    primerPaso = pasos[1]
    return primerPaso

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
    print('*'*119)
    print(str(texto).center(119,'='))
    print('*'*119)

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

def GetOpt(textOpts,inputOptText="",rangeList=[],exceptions=[]):
    while True:
        print()
        for texto in textOpts:
            print(" ".rjust(28)+str(texto))
        opc = input(inputOptText)
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

def character_list():
    characters = get_characters()
    for character in characters:
        print(" ".rjust(28) + "{}) {}".format(character,characters[character][0]))


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

def adventuresForCharacter(adventures):
    aventuras = DictAdventures()
    aventurasParaCaracter = {}
    for i in range(len(aventuras)+1):
        if i in adventures:
            aventurasParaCaracter[i] = aventuras[i]
    return aventurasParaCaracter

def adventuresIdForCharacter(id_character):
    aventurasParaCaracter = Dict_Char_Adv()
    listaAventuras = []
    for item in range(1, len(aventurasParaCaracter)+1):
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
            print("{}) {}".format(options[id_option][0], options[id_option][3]))
            print()
            optionList.append(str(options[id_option][0]))
    return optionList


def getNextStep(id_option):
    options = crearListaOptions()
    for id in range(1, len(options)+1):
        if id_option == options[id][0]:
            id_next_step = options[id][1]
    return id_next_step


def endGame():
    print(' ********   **     ****     **')
    print('/**/////   /**    /**/**   /**')
    print('/**        /**    /**//**  /**')
    print('/*******   /**    /** //** /**')
    print('/**////    /**    /**  //**/**')
    print('/**        /**    /**   //****')
    print('/**        /**    /**    //***')
    print('//         //     //      /// ')


def InsertHistory(gameId, stepId, optionId):
    cur = conn.cursor()
    sql = f"insert into BDDPROYECTOENERO.HISTORY (id_game, id_step, id_option, user_create, create_date) values('{gameId}','{stepId}', '{optionId}',current_user(), current_time())"
    cur.execute(sql)
    conn.commit()

def getFormatedAdventure(adventures):
    print("Adventures".center(200, "="))
    print("")
    print("IdAdventure", "Adventure".rjust(10), "Description".rjust(55))
    print("".center(200, "*"))
    for i in adventures:
        print(str(i).ljust(13), str(adventures[i][0]).ljust(53), adventures[i][1])


def InsertLastHistory(gameId, stepId):
    cur = conn.cursor()
    sql = f"insert into BDDPROYECTOENERO.HISTORY (id_game, id_step, user_create, create_date) values('{gameId}','{stepId}',current_user(), current_time())"
    cur.execute(sql)
    conn.commit()


def play(user):
    print("Characters: ")
    user_id = selectUserID(user)
    character_list()
    print(" ".rjust(28) + "0) Go to menu")
    chossed_character = input("Choose your Character ID: ")
    characterIdList = character_ID_list()
    while chossed_character not in characterIdList and chossed_character != "0":
        print('Incorrect ID')
        chossed_character = input("Choose your Character ID: ")
    if chossed_character == "0":
        opc = 5
        return
    getHeader(get_characters()[int(chossed_character)][0])
    input("Press enter to continue")
    print("Adventures: ")
    adventure_character_list = adventuresIdForCharacter(int(chossed_character))
    getFormatedAdventure(adventuresForCharacter(adventure_character_list))
    print("0".ljust(14)+"Go to menu")
    chossed_adventure = input("Choose your adventure ID: ")
    while int(chossed_adventure) not in adventure_character_list and chossed_adventure != "0":
        print('Incorrect ID')
        chossed_character = input("Choose your adventure ID: ")
    if chossed_adventure == "0":
        opc = 5
        return
    insertCurrentGame(chossed_character, user_id, chossed_adventure)
    pasoFinal = 0
    id_adventure = int(chossed_adventure)
    print(get_first_step_adventure(id_adventure)[3])
    id_step = get_first_step_adventure(id_adventure)[0]
    id_game = getIdGames()[len(getIdGames()) - 1]
    options = crearListaOptions()
    while pasoFinal != 1:
        listaIdOpciones = getOptionsForStep(id_step)
        optionChoosed = input("Choose your option")
        print("*" * 70)
        while optionChoosed not in listaIdOpciones:
            print("Incorrect option")
            optionChoosed = input("Please choose your option again")
        optionChoosed = int(optionChoosed)
        print(options[optionChoosed][3])
        print()
        InsertHistory(id_game, id_step, optionChoosed)
        id_step = getNextStep(optionChoosed)
        actualStep = DictSteps()[id_step][3]
        print(actualStep)
        pasoFinal = DictSteps()[id_step][2]
    InsertLastHistory(id_game, id_step)
    input("Press enter to continue")
    endGame()
    input("Press enter to continue")

def getHistoryByGame(id_game):
    historial = crearListaHistorial()
    historia = []
    for i in range(1,len(historial)):
        if historial[i][1] == id_game:
            historia.append(historial[i])
    return historia


def replay():
    games = crearListaGames()
    id_games = getIdGames()
    users = crearListaUsuarios()
    adventures = DictAdventures()
    characters = DictCharacters()
    steps = DictSteps()
    options = DictOptions()
    print("="*119)
    print("Id".ljust(10) + "Username".ljust(15) + "Name".ljust(55) + "CharacterName".ljust(20)+"Date".ljust(25))
    print("*" * 119)
    for game in range(len(games),0,-1):
        print("{})".format(game).ljust(10) + "{}".format(users[games[game][2]][0]).ljust(15) + "{}".format(adventures[games[game][3]][0]).ljust(55) + "{}".format(characters[games[game][1]][0]).ljust(20) + "{}".format(games[game][6]))
    print()
    print("0)".ljust(10) + "Go back")
    gameChoosed = input("Choose a game by id")
    while int(gameChoosed) not in id_games and gameChoosed != "0":
        print("Invalid id, please enter a valid id")
        gameChoosed = input("Choose a game by id")
    if gameChoosed == "0":
        return
    else:
        getHeader(adventures[games[int(gameChoosed)][3]][0])
        historial = getHistoryByGame(int(gameChoosed))
        print(historial)
        for i in range(len(historial)):
            input("Press enter to continue")
            print(steps[historial[i][2]][3])
            if steps[historial[i][2]][2] == 1:
                break
            print()
            getOptionsForStep(historial[i][2])
            input("Press enter to continue")
            print("You have been selected number {}".format(historial[i][3]))
            print(options[historial[i][3]][2])
            print()
            print(options[historial[i][3]][3])
        endGame()




