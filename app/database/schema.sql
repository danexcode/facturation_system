CREATE DATABASE IF NOT EXISTS tienda;
USE tienda;

CREATE TABLE IF NOT EXISTS categories(
	id BIGINT AUTO_INCREMENT,
    name VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS products(
	id BIGINT AUTO_INCREMENT,
    category_id BIGINT NOT NULL,
    name VARCHAR(150) NOT NULL,
    stock INT NOT NULL,
    price DOUBLE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE IF NOT EXISTS clients(
	id BIGINT AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dni BIGINT UNIQUE,
    phone VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS orders(
	id BIGINT AUTO_INCREMENT,
    total DOUBLE NOT NULL,
    client_id BIGINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

CREATE TABLE IF NOT EXISTS order_product(
	order_id BIGINT,
    product_id BIGINT,
    amount INT NOT NULL,
    product_price DOUBLE NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO categories (name) VALUES ("Comida");

INSERT INTO products (category_id, name, stock, price) VALUES (1, "Harina PAN 1kg", 500, 1);
INSERT INTO products (category_id, name, stock, price) VALUES (1, "Arroz integral 1kg", 200, 2);
INSERT INTO products (category_id, name, stock, price) VALUES (1, "Espaguetti 1kg", 100, 1.5);

INSERT INTO clients (name, last_name, dni, phone) VALUES ("Daniel", "Rodriguez", 30001938, "1234567");

CREATE USER "user_1"@"192.168.0.101" IDENTIFIED BY "admin1";
GRANT SELECT, INSERT, UPDATE ON *.* TO "user_1"@"192.168.0.101";
FLUSH PRIVILEGES;

CREATE USER "user_2"@"192.168.0.102" IDENTIFIED BY "admin2";
GRANT SELECT, INSERT ON *.* TO "user_2"@"192.168.0.102";
FLUSH PRIVILEGES;

CREATE USER "user_3"@"192.168.0.103" IDENTIFIED BY "admin3";
GRANT SELECT ON *.* TO "user_3"@"192.168.0.103";
FLUSH PRIVILEGES;