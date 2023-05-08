SET SCHEMA 'seminar5';
/*
CREATE TABLE "cars" (
	Id INT NOT NULL PRIMARY KEY,
    Name VARCHAR(45),
    Cost INT );

INSERT INTO cars VALUES
	(1, 'Audi', 52642),
    (2, 'Mercedes', 57127 ),
    (3, 'Skoda', 9000 ),
    (4, 'Volvo', 29000),
	(5, 'Bentley', 350000),
    (6, 'Citroen', 21000 ), 
    (7, 'Hummer', 41400), 
    (8, 'Volkswagen', 21600);

SELECT * FROM cars

CREATE OR REPLACE VIEW CheapCars AS
	SELECT 	* FROM cars 
	WHERE cost < 25000
	ORDER BY cost;

DROP VIEW IF EXISTS CheapCars;
CREATE VIEW CheapCars AS
	SELECT * FROM cars 
	WHERE cost < 30000
	ORDER BY cost;

SELECT * FROM CheapCars

CREATE VIEW SkodaAudi AS
	SELECT * FROM cars 
	WHERE name = 'Skoda' OR name = 'Audi';

SELECT * FROM SkodaAudi

*/	

