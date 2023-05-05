SELECT 	color, 
		mark, 
		count(*)
FROM auto
WHERE mark IN ('BMW', 'LADA')
GROUP BY color, mark;

SELECT 
	DISTINCT 
		mark, 
		(select count(*) 
			FROM auto a_tmp 
			WHERE a_tmp.mark != a.mark) AS Other_count 
FROM auto a;
