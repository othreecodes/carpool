-- phpMyAdmin SQL Dump
-- version 4.4.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 25, 2016 at 03:15 PM
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
-- Table structure for table `agency_details`
--

CREATE TABLE IF NOT EXISTS `agency_details` (
  `id` int(11) NOT NULL,
  `name` varchar(1000) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `user_id` varchar(1000) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `agency_details`
--

INSERT INTO `agency_details` (`id`, `name`, `address`, `user_id`) VALUES
(1, 'ere', 'erer', 'g');

-- --------------------------------------------------------

--
-- Table structure for table `licence`
--

CREATE TABLE IF NOT EXISTS `licence` (
  `id` int(11) NOT NULL,
  `driver_id` varchar(1000) NOT NULL,
  `licence_no` varchar(1000) NOT NULL,
  `iss_date` varchar(1000) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `licence`
--

INSERT INTO `licence` (`id`, `driver_id`, `licence_no`, `iss_date`) VALUES
(1, 'd', 'rwerew', '2016-06-15'),
(2, 'g', '733', '2015-08-03');

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE IF NOT EXISTS `request` (
  `id` int(11) NOT NULL,
  `pick` varchar(1000) NOT NULL,
  `dest` varchar(1000) NOT NULL,
  `reg_date` varchar(1000) NOT NULL,
  `user_id` varchar(1000) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `bearable` varchar(1000) NOT NULL,
  `status` varchar(1000) NOT NULL,
  `driver_id` varchar(1000) NOT NULL,
  `vehicle_id` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `request`
--

INSERT INTO `request` (`id`, `pick`, `dest`, `reg_date`, `user_id`, `gender`, `bearable`, `status`, `driver_id`, `vehicle_id`) VALUES
(17, 'ff', 'dd', '2016-06-23 14:19:56.905000', 'o', 'Male', '34', 'denied', 'g', '0'),
(18, 'None', 'None', '2016-06-23 14:41:02.640000', 'o', 'Male', 'None', 'pending', 'g', '0');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL,
  `names` varchar(1000) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `email` varchar(1000) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `user_type` varchar(100) NOT NULL,
  `username` varchar(1000) NOT NULL,
  `password` varchar(1000) NOT NULL,
  `reg_date` varchar(1000) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `names`, `address`, `email`, `mobile`, `gender`, `user_type`, `username`, `password`, `reg_date`) VALUES
(1, 'huuy', 'rr', 'r', 'ghthg', 'Male', 'Passenger', 'o', 'o', '2016-06-22 20:35:21'),
(2, 'd', 'r', 'y', 'u', 'Male', 'Driver', 'y', 'y', '2016-06-22 20:38:06'),
(3, 'dsf', 'fdsd', 'sdfdf', 'fsdf', 'Male', 'Driver', 'dsf', 'dsf', '2016-06-23 09:39:28'),
(4, 'ghf', 'gh', 'fg', 'f', 'Male', 'Driver', 'gh', 'hg', '2016-06-23 09:40:31'),
(5, 'f', 'd', 'fd', 'fd', 'Male', 'Driver', 'fd', 'df', '2016-06-23 09:42:39'),
(6, 'gf', 'gf', 'gf', 'fg', 'Male', 'Driver', 'fg', 'gf', '2016-06-23 09:43:03'),
(7, 'fds', 'fsd', 'fds', 'fsd', 'Male', 'Driver', 'fsd', 'fsd', '2016-06-23 09:48:32'),
(8, 's', 'ds', 'sd', 'sd', 'Male', 'Driver', 'ds', 'sd', '2016-06-23 09:49:19'),
(9, 'sf', 'fsd', 'dsf', 'fsd', 'Male', 'Driver', 'fds', 'fds', '2016-06-23 10:52:17'),
(10, 'vcx', 'vcx', 'cxv', 'cxv', 'Male', 'Driver', 'cvx', 'cvx', '2016-06-23 10:54:08'),
(11, 'ds', 'fsdf', 'ddsfd', 'dsf', 'Male', 'Driver', 'dsf', 'sdf', '2016-06-23 10:55:01'),
(12, 'dgd', 'gd', 'gfd', 'gfd', 'Male', 'Driver', 'd', 'dfg', '2016-06-23 10:55:43'),
(13, 'ghrtrfg', 'ghfgf', 'ggfnbgf', 'gfgf', 'Male', 'Driver', 'g', 'jhjh', '2016-06-23 14:15:13'),
(14, '', '', '', '', 'Male', 'Passenger', '', '', '2016-06-24 11:26:41');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE IF NOT EXISTS `vehicle` (
  `id` int(11) NOT NULL,
  `year` varchar(1000) NOT NULL,
  `make` varchar(1000) NOT NULL,
  `model` varchar(1000) NOT NULL,
  `seats` varchar(1000) NOT NULL,
  `type` varchar(1000) NOT NULL,
  `category` varchar(1000) NOT NULL,
  `user_id` varchar(1000) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`id`, `year`, `make`, `model`, `seats`, `type`, `category`, `user_id`) VALUES
(1, '1800', 'tiyuyt', 'heh', '5', 'Private', 'Car', 'y'),
(2, '1800', 'df', 'ff', '5', 'Hired', 'Car', 'g');

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
  `user_id` varchar(1000) NOT NULL,
  `vid` varchar(11) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `vehicle_sharing`
--

INSERT INTO `vehicle_sharing` (`id`, `cost`, `start_point`, `dest_point`, `start_time`, `arrival_time`, `no_pass`, `date`, `gender`, `user_id`, `vid`) VALUES
(3, '80', 'g', 'g', '8:00', '9:00', '4', '2016-06-23', 'Both', 'g', '0'),
(4, 'jnjhkj', 'jkhjkh', 'jhkjh', 'jkhjkh', 'kjhjkh', '3', '2016-06-23', 'Both', 'g', '0'),
(5, 'jkk', 'jkhjkj', 'hkjhkjhkj', 'hkjhkjhkj', 'hkjhjkhj', '3', '2016-06-16', 'Both', 'g', '0'),
(6, 'gghfgh', 'ghfgjfgh', 'fjhfjgfg', 'hfjhfjgf', 'hgfjh', '5', '2016-07-14', 'Male', 'g', '0'),
(7, 'jkhjhbj', 'jkjlhkjh', 'jklhjhkjl', 'jhjlhjkh', 'jhjhjk', '4', '2016-06-16', 'Both', 'g', '0'),
(8, 'gkj', ',hjhlkjh', 'jhljkhj', 'hljhljkhj', 'lkhlkj', '4', '2016-06-15', 'Female', 'g', '0'),
(9, 'jgljkghj', 'jhgkhgkj', 'hjghjgk', 'hjghgkjghkghjghj', 'hjgkhj', '5', '2016-06-07', 'Both', 'g', 'None'),
(10, 'kjhljh', 'lkjhkjhl', 'jkhlkjhjkl', 'hjkhjlkh', 'jkhlkjhjkl', '5', '2016-06-23', 'Female', 'g', 'None'),
(11, 'jkhjkhlj', 'hljkhlk', 'hjkhjklh', 'jklhjkh', 'jkhlkj', '4', '2016-06-08', 'Male', 'g', 'None'),
(12, 'jhghgkj', 'hgkjg', 'kjhgkhg', 'hjgkhg', 'jghg', '3', '2016-06-16', 'Male', 'g', '2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `agency_details`
--
ALTER TABLE `agency_details`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `licence`
--
ALTER TABLE `licence`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehicle`
--
ALTER TABLE `vehicle`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vehicle_sharing`
--
ALTER TABLE `vehicle_sharing`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `agency_details`
--
ALTER TABLE `agency_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `licence`
--
ALTER TABLE `licence`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=19;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `vehicle`
--
ALTER TABLE `vehicle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `vehicle_sharing`
--
ALTER TABLE `vehicle_sharing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=13;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
