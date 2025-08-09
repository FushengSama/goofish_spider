
CREATE TABLE `goods` (
  `category` char(64) DEFAULT NULL,
  `price` int NOT NULL,
  `uuid` char(64) NOT NULL,
  `location` char(16) DEFAULT NULL,
  `user_name` char(64) DEFAULT NULL,
  `instruction` text,
  `link` varchar(255) NOT NULL DEFAULT '',
  `update_time` time DEFAULT NULL,
  `is_delete` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- spiderTest.categorys definition

CREATE TABLE `categorys` (
  `category` char(64) NOT NULL,
  `num` int DEFAULT NULL,
  `create_time` time DEFAULT NULL,
  `is_delete` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`category`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;