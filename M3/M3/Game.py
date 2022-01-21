import functions.Functions as fnc
opc = 5

while opc != 4:
    fnc.gameTitle()
    txt = ("1)Login","2)Create user","3)Show adventures","4)Exit")
    opt = "\nChoose your Option:"
    lista = ["1","2","3","4"]
    exc = []
    opc = fnc.GetOpt(txt, opt, lista, exc)
    while opc == "1":
        LoginCheck = 0
        fnc.getHeader("Login")
        while LoginCheck != 1:
            user = input("Username: ")
            passwd = input("Password: ")
            LoginCheck = fnc.checkUserbdd(user,passwd)
            if LoginCheck == -1:
                print("Incorrect Password")
            if LoginCheck == 0:
                print("User not found")
            if LoginCheck == 1:
                print("Login Correct,", user)
                input("Press Enter to start the game")
                user_id = fnc.selectUserID(user)
                fnc.character_list()
                print("0) Log Out")
                chossed_character = input("Choose your Character ID: ")
                characterIdList = fnc.character_ID_list()
                while chossed_character not in characterIdList and chossed_character != "0":
                    print('Incorrect ID')
                    chossed_character = input("Choose your Character ID: ")
                if chossed_character == "0":
                    opc = 5
                    break
                fnc.getHeader(fnc.get_characters()[int(chossed_character)][0])
                input("Press enter to continue")
                fnc.adventuresForCharacter(int(chossed_character))
                print("0) Log Out")
                chossed_adventure = input("Choose your adventure ID: ")
                adventure_character_list = fnc.adventuresIdForCharacter(int(chossed_character))
                while int(chossed_adventure) not in adventure_character_list and chossed_adventure != "0":
                    print('Incorrect ID')
                    chossed_character = input("Choose your adventure ID: ")
                if chossed_adventure == "0":
                    opc = 5
                    break
                fnc.insertCurrentGame(chossed_character,user_id,chossed_adventure)
                pasoFinal = 0
                id_adventure = int(chossed_adventure)
                print(fnc.get_first_step_adventure(id_adventure)[3])
                id_step = fnc.get_first_step_adventure(id_adventure)[0]
                while pasoFinal != 1:
                    listaIdOpciones = fnc.getOptionsForStep(id_step)
                    optionChoosed = input("Choose your option")
                    while optionChoosed not in listaIdOpciones:
                        print("Incorrect option")
                        optionChoosed = input("Please choose your option again")
                    optionChoosed = int(optionChoosed)
                    id_step = fnc.getNextStep(optionChoosed)
                    actualStep = fnc.DictSteps()[id_step][3]
                    print(actualStep)
                    pasoFinal = fnc.DictSteps()[id_step][2]
                fnc.endGame()
                input("Press enter to continue")




        break


    if opc =="2":
        fnc.getHeader("Create User")
        nombreUsuarioValido = False
        passwordValida = False
        while nombreUsuarioValido == False:
            Username = input("Write your new user: ")
            nombreUsuarioValido = fnc.checkUser(Username)
        while passwordValida == False:
            Password = input("Write a secure password: ")
            passwordValida = fnc.checkPassword(Password)
        fnc.InsertUser(Username,Password)
    if opc =="3":
        fnc.getHeader("Show Adventures")
    if opc == "4":
        break
