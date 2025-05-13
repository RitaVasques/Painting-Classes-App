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
-- Table structure for table `accounting`
--

CREATE TABLE `accounting` (
  `entry_id` int(255) NOT NULL,
  `student_id` int(255) NOT NULL,
  `date` date NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `accounting`
--

INSERT INTO `accounting` (`entry_id`, `student_id`, `date`, `amount`) VALUES
(6, 1, '2025-05-05', 200),
(7, 1, '2025-01-08', 130),
(8, 1, '2025-02-01', 200),
(9, 2, '2025-05-02', 240),
(10, 2, '2025-04-01', 130),
(12, 3, '2025-01-15', 130),
(13, 3, '2025-02-02', 220),
(14, 2, '2025-01-08', 150),
(15, 4, '2025-01-08', 200),
(16, 1, '2025-03-02', 130),
(17, 1, '2025-04-05', 100),
(18, 2, '2025-02-02', 250),
(19, 2, '2025-03-04', 150),
(20, 3, '2025-03-08', 250),
(21, 3, '2025-04-05', 180),
(23, 7, '2025-01-10', 180),
(24, 7, '2025-02-05', 200);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounting`
--
ALTER TABLE `accounting`
  ADD PRIMARY KEY (`entry_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounting`
--
ALTER TABLE `accounting`
  MODIFY `entry_id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
