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

