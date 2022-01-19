import functions.Functions as fnc
first_menu = True

while first_menu:
    fnc.gameTitle()
    txt = "1)Login\n2)Create user\n3)Show adventures\n4)Exit"
    opt = "\nChoose your Option:"
    lista = ["1","2","3","4"]
    exc = ["w", "e", "-1"]
    opc = fnc.GetOpt(txt, opt, lista, exc)
    LoginCheck = 0
    if opc == "1":
        fnc.getHeader("Login")
        while LoginCheck != 1:
            user = input("Username: ")
            passwd = input("Password: ")
            LoginCheck = fnc.checkUserbdd(user,passwd)
            if LoginCheck == 1:
                print("Login Correct")
            if LoginCheck == -1:
                print("Incorrect Password")
            if LoginCheck == 0:
                print("User not found")
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
    break
