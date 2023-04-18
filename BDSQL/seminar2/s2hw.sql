-- Task 1

CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    count INT,
    price DECIMAL(10,2)
);

INSERT INTO sales (name, count, price)
VALUES
('n1', 54, 10.50),
('n2', 97, 23.00),
('n3', 256, 15.75),
('n4', 168, 9.99),
('n5', 315, 55.00),
('n6', 32, 17.50),
('n7', 101, 17.50),
('n8', 456, 17.50),
('n9', 321, 17.50);

-- Task 2

SELECT
    CASE
        WHEN count < 100 THEN '<100'
        WHEN count BETWEEN 100 AND 300 THEN '100-300'
        ELSE '>300'
    END AS segments,
    COUNT(*) AS segments_count
FROM
    sales
GROUP BY
    segments;

-- Task 3

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    client VARCHAR(20) NOT NULL,
    price DECIMAL(9,2) NOT NULL,
    status INT NOT NULL DEFAULT 5
);

INSERT INTO orders (client, price, status)
VALUES
('c1', 100, 0),
('c2', 876, 1),
('c3', 1234, 1),
('c4', 98765, 1),
('c5', 3456, -1),
('c6', 8765, 0),
('c7', 8765, 7);

SELECT id, client, price,
    CASE
    	WHEN status < 0 THEN "The order cancelled"
    	WHEN status = 0 THEN "The order opened. Not paid"
    	WHEN status = 1 THEN "The order paid"
        ELSE "Something wrong. Check the order."
    END AS 'order status'
FROM orders;


-- Task 4

0 - значение типа INT и ему подобных, может быть и символом.
NULL - условное "ничто", то есть пустое значение, отсутствие значения, такой специальный тип для ничего )
