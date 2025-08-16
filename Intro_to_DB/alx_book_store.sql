-- CREATE DATABASE
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

-- DROP TABLES IF THEY EXIST
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS publishers;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS order_details;

-- CREATE TABLES
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL
);

CREATE TABLE publishers (
    publisher_id INT PRIMARY KEY,
    publisher_name VARCHAR(255) NOT NULL
);

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215),
    address TEXT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_details (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    book_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- OPTIONAL: INSERT SAMPLE DATA
-- INSERT INTO authors (author_id, author_name) VALUES (1, 'J.K. Rowling');
-- INSERT INTO publishers (publisher_id, publisher_name) VALUES (1, 'Penguin');
-- INSERT INTO books (book_id, title, author_id, price, publication_date) VALUES (1, 'Harry Potter', 1, 20.5, '2000-07-08');
-- INSERT INTO customers (customer_id, customer_name, email, address) VALUES (1, 'Alice', 'alice@example.com', '123 Main St');
-- INSERT INTO orders (order_id, customer_id, order_date) VALUES (1, 1, '2025-08-16');
-- INSERT INTO order_details (order_detail_id, order_id, book_id, quantity) VALUES (1, 1, 1, 2);
