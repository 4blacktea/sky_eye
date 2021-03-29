CREATE TABLE IF NOT EXISTS `domain` (
  `id` int(8) NOT NULL,
  `domain` varchar(200) NOT NULL,
  `main_domain` varchar(200) NOT NULL,
  `domain_group` varchar(200) NOT NULL,
  `createtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=351938 DEFAULT CHARSET=utf8mb4;