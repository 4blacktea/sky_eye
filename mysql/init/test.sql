-- 创建数据库
CREATE DATABASE  `sky_eye` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
grant all PRIVILEGES on sky_eye.* to root@'%' identified by 'adminermysql';
flush privileges;
use sky_eye;
-- 创建domain表
CREATE TABLE IF NOT EXISTS `domain` (
  `id` int(8) NOT NULL,
  `domain` varchar(200) NOT NULL,
  `main_domain` varchar(200) NOT NULL,
  `domain_group` varchar(200) NOT NULL,
  `createtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=351938 DEFAULT CHARSET=utf8mb4;
-- 创建port表
CREATE TABLE IF NOT EXISTS `port` (
  `id` int(8) NOT NULL,
  `domain` varchar(200) NOT NULL,
  `main_domain` varchar(200) NOT NULL,
  `domain_group` varchar(200) NOT NULL,
  `port` int(8) NOT NULL,
  `protocol` varchar(200) NOT NULL,
  `p_version` varchar(200) NOT NULL,
  `p_status` varchar(200) NOT NULL,
  `createtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=1715 DEFAULT CHARSET=utf8mb4;

