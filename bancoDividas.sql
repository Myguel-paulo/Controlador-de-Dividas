create database bancoDividas;
use bancoDividas;

create table salario_meses(
id_mes int(9) auto_increment,
nome_mes varchar(80) not null,
ano varchar(4) not null,
valor_salario decimal(10,2),
primary key(id_mes)
);

create table dividas(
id_divida int(9) auto_increment,
descricao varchar(180),
valor decimal(10,2) not null,
id_mes int(9) not null,
foreign key (id_mes) references salario_meses(id_mes),
primary key(id_divida)
);


