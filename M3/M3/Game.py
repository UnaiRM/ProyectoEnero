import functions.Functions as fnc
opc = 5
loged = False
while opc != 4:
    if loged == False:
        fnc.gameTitle()
        txt = ("1)Login","2)Create user","3)Replay adventures","4)Exit")
        opt = "\nChoose your Option:"
        lista = ["1","2","3","4"]
        exc = []
        opc = fnc.GetOpt(txt, opt, lista, exc)
    else:
        fnc.gameTitle()
        txt = ("1)Log Out", "2)Create user", "3)Replay adventures", "4)Play", "5)Exit")
        opt = "\nChoose your Option:"
        lista = ["1", "2", "3", "4","5"]
        exc = []
        opc = fnc.GetOpt(txt, opt, lista, exc)
        if opc == "1":
            loged = False
            opc = 0
        if opc == "4":
            fnc.play(user)
            opc = 0
        if opc == "5":
            opc = "4"
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
                loged = True
                input("Press Enter to start the game")
                fnc.play(user)
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
        fnc.replay()
    if opc == "4":
        print("You have successfully exited the game!")
        break

