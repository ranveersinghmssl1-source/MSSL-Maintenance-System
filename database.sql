CREATE DATABASE maintenance_system;
CREATE TABLE machine_master (
    id INT AUTO_INCREMENT PRIMARY KEY,
    machine_code VARCHAR(20),
    machine_name VARCHAR(100),
    department VARCHAR(50),
    status VARCHAR(20)
);
