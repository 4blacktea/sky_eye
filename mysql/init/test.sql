-- 创建数据库
CREATE DATABASE  `sky_eye` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
grant all PRIVILEGES on sky_eye.* to root@'%' identified by 'adminermysql';
flush privileges;
use sky_eye;
-- 创建domain表
CREATE TABLE IF NOT EXISTS `domain` (
  `id` int(8) AUTO_INCREMENT primary key NOT NULL,
  `domain` varchar(200) NOT NULL,
  `main_domain` varchar(200) NOT NULL,
  `domain_group` varchar(200) NOT NULL,
  `createtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=351938 DEFAULT CHARSET=utf8mb4;
-- 创建port表
CREATE TABLE IF NOT EXISTS `port` (
  `id` int(8) AUTO_INCREMENT primary key NOT NULL,
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
--创建web表
CREATE TABLE IF NOT EXISTS `web` (
  `id` int(8) NOT NULL,
  `domain` text NOT NULL,
  `web_port` int(8) NOT NULL,
  `http_protocol` varchar(200) NOT NULL,
  `web_url` varchar(200) NOT NULL,
  `finger` varchar(200) NOT NULL,
  `screen_pic` varchar(200) NOT NULL,
  `creattime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ext` int(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=utf8mb4;
-- 创建monitor表
CREATE TABLE IF NOT EXISTS `monitor` (
  `id` int(8) AUTO_INCREMENT primary key NOT NULL,
  `target_type` varchar(200) NOT NULL,
  `target` varchar(200) NOT NULL,
  `scan_strategy` varchar(200) NOT NULL,
  `strategy_vule` varchar(200) NOT NULL,
  `is_open` varchar(100) NOT NULL DEFAULT '0',
  `createtime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

