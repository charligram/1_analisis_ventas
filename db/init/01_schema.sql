CREATE TABLE product (
    product_id VARCHAR(200) PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(100),
    subcategory VARCHAR(100)
);

CREATE TABLE geography (
    geography_id SERIAL PRIMARY KEY,
    country VARCHAR(50),
    city VARCHAR(50),
    "state" VARCHAR(50),
    region VARCHAR(50),
    postal_code VARCHAR(50)
);

CREATE TABLE customer (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE sale (
    sale_id SERIAL PRIMARY KEY,
    order_id VARCHAR(100),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    segment VARCHAR(50),
    product_id VARCHAR(200),
    geography_id int,
    customer_id VARCHAR(50),
    sales NUMERIC(15, 4),

    FOREIGN KEY (product_id) REFERENCES product(product_id),
    FOREIGN KEY (geography_id) REFERENCES geography(geography_id),
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
);