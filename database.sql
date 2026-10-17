CREATE DATABASE maintenance_system;
CREATE TABLE machine_master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    machine_code VARCHAR(20),
    machine_name VARCHAR(100),
    department VARCHAR(50),
    status VARCHAR(20)
);
CREATE TABLE operator_master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(20),
    operator_name VARCHAR(100),
    department VARCHAR(50),
    username VARCHAR(50),
    password VARCHAR(100),
    status VARCHAR(20)
);
CREATE TABLE technician_master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tech_id VARCHAR(20),
    technician_name VARCHAR(100),
    skill VARCHAR(50),
    department VARCHAR(50),
    status VARCHAR(20)
);
CREATE TABLE problem_master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    problem_code VARCHAR(20),
    problem_name VARCHAR(100),
    department VARCHAR(50),
    status VARCHAR(20)
);
