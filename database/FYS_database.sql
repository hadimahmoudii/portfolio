-- Maak de database "FYS"
CREATE DATABASE IF NOT EXISTS FYS;

-- Schakel over naar de database "FYS"
USE FYS;

-- Maak de tabel "Passagier" binnen de database "FYS"
CREATE TABLE IF NOT EXISTS `Passagier` (
  `klantnummer` int NOT NULL,
  `voornaam` varchar(45) NOT NULL,
  `achternaam` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`klantnummer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Maak de tabel "Ticket" binnen de database "FYS"
CREATE TABLE IF NOT EXISTS `Ticket` (
  `ticketnummer` int NOT NULL,
  `klantnummer` int NOT NULL,
  PRIMARY KEY (`ticketnummer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Voeg enkele rijen toe aan de tabel "Passagier"
INSERT INTO `Passagier` VALUES 
  ('001','Hadi','Mahmoudi'),
  ('002','Lionel','Messi'),
  ('003','Cristiano','Ronaldo');

-- Voeg enkele rijen toe aan de tabel "Ticket"
INSERT INTO `Ticket` VALUES 
  ('001002003','001'),
  ('004005006','002'),
  ('007008009','003');