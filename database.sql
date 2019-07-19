CREATE DATABASE  IF NOT EXISTS `practice`;
USE `practice`;
--
-- Host: localhost    Database: practice
-- ------------------------------------------------------

--
-- Create Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(250) DEFAULT NULL,
  `Email` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`Id`)
);

LOCK TABLES `users` WRITE;

--
-- Insert 3 records in to table `users`
--

INSERT INTO `users` VALUES (1,'Bijay Koirala','Koirala@gmail.com'),(2,'Yadav Pokharel','Pokharel@gmail.com'),(3,'Maharjan Koirala','Maharjan@gmail.com'),(4,'$name','$email'),(6,'name','email'),(8,'Dip','Dip@yahoo.com');

--
-- procedure to delete records with null entry from the table `users`
--

DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `deleter_user_if_null`()
begin
delete from users where id is null or name is null or email is null;
end ;;
DELIMITER ;

--
-- procedure to get users from the table `users`
--

DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `getuser`()
begin
select * from users;
end ;;
DELIMITER ;

--
-- procedure to a insert user into table `users`
--

DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_user`(
in _name varchar(250),
in _email varchar(250)
)
begin
insert into users (Name, Email)
values(_name, _email);
end ;;
DELIMITER ;

