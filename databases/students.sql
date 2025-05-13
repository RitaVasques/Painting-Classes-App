-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 13, 2025 at 09:01 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `PaintingStudio_students_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `student_id` int(20) NOT NULL,
  `name` varchar(45) NOT NULL,
  `schedule` varchar(45) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`student_id`, `name`, `schedule`, `email`, `phone`) VALUES
(1, 'Joanna Smith', 'Tuesday Morning', 'joanna_smith@gmail.com', 795885426),
(2, 'Anna Banana', 'Tuesday Morning', 'anna.banana@hotmail.com', 795964723),
(3, 'Alejandra R.S.', 'Thursday Afternoon', 'alexrs@gmail.com', 758664812),
(6, 'Maria Flores', 'Monday Afternoon', 'm_flores@gmail.com', 765334571),
(7, 'Martha Silva', 'Wednesday Morning', 'martha.silva@gmail.com', 786115289),
(9, 'Anna Jones', 'Monday Morning', 'aj@hotmail.com', 759351245),
(10, 'Isabella', 'Johnson', 'isabella.johnson@gmail.co.uk', 758247698);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`student_id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `id` (`student_id`),
  ADD UNIQUE KEY `name_2` (`name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `student_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
