-- -----------------------------------------------------
-- Database: alx_book_store
-- -----------------------------------------------------

-- Drop database if it exists
DROP DATABASE IF EXISTS alx_book_store;

-- Create the database
CREATE DATABASE alx_book_store;

-- Use the database
USE alx_book_store;

-- -----------------------------------------------------
-- Table: Authors
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

-- -----------------------------------------------------
-- Table: Books
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- -----------------------------------------------------
-- Table: Customers
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL,
    address TEXT
);

-- -----------------------------------------------------
-- Table: Orders
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- -----------------------------------------------------
-- Table: Order_Details
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Order_Details (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
