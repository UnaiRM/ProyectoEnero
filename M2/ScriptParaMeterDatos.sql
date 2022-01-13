use BDDPROYECTOENERO;

insert into USER(user_name, password, user_create, create_date)
values ('Unai','qwerty', current_user(), curdate()), ('Xavi','12345', current_user(), curdate()), ('Samu','123123', current_user(), curdate());

insert into BDDPROYECTOENERO.CHARACTER(name, description, user_create, create_date)
values ('Goku', 'Un super sayan del planeta Vegeta, muy mamado', current_user(),curdate()),
		('Aventurero', 'Tipico protagonista de historias de aventuras', current_user(), curdate()),
		('Mario Bros', 'Un fontanero un tanto extraño que se alimenta con setas alucinogenas', current_user(), curdate());

insert into ADVENTURE(name, description, user_create, create_date)
values ('Freezer Vuelve a atacar(version corta de la pelea)','Freezer decide volver a la vida y atacar de nuevo el planeta tierra, si, otra vez el mismo planeta...', current_user(), curdate()),
		('Los 3 caminos del bosque maldito', 'Apareces en medio de un gran bosque maldito, deberas elegir sabiamente para no morir', current_user(), curdate()),
        ('A salvar a la princesa','La princesa parece estar en apuros, corre y ve a salvarle', current_user(), curdate()),
        ('Pelea epica contra Saitama', 'Estas dentro de una competicion de combates y te ha tocado contra Saitama, ideatelas para ganar', current_user(), curdate());


insert into STEP(id_adventure, final_step, description, user_create, create_date)
values  (1,0, 'Al parecer freezer es un resentido y vuelve a la vida para destruir el planeta tierra!!! Que haras?', current_user(), curdate()),
		(1,1, 'Has querido ser amable con el y pedirle porfavor que se vaya, parece ser que el no ha sido tan amable, has muerto :c', current_user(), curdate()),
        (1,0, 'Has decidido pelear con el, pero parece que tu ferza de ahora no es suficiente, que haces?', current_user(), curdate()),
        (1,1, 'Decides convertirte en super sayan2, pero parece que sigue siendo insuficiente y freezer te mata...', current_user(), curdate()),
        (1,1, 'Decides llamar a Saitama tu querido amigo, el se hace cargo del asunto y os vais a hechar unas partidas a la consola', current_user(), curdate()),
        (2,0, 'La alarma te despierta, que deberias hacer?', current_user(),curdate()),
        (2,0, 'Vuelve a sonar la alarma, creo que deberias hacer algo...', current_user(), curdate()),
        (2,1, 'Acabas perdiendo contra la pereza, a la proxima muevete aunque sea...', current_user(),curdate()),
        (2,0, 'Logras levantarte exitosamente, que deberias hacer?', current_user(), curdate()),
        (2,1, 'Has sido sabio, y te has dado cuenta que no vale la pena correr tantos peligros, hay muchos peces en el mar', current_user(), curdate()),
        (2,0, 'Te encuentras con un monstruo, que deberias hacer?', current_user(), curdate()),
        (2,0, 'Consigues entrar al castillo sin problemas, que haces?', current_user(), curdate()),
        (2,1, 'Parece ser que el monstruo te ha caido fantasticamente, y se te ha olvidado ir a por la princesa por salir de fiesta con el', current_user(), curdate()),
        (2,0, 'Has logrado entrar al castillo del monstruo!!! Que deberias hacer?',current_user(), curdate()),
        (2,1, 'Intentas luchar contra el jefe, pero parece que el es muchisimo mas fuerte que tu, acabas siendo su cena', current_user(), curdate()),
        (2,1, 'Parece ser que esta celda no es la de la princesa... Has caido en una trampa, ahora estaras encerrado para siempre',current_user(), curdate()),
        (2,0, 'Llegas ardiendo a la torre del monstruo, que deberias hacer?', current_user(), curdate()),
        (2,1, 'Por lo que parece no sabes que las hojas secas se queman mas... mala eleccion, mueres abrasado', current_user(), curdate()),
        (2,0, 'El heroe entra al castillo y se encuentra a la princesa cenando con el monstruo? Que deberia hacer?', current_user(), curdate()),
        (2,1, 'Vaya, al final el monstruo eres tu, y acabas separando a dos personas que se aman...',current_user(), curdate()),
        (2,1, 'Te has dado cuenta que eres un stalker, y decides dejarles ser felices y irte por donde has entrado',current_user(), curdate()),
        (3,0, 'Has entrado a un concurso de combates porque te crees muy fuerte, y te toca contra el gran Saitama en el primer combate, que deberias hacer?', current_user(), curdate()),
        (3,1, 'Enserio decides enfrentarle de frente? No logras hacerle ni un rasguño y el te vence solo con pestañear...', current_user(), curdate()),
        (3,1, 'Decides huir y pierdes tu orgullo, pero al menos sales vivo de allá', current_user(), curdate()),
        (3,0, 'Al pedir que nivelen mas tu combate, te colocan contra Freezer, que ya se ha cansado de intentar destruir la tierra y estaba de paso, que decides hacer?', current_user(), curdate()),
        (3,1, 'Al parecer has logrado convertirte en supersayan 3, y logras salir victorioso, muchas felicidades',current_user(), curdate()),
        (3,1, 'Freezer te dice que te va a dejar ganar, y tu te lo crees, acabas reciviendo una gran paliza y una leccion, no confies en los malos de la serie...', current_user(), curdate());
     
select * from BDDPROYECTOENERO.OPTION;


insert into BDDPROYECTOENERO.OPTION(id_next_step, id_last_step,description, answer, user_create, create_date)
values  (2,1,'Intentar ser amable para que se vaya sin pelear', 'Le dices amablemente si se puede ir, que no va a ganar nada destruyendo la tierra',current_user(),curdate()),
		(4,3,'Convertirte en superSayan2', 'Asumes que con la fuerza de un supersayan2 podras vencer a freezer y te conviertes en uno', current_user(),curdate()),
        (5,3,'Llamar a tu amigo Saitama', 'Hoy no te apetece pelear, y decides llamar a Saitama',current_user(),curdate()),
        (7,6,'Pausar la alarma para dormir un poco mas', 'Por un rato que duerma mas no pasara nada...',current_user(),curdate()),
        (8,7,'Apagar la alarma, a dormir se ha dicho!', 'No te apetece salir a por la princesa hoy, que ayer curraste mucho',current_user(),curdate()),
        (9,6,'Sair de la cama', 'Por mucho sueño que tengas debes salvar a tu princesa!',current_user(),curdate()),
        (10,9,'No ir a por la princesa', 'Aunque te hayas levantado decides no ir hacia ella, ya encontraras a otra persona',current_user(),curdate()),
        (11,9,'Equiparte apropiadamente y salir a la aventura', 'Coges algo de quipamiento (Armadura, espada y unas pociones',current_user(),curdate()),
        (12,9,'No equiparse ya que es demasiado fuerte, no tendra problemas', 'Sale por la puerta con el pijama puesto y todo',current_user(),curdate()),
        (13,11,'Intentar hacerte amigo del monstruo', 'Crees que podrias solucionar el problema de una forma pacifica y intentas hacerte amigo del monstruo',current_user(),curdate()),
        (17,11,'Pelear contra el monstruo','El monstruo no parece muy fuerte, asi que deberia poder luchar contra el',current_user(),curdate()),
        (14,11,'Salir corriendo lo mas rapido posible','Crees que el monstruo te supera y debes correr y pasar de el',current_user(),curdate()),
        (15,14,'Ir a buscar al gran boss y matarle', 'Crees que dandole un ataque sorpresa podras matar al jefe y decides buscarle',current_user(),curdate()),
        (16,14,'Ir directo hacia la celda de la princesa','Hay unas indicaciones claras hacia donde debes ir para llegar a la celda de la princesa',current_user(),curdate()),
        (18,17,'Intentar apagar el fuego tirandote al suelo','Decides tirarte al suelo y dar vueltas para apagar el fuego',current_user(),curdate()),
        (19,17,'Tomar una pocion de cuerpo ignifugo','Sacas la pocion de cuerpo ignifugo que te habias crafteado en minecraft',current_user(),curdate()),
        (20,19,'Raptar a la princesa','Muerto de la envidia intentas raptar y llevarte a la princesa',current_user(),curdate()),
        (21,19,'Dejarles en paz','Te sientes mal por lo que has estado haciendo y prefieres irte',current_user(),curdate()),
        (23,22,'Pelear de frente','Sientes por alguna extraña razon que puedes ganar',current_user(),curdate()),
        (24,22,'Irte del concurso','Tienes tanto miedo que sales corriendo',current_user(),curdate()),
        (25,22,'Pedir un cambio','Piensas un poco y decides pedir un cambio de oponente',current_user(),curdate()),
        (26,25,'Convertirte en superSayan3','Intentas convertirte en supersayan 3 para vencer a Freezer',current_user(),curdate()),
        (27,25,'Pedirle a Freezer que se deje ganar','Piensas que convencer a Freezer es la mejor manera de salir vivo de alli',current_user(),curdate())

