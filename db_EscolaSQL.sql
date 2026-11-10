/* Código para ser executado num SGBD. No meu caso, MySQL.
Não foi necessário usar hashs para esconder a senha pois este projeto foi executado com objetivo de aprendizagem. Os dados não correspondem a usuários/senhas reais.
Além disso, é necessário configurar o host pelo SGBD.
*/

CREATE USER 'admin_python'@'localhost' IDENTIFIED BY 'Senha123!';

GRANT ALL PRIVILEGES ON *.*
TO 'admin_python'@'localhost'
WITH GRANT OPTION;

CREATE DATABASE db_escola;
USE db_escola;

CREATE TABLE IF NOT EXISTS usuarios(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nomeAluno VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    idade int
    );

select * from usuarios;