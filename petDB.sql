CREATE DATABASE IF NOT EXISTS `petDB`;

USE `petDB`;

CREATE TABLE IF NOT EXISTS `userInfo` (
	`user` varchar(30) NOT NULL,
    `email` varchar(50),
    `password` varchar(30),
    `loggedIn` bool, 
    PRIMARY KEY (`user`)
);

CREATE TABLE IF NOT EXISTS `petInfo`(
    `pet_name` varchar(20),
    `pet_type` varchar(5),
    `username` varchar(30) NOT NULL,
    PRIMARY KEY (`pet_name`),
    FOREIGN KEY (`username`) REFERENCES `userInfo`(`user`)

);

INSERT INTO `userInfo`
VALUES ('dslidder', 'dslidder@iastate', 'pass',true), ('alex', 'alex@iastate','pass2',false), ('adam', 'adam@iastate','pass3',false), ('caitih', 'caiti@iastate','pass4',false);

INSERT INTO `petInfo`
VALUES ('Cleo', 'Dog', 'dslidder'), ('Dragon', 'Cat', 'alex'), ('Peanut', 'cat', 'caitih'), ('Toto', 'dog', 'adam');

SELECT pet_name FROM petInfo WHERE username = 'dslidder';
