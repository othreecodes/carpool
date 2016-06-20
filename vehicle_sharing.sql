-- phpMyAdmin SQL Dump
-- version 4.4.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2016 at 11:00 PM
-- Server version: 5.6.26
-- PHP Version: 5.6.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `carpool`
--

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_sharing`
--

CREATE TABLE IF NOT EXISTS `vehicle_sharing` (
  `id` int(11) NOT NULL,
  `cost` varchar(1000) NOT NULL,
  `start_point` varchar(1000) NOT NULL,
  `dest_point` varchar(1000) NOT NULL,
  `start_time` varchar(1000) NOT NULL,
  `arrival_time` varchar(1000) NOT NULL,
  `no_pass` varchar(1000) NOT NULL,
  `date` varchar(1000) NOT NULL,
  `gender` varchar(1000) NOT NULL,
  `user_id` varchar(1000) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicle_sharing`
--

INSERT INTO `vehicle_sharing` (`id`, `cost`, `start_point`, `dest_point`, `start_time`, `arrival_time`, `no_pass`, `date`, `gender`, `user_id`) VALUES
(1, '200', 'Gate', 'zik hall', '8:00am', '8:30am', '6', '2016-05-03', 'Both', 'ola'),
(2, '90', 'Gate', 'Zoo', '9:00', '9:15', '4', '2016-05-06', 'Both', 'ola'),
(3, '80', 'ZIik', 'Gate', '20:00', '20:30', '3', '2016-06-06', 'Both', 'yinka');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `vehicle_sharing`
--
ALTER TABLE `vehicle_sharing`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `vehicle_sharing`
--
ALTER TABLE `vehicle_sharing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
