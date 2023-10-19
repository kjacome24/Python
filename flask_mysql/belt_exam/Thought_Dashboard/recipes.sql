CREATE DATABASE  IF NOT EXISTS `recipes_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `recipes_schema`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: recipes_schema
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recipes`
--

DROP TABLE IF EXISTS `recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `instructions` varchar(255) DEFAULT NULL,
  `under_30_min` varchar(255) DEFAULT NULL,
  `date_cooked` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_recipes_users_idx` (`user_id`),
  CONSTRAINT `fk_recipes_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipes`
--

LOCK TABLES `recipes` WRITE;
/*!40000 ALTER TABLE `recipes` DISABLE KEYS */;
INSERT INTO `recipes` VALUES (1,'Omelette','In some combination of the above','dasdasdasd','Yes','2023-10-04 00:00:00','2023-10-15 21:26:35','2023-10-15 21:26:35',1),(3,'Boiled eggs','Eggs boiled','Just boil the egg.','Yes','2023-10-14 00:00:00','2023-10-15 19:44:05','2023-10-15 19:44:05',3),(4,'Hot dog','hot dogs','boil the sausage and put everything toguether. ','Yes','2023-10-10 00:00:00','2023-10-15 19:49:54','2023-10-15 19:49:54',4),(5,'Tamales (Colombia)','This is a colombian thing','To complicated to explain. Maybe later.','No','2023-10-04 00:00:00','2023-10-15 21:12:40','2023-10-15 21:12:40',1),(7,'Muffin','I have no idea how to make it','try by yourself','No','2023-10-27 00:00:00','2023-10-15 21:27:18','2023-10-15 21:27:18',1);
/*!40000 ALTER TABLE `recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kevin','Duque','kevin.arturo.jacome.duque@gmail.com','$2b$12$f.i1Q93DfqWeR8Y1QeO2DuwrbCwewwxC6wsfUEtXzkto4ZR/cTVdi','2023-10-15 16:39:25','2023-10-15 16:39:25'),(2,'Emir','Duque','eduquemoscoso@gmail.com','$2b$12$jM9fzRYDQ4/92Un/51hG4.cm6gyvR78UBemfkACjR.zbzh3ictrNC','2023-10-15 16:41:07','2023-10-15 16:41:07'),(3,'Uma','Lola','uque@mail.m','$2b$12$N/.pFk9h6yXwaaIZXWHVRuCCHe2mkRieLX/4swkW0GlV3vIYB7U66','2023-10-15 16:45:34','2023-10-15 16:45:34'),(4,'Arturo','Jacome','aduque@gmail.com','$2b$12$aLiiHiOETzNKVuSaBDDGCOBErx3cXOYI7qgKqzX7ou6xCzAsvJi5e','2023-10-15 17:14:59','2023-10-15 17:14:59'),(5,'Arturo','Duque','ajacom@gmail.com','$2b$12$G8nfRwfQatLNBOdSUNFWUuPAqfJRMcTdipoMlyuY9wXKi5MdLagCi','2023-10-15 21:29:06','2023-10-15 21:29:06');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-15 21:34:41
