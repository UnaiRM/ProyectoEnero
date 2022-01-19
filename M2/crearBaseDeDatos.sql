drop database if exists BDDPROYECTOENERO;

CREATE DATABASE if not exists BDDPROYECTOENERO;

use BDDPROYECTOENERO;

create table if not exists BDDPROYECTOENERO.USER (
id_user int,
user_name varchar(45),
password varchar(45),
user_create varchar(45),
user_modify varchar(45),
create_date datetime,
modify_date datetime);


create table if not exists BDDPROYECTOENERO.CHARACTER(
id_character int,
name varchar(45),
description varchar(200),
user_create varchar(45),
user_modify varchar(45),
create_date datetime,
modify_date datetime);

create table if not exists ADVENTURE(
id_adventure int,
name varchar(200),
description varchar(200),
user_create varchar(45),
user_modify varchar(45),
create_date datetime,
modify_date datetime);

create table if not exists STEP(
id_step int,
id_adventure int,
final_step int,
description varchar(200),
user_create varchar(45),
user_modify varchar(45),
create_date datetime,
modify_date datetime);


create table if not exists BDDPROYECTOENERO.OPTION(
id_option int,
id_next_step int,
id_last_step int,
description varchar(200),
answer varchar(200),
user_create varchar(45),
user_modify varchar(45),
create_date datetime,
modify_date datetime);

create table if not exists GAME(
id_game int,
id_character int,
id_user int,
id_adventure int,
user_create varchar(45),
user_modify varchar(45),
create_date datetime,
modify_date datetime,
date datetime);

create table if not exists BDDPROYECTOENERO.HISTORY(
id_history int,
id_game int,
id_option int,
id_step int not null,
user_create varchar(45),
user_modify varchar(45),
create_date datetime,
modify_date datetime);

create table if not exists CHARACTER_ADVENTURE(
id_character int,
id_adventure int);

