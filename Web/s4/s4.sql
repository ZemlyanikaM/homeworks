-- create
CREATE TABLE students (
  stId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  adress TEXT NOT NULL
);

-- insert
INSERT INTO students VALUES (1, 'Sophie', 26, 'Moscow, anystreet, anyhouse');
INSERT INTO students VALUES (2, 'Denis', 34, 'Tula, anystreet, anyhouse');
INSERT INTO students VALUES (3, 'Sergey',38, 'Sochi, anystreet, anyhouse');


-- fetch 
SELECT * FROM students;