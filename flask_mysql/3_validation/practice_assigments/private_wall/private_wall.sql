CREATE DATABASE  IF NOT EXISTS `private_wall_schema` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `private_wall_schema`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: private_wall_schema
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
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `sender_id` int NOT NULL,
  `receiver_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users_idx` (`sender_id`),
  KEY `fk_messages_users1_idx` (`receiver_id`),
  CONSTRAINT `fk_messages_users` FOREIGN KEY (`sender_id`) REFERENCES `users` (`id`),
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`receiver_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'xxxxxxxxxxxxxxxxxxxxxx','2023-10-14 23:02:00','2023-10-14 23:02:00',1,2),(2,'ssssssssssssssssssssssssssss','2023-10-14 23:03:48','2023-10-14 23:03:48',1,3),(4,'dsdsdsdsd','2023-10-15 00:10:31','2023-10-15 00:10:31',1,2),(9,'Hello Arnold! Have you seen the latest report? Please ping me ASAP.','2023-10-15 02:29:42','2023-10-15 02:29:42',1,2),(10,'Hello Yousef! Is there any update about the meeting?','2023-10-15 02:30:16','2023-10-15 02:30:16',1,3),(11,'Hello Jorge. I am sorry but I could not pick up your call. WHats up?','2023-10-15 02:32:13','2023-10-15 02:32:13',1,4),(12,'Hello Moha, indeed. It does not look good. We will have to brain storm to change the idea. ','2023-10-15 02:33:58','2023-10-15 02:33:58',2,1),(13,'Hi Moha,\r\nHave you talk to Daniel? He is looking for you.','2023-10-15 03:08:49','2023-10-15 03:08:49',4,1);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
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
  `updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Mohammed','Morales','kduque@codingdojo.com','$2b$12$ePKShu4ltWS8NBVX5BcJbuhnxIkM1Si8QAmCUT6HqOuJlFSswCh.2','2023-10-14 19:04:49','2023-10-14 19:04:49'),(2,'Arnold','Jacome','kabo92@hotmail.com','$2b$12$kDpLYiwLF7FhqSTjP2qpxuHycXGBBvoEM9FkenCAryZ1X32wdAUZG','2023-10-14 21:01:34','2023-10-14 21:01:34'),(3,'Yousef','Hoxha','ell@cmcm.com','$2b$12$EnEwMeNahAPCJcOFNP6JP.GvxVxUH3ZVlT6utxM4swBvSCgD05mi.','2023-10-14 21:02:04','2023-10-14 21:02:04'),(4,'Jorge','Leka','dddd@sdsdsd.co','$2b$12$.zUZuCfTGLzhwBRSZb0dO.6MO3tf4QXQOpwybA0cd34bEMIZTx4Yy','2023-10-14 21:03:29','2023-10-14 21:03:29'),(5,'Daniel','Hoxha','dfffff@codingdojo.com','$2b$12$849pOM5eOtyCXegtVt056OEZ2A4z0aTH.w1dSrDMuMJTrfufqHEhm','2023-10-14 21:05:17','2023-10-14 21:05:17'),(6,'Kevin','Duque','kevin.arturo.jacome.duque@gmail.com','$2b$12$/BtsaLnfIsaEeUyOOuFQZu.wnffWQW8YF0pJS9oDBYsA5nHR/yXUi','2023-10-15 01:05:49','2023-10-15 01:05:49'),(7,'arturin','Duque','duque@gmail.com','$2b$12$/K3CNchqeMon12anpUXgCe4wGrth8zlwPP0ZGeYlivAMEDaLMD7QS','2023-10-15 02:03:55','2023-10-15 02:03:55');
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

-- Dump completed on 2023-10-15  3:39:46
