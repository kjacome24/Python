CREATE DATABASE  IF NOT EXISTS `thoughts_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `thoughts_schema`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: thoughts_schema
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
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `thought_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_likes_users1_idx` (`user_id`),
  KEY `fk_likes_thoughts1_idx` (`thought_id`),
  CONSTRAINT `fk_likes_thoughts1` FOREIGN KEY (`thought_id`) REFERENCES `thoughts` (`id`),
  CONSTRAINT `fk_likes_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (72,2,2),(73,2,4),(76,2,20),(87,3,2),(88,4,21),(89,3,4),(91,6,20),(92,1,23),(94,1,4),(95,1,20),(96,1,21);
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `thoughts`
--

DROP TABLE IF EXISTS `thoughts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `thoughts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `thought` varchar(255) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`,`user_id`),
  KEY `fk_recipes_users_idx` (`user_id`),
  CONSTRAINT `fk_recipes_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `thoughts`
--

LOCK TABLES `thoughts` WRITE;
/*!40000 ALTER TABLE `thoughts` DISABLE KEYS */;
INSERT INTO `thoughts` VALUES (2,'Be stoic','2023-10-18 00:23:50','2023-10-18 00:23:50',2),(4,'The top of the montain is just the beginning of the next one.','2023-10-18 13:53:17','2023-10-18 13:53:17',2),(20,'Be or not to be','2023-10-18 19:20:04','2023-10-18 19:20:04',1),(21,'Skills will overpower universities','2023-10-18 20:40:09','2023-10-18 20:40:09',4),(22,'Unity is key for a better world','2023-10-18 20:41:13','2023-10-18 20:41:13',3),(23,'Me van a comprar una play! hurra!!!','2023-10-18 21:00:50','2023-10-18 21:00:50',6);
/*!40000 ALTER TABLE `thoughts` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kevin','Duque','kevin.arturo.jacome.duque@gmail.com','$2b$12$f.i1Q93DfqWeR8Y1QeO2DuwrbCwewwxC6wsfUEtXzkto4ZR/cTVdi','2023-10-15 16:39:25','2023-10-15 16:39:25'),(2,'Emir','Duque','eduquemoscoso@gmail.com','$2b$12$jM9fzRYDQ4/92Un/51hG4.cm6gyvR78UBemfkACjR.zbzh3ictrNC','2023-10-15 16:41:07','2023-10-15 16:41:07'),(3,'Uma','Lola','uque@mail.m','$2b$12$N/.pFk9h6yXwaaIZXWHVRuCCHe2mkRieLX/4swkW0GlV3vIYB7U66','2023-10-15 16:45:34','2023-10-15 16:45:34'),(4,'Arturo','Jacome','aduque@gmail.com','$2b$12$aLiiHiOETzNKVuSaBDDGCOBErx3cXOYI7qgKqzX7ou6xCzAsvJi5e','2023-10-15 17:14:59','2023-10-15 17:14:59'),(5,'Arturo','Duque','ajacom@gmail.com','$2b$12$G8nfRwfQatLNBOdSUNFWUuPAqfJRMcTdipoMlyuY9wXKi5MdLagCi','2023-10-15 21:29:06','2023-10-15 21:29:06'),(6,'Matias','Gutierrez','matiguti@gmail.com','$2b$12$Ws9VCjOCFl45JmvnLocHlu4Elj3Inpylg4IZCu4.IU/LUj4iYurNa','2023-10-18 21:00:24','2023-10-18 21:00:24');
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

-- Dump completed on 2023-10-18 22:22:08
