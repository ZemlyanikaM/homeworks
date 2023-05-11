SET SCHEMA 'seminar6';
CREATE OR REPLACE FUNCTION evennums()
RETURNS SETOF int
LANGUAGE plpgsql AS
$func$
DECLARE 
	num INT default 2;
BEGIN
		WHILE (num <= 10) LOOP
		RETURN NEXT num;
		num = num+2;
	END LOOP;
END;
$func$;

SELECT evennums();