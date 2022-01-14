drop database if exists BDDPROYECTOENERO;

CREATE DATABASE if not exists BDDPROYECTOENERO;

use BDDPROYECTOENERO;

create table if not exists BDDPROYECTOENERO.USER (
id_user int not null auto_increment primary key,
user_name varchar(45) not null,
password varchar(45) not null,
user_create varchar(45) null,
user_modify varchar(45) null,
create_date date null,
modify_date date null);

desc USER;

create table if not exists BDDPROYECTOENERO.CHARACTER(
id_character int auto_increment primary key,
name varchar(45) not null unique,
description varchar(200) not null,
user_create varchar(45) null,
user_modify varchar(45) null,
create_date date null,
modify_date date null);

create table if not exists ADVENTURE(
id_adventure int auto_increment primary key,
name varchar(200) not null,
description varchar(200) not null,
user_create varchar(45) null,
user_modify varchar(45) null,
create_date date null,
modify_date date null);

create table if not exists STEP(
id_step int auto_increment,
id_adventure int not null,
final_step bit(1) null,
description varchar(200) not null,
user_create varchar(45) null,
user_modify varchar(45) null,
create_date date null,
modify_date date null,
constraint FK_ADVENTURE_STEP
foreign key (id_adventure)
	references ADVENTURE(id_adventure),
primary key(id_step, id_adventure)
	);


create table if not exists BDDPROYECTOENERO.OPTION(
id_option int auto_increment primary key,
id_next_step int not null,
id_last_step int not null,
description varchar(200) not null,
answer varchar(200) not null,
user_create varchar(45) null,
user_modify varchar(45) null,
create_date date null,
modify_date date null,
constraint FK_OPTION_STEP
foreign key (id_next_step)
	references STEP(id_step),
constraint FK_STEP_OPTION
foreign key(id_last_step)
	references STEP(id_step)
    );

create table if not exists GAME(
id_game int auto_increment primary key,
id_character int not null,
id_user int not null,
id_adventure int not null,
user_create varchar(45) null,
user_modify varchar(45) null,
create_date date null,
modify_date date null,
date date not null,
constraint FK_GAME_CHARACTER
foreign key(id_character)
	references BDDPROYECTOENERO.CHARACTER(id_character),
constraint FK_GAME_USER
foreign key(id_user)
	references BDDPROYECTOENERO.USER(id_user),
constraint FK_GAME_ADVENTURE
foreign key(id_adventure)
	references ADVENTURE(id_adventure)
    );

create table if not exists BDDPROYECTOENERO.HISTORY(
id_history int auto_increment primary key,
id_game int not null,
id_option int not null,
id_step int not null,
user_create varchar(45) null,
user_modify varchar(45) null,
create_date date null,
modify_date date null,
constraint FK_HISTORY_GAME
foreign key(id_game)
	references GAME(id_game),
constraint FK_HISTORY_OPTION
foreign key(id_option)
	references BDDPROYECTOENERO.OPTION(id_option),
constraint FK_HISTORY_STEP
foreign key(id_step)
	references STEP(id_step)
    );

create table if not exists CHARACTER_ADVENTURE(
id_character int,
id_adventure int,
constraint FK_CHARACTER_ADVENTURE
foreign key(id_character)
	references BDDPROYECTOENERO.CHARACTER(id_character),
constraint FK_ADVENTURE_CHARACTER
foreign key(id_adventure)
	references ADVENTURE(id_adventure),
primary key(id_character, id_adventure)
    );

