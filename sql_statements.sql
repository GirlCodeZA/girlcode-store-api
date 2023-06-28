-- Create Categories Table
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    cat_name TEXT NOT NULL UNIQUE,
    slug TEXT NOT NULL UNIQUE,
    cat_desc TEXT
);

-- Insert Initial Categories
INSERT INTO categories (cat_name, slug)
VALUES ('Furniture', 'furniture'),
	('Hand Bag', 'hand-bag'),
	('Books', 'books'),
	('Tech', 'tech'),
	('Sneakers', 'sneakers'),
	('Travel', 'travel');
	
-- Add cat_img column on categories
ALTER TABLE categories
ADD cat_img TEXT;

-- Updated cat_img column for all rows
UPDATE categories
SET cat_img='cats_img.jpg';

-- Create Products table
CREATE TABLE products (
	id SERIAL PRIMARY KEY,
	prod_name TEXT NOT NULL UNIQUE,
	prod_img TEXT NOT NULL UNIQUE,
	prod_desc TEXT,
	prod_slug TEXT NOT NULL UNIQUE,
	prod_price DOUBLE PRECISION NOT NULL 
);

INSERT INTO products (prod_name, prod_img, prod_desc, prod_slug, prod_price)
VALUES ('Insta Mini 9', 'insta-mini-9.png', 'Selfie mode and selfie mirrow, Macro mode', 'insta-mini-9', 99.85);
