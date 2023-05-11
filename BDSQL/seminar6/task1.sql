SET SCHEMA 'seminar6';
CREATE OR REPLACE FUNCTION timeconverter(seconds INT)
RETURNS SETOF int LANGUAGE plpgsql AS
$func$
DECLARE 
	days INT default 0;
    hours INT default 0;
    minutes INT default 0;
BEGIN
    WHILE seconds >= 86400 LOOP
    	days = seconds / 86400;
    	seconds = seconds % 86400;
    END LOOP;
	RETURN NEXT days;

    WHILE seconds >= 3600 LOOP
    	hours = seconds / 3600;
    	seconds = seconds % 3600;
    END LOOP;
	RETURN NEXT hours;

    WHILE seconds >= 60 LOOP
    	minutes = seconds / 60;
    	seconds = seconds % 60;
    END LOOP;
	RETURN NEXT minutes;
	RETURN next seconds;
END;
$func$;

SELECT timeconverter(123456);