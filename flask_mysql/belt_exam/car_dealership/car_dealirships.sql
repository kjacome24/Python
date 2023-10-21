CREATE DATABASE  IF NOT EXISTS `car_dealership_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `car_dealership_schema`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: car_dealership_schema
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
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `id` int NOT NULL AUTO_INCREMENT,
  `price` int DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `make` varchar(255) DEFAULT NULL,
  `year` int DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_recipes_users_idx` (`user_id`),
  CONSTRAINT `fk_recipes_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES (1,2000,'Miata','Mazda',1900,'All good1','2023-10-19 21:51:47','2023-10-19 21:51:47',1),(3,1000,'Accent','Hyunday',2005,'All good3','2023-10-19 21:51:47','2023-10-19 21:51:47',2),(4,5000,'Limona','Toyoya',2003,'All good4','2023-10-19 21:51:47','2023-10-19 21:51:47',3),(9,7000,'Corola','Toyota',2020,'A classic one','2023-10-20 01:08:09','2023-10-20 01:08:09',1),(11,2400,'Alegro','Mazda',2014,'Good to go','2023-10-20 01:08:38','2023-10-20 01:08:38',2),(12,8000,'Clio','Renoult',2023,'A small but fast car','2023-10-20 01:19:22','2023-10-20 01:19:22',4),(13,3000,'Sandero','Renoult',2023,'I need money ','2023-10-20 01:23:01','2023-10-20 01:23:01',3),(14,3500,'Jetta','Volkswagen',2023,'This is a great deal. The car is in perfect condition, almost new. ','2023-10-20 02:01:01','2023-10-20 02:01:01',3),(16,1700,'Twingo','Renoult',2000,'An oldy that will not cost u a penny!','2023-10-20 02:38:18','2023-10-20 02:38:18',7);
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchases`
--

DROP TABLE IF EXISTS `purchases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchases` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `car_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_likes_users1_idx` (`user_id`),
  KEY `fk_likes_thoughts1_idx` (`car_id`),
  CONSTRAINT `fk_likes_thoughts1` FOREIGN KEY (`car_id`) REFERENCES `cars` (`id`),
  CONSTRAINT `fk_likes_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchases`
--

LOCK TABLES `purchases` WRITE;
/*!40000 ALTER TABLE `purchases` DISABLE KEYS */;
INSERT INTO `purchases` VALUES (1,4,1),(2,1,4),(6,7,3);
/*!40000 ALTER TABLE `purchases` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kevin','Duque','kevin.arturo.jacome.duque@gmail.com','$2b$12$f.i1Q93DfqWeR8Y1QeO2DuwrbCwewwxC6wsfUEtXzkto4ZR/cTVdi','2023-10-15 16:39:25','2023-10-15 16:39:25'),(2,'Emir','Duque','eduquemoscoso@gmail.com','$2b$12$jM9fzRYDQ4/92Un/51hG4.cm6gyvR78UBemfkACjR.zbzh3ictrNC','2023-10-15 16:41:07','2023-10-15 16:41:07'),(3,'Uma','Lola','uque@mail.m','$2b$12$N/.pFk9h6yXwaaIZXWHVRuCCHe2mkRieLX/4swkW0GlV3vIYB7U66','2023-10-15 16:45:34','2023-10-15 16:45:34'),(4,'Arturo','Jacome','aduque@gmail.com','$2b$12$aLiiHiOETzNKVuSaBDDGCOBErx3cXOYI7qgKqzX7ou6xCzAsvJi5e','2023-10-15 17:14:59','2023-10-15 17:14:59'),(5,'Arturo','Duque','ajacom@gmail.com','$2b$12$G8nfRwfQatLNBOdSUNFWUuPAqfJRMcTdipoMlyuY9wXKi5MdLagCi','2023-10-15 21:29:06','2023-10-15 21:29:06'),(7,'Emilio','Mosquera','emosquera@gmail.com','$2b$12$hGeR3bxCisdItS5VqUyYOu9IAiKPaGdPxAA7Qu3ls9AUqXRlRUdZe','2023-10-20 02:34:49','2023-10-20 02:34:49');
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

-- Dump completed on 2023-10-20  2:45:50
