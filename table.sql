-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 29, 2022 at 08:38 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.1.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `criminaldb`
--

-- --------------------------------------------------------

--
-- Table structure for table `criminaldata`
--

CREATE TABLE `criminaldata` (
  `Criminal-ID` int(6) NOT NULL,
  `Address` varchar(40) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Father's Name` varchar(30) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB(yyyy-mm-dd)` varchar(10) NOT NULL,
  `Crimes Done` varchar(40) NOT NULL,
  `Date of Arrest` varchar(10) NOT NULL,
  `Place of Arrest` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `criminaldata`
--

INSERT INTO `criminaldata` (`Criminal-ID`, `Address`, `Phone`, `Name`, `Father's Name`, `Gender`, `DOB(yyyy-mm-dd)`, `Crimes Done`, `Date of Arrest`, `Place of Arrest`) VALUES
(7564, 'jhansi', '324517898', 'david', 'lovely', 'male', '1978-05-03', 'theft', '2008-05-01', 'uttrakhand'),
(8763, '', '', 'jenny', '', '', '', '', '', ''),
(765894, 'durg', '764784598', 'mansi mishra', 'bhartendu mishra', 'female', '2002-09-04', 'fraud', '2020-09-08', 'mumbai'),
(567894, 'mumbai', '9307685943', 'salman khan', 'mr. khan ', 'male', '2002-09-09', 'fraud', '2020-09-09', 'delhi'),
(876546, 'america', '9301821345', 'vijay mallya', 'mr. mallya', 'male', '1978-09-08', 'fraud, loan', '2016-08-09', 'delhi');

-- --------------------------------------------------------

--
-- Table structure for table `missingdata`
--

CREATE TABLE `missingdata` (
  `Report-ID` int(6) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Father's Name` varchar(30) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` varchar(10) NOT NULL,
  `Identification` varchar(50) NOT NULL,
  `Date of Missing` varchar(10) NOT NULL,
  `Place of Missing` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `missingdata`
--

INSERT INTO `missingdata` (`Report-ID`, `Name`, `Father's Name`, `Address`, `Phone`, `Gender`, `DOB`, `Identification`, `Date of Missing`, `Place of Missing`) VALUES
(65474, 'anamika', '', 'delhi', '6547849320', 'female', '1979-03-06', '', '2020-09-09', 'agra'),
(6574, 'priya ', '', '', '', '', '', '', '', ''),
(764754, 'rajesh yadav', '--', '--', '998468647', 'm', '2020-09-08', 'mole', '2020-09-08', 'm'),
(876589, 'salman khan', 'mr. khan', 'mumbai', '930172525', 'male', '1967-09-08', 'mole on nose', '2020-09-08', 'delhi'),
(874, 'shahruk khan', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `user_information`
--

CREATE TABLE `user_information` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_information`
--

INSERT INTO `user_information` (`id`, `first_name`, `last_name`, `gender`, `username`, `password`) VALUES
(15, 'Mansi', 'Mishra', 'Female', 'mansi', 'mansi0904'),
(16, 'Margi', 'Mishra', 'Female', 'Margi', 'margi0306'),
(19, 'Sakshi', 'Mishra', 'Female', 'Sakshi', 'sakshi1907'),
(20, 'Kunjal', 'Ramteke', 'Female', 'Kunjal', '1234'),
(21, 'Pranjal', 'Hinduja', 'Female', 'pranjal', '1234'),
(24, 'munna', 'yadav', 'Male', 'munna', '1234'),
(29, 'papa', 'mishra', 'Male', 'papa', '123'),
(32, 'Mansi', 'Mishra', 'Female', 'man', '12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `criminaldata`
--
ALTER TABLE `criminaldata`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `missingdata`
--
ALTER TABLE `missingdata`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `user_information`
--
ALTER TABLE `user_information`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_information`
--
ALTER TABLE `user_information`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;
