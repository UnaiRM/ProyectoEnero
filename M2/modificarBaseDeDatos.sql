use BDDPROYECTOENERO;

alter table USER modify id_user int primary key auto_increment not null unique;
alter table USER modify user_name varchar(45) not null unique;
alter table USER modify password varchar(45) not null;
alter table USER modify create_date datetime not null;
alter table USER modify user_create varchar(45) not null;



alter table BDDPROYECTOENERO.CHARACTER modify id_character int primary key auto_increment not null unique;
alter table BDDPROYECTOENERO.CHARACTER modify name varchar(45) not null unique;
alter table BDDPROYECTOENERO.CHARACTER modify description varchar(200) not null;
alter table BDDPROYECTOENERO.CHARACTER modify create_date datetime not null;
alter table BDDPROYECTOENERO.CHARACTER modify user_create varchar(45) not null;



alter table ADVENTURE modify id_adventure int primary key auto_increment not null unique;
alter table ADVENTURE modify name varchar(200) not null;
alter table ADVENTURE modify description varchar(200) not null;
alter table ADVENTURE modify create_date datetime not null;
alter table ADVENTURE modify user_create varchar(45) not null;



alter table STEP modify id_step int auto_increment not null unique;
alter table STEP modify id_adventure int not null;
alter table STEP modify final_step int null;
alter table STEP modify description varchar(200) not null;
alter table STEP modify create_date datetime not null;
alter table STEP modify user_create varchar(45) not null;
alter table STEP add constraint pk_step primary key (id_step, id_adventure);
alter table STEP add constraint FK_ADVENTURE_STEP
foreign key (id_adventure)
	references ADVENTURE(id_adventure);
    

alter table BDDPROYECTOENERO.OPTION modify id_option int primary key auto_increment not null unique;
alter table BDDPROYECTOENERO.OPTION modify id_next_step int not null;
alter table BDDPROYECTOENERO.OPTION modify id_last_step int not null;
alter table BDDPROYECTOENERO.OPTION modify description varchar(200) not null;
alter table BDDPROYECTOENERO.OPTION modify create_date datetime not null;
alter table BDDPROYECTOENERO.OPTION modify user_create varchar(45) not null;
alter table BDDPROYECTOENERO.OPTION add constraint FK_OPTION_STEP
foreign key (id_next_step)
	references STEP(id_step);
alter table BDDPROYECTOENERO.OPTION add constraint FK_STEP_OPTION
foreign key(id_last_step)
	references STEP(id_step);
    


alter table GAME modify id_game int primary key auto_increment not null unique;
alter table GAME modify id_character int not null;
alter table GAME modify id_user int not null;
alter table GAME modify id_adventure int not null;
alter table GAME modify create_date datetime not null;
alter table GAME modify user_create varchar(45) not null;
alter table GAME add constraint FK_GAME_CHARACTER
foreign key(id_character)
	references BDDPROYECTOENERO.CHARACTER(id_character);
alter table GAME add constraint FK_GAME_USER
foreign key(id_user)
	references BDDPROYECTOENERO.USER(id_user);
alter table GAME add constraint FK_GAME_ADVENTURE
foreign key(id_adventure)
	references ADVENTURE(id_adventure);
    
    

alter table BDDPROYECTOENERO.HISTORY modify id_history int primary key auto_increment not null unique;
alter table BDDPROYECTOENERO.HISTORY modify id_game int not null;
alter table BDDPROYECTOENERO.HISTORY modify id_option int not null;
alter table BDDPROYECTOENERO.HISTORY modify id_step int not null;
alter table BDDPROYECTOENERO.HISTORY modify create_date datetime not null;
alter table BDDPROYECTOENERO.HISTORY modify user_create varchar(45) not null;
alter table BDDPROYECTOENERO.HISTORY add constraint FK_HISTORY_GAME
foreign key(id_game)
	references GAME(id_game);
alter table BDDPROYECTOENERO.HISTORY add constraint FK_HISTORY_OPTION
foreign key(id_option)
	references BDDPROYECTOENERO.OPTION(id_option);
alter table BDDPROYECTOENERO.HISTORY add constraint FK_HISTORY_STEP
foreign key(id_step)
	references STEP(id_step);



alter table CHARACTER_ADVENTURE modify id_character int not null;
alter table CHARACTER_ADVENTURE modify id_adventure int not null;
alter table CHARACTER_ADVENTURE add constraint FK_CHARACTER_ADVENTURE
foreign key(id_character)
	references BDDPROYECTOENERO.CHARACTER(id_character);
alter table CHARACTER_ADVENTURE add constraint FK_ADVENTURE_CHARACTER
foreign key(id_adventure)
	references ADVENTURE(id_adventure);
alter table CHARACTER_ADVENTURE add constraint pk_adventure primary key (id_character, id_adventure);
  