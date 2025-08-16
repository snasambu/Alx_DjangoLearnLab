-- Create the database
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

-- Example table for books
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    published_date DATE
);

-- Example insert
INSERT INTO books (title, author, price, published_date) VALUES
('The Alx Guide', 'Snasambu', 29.99, '2025-01-01'),
('Python Basics', 'OpenAI', 39.99, '2025-02-01');
