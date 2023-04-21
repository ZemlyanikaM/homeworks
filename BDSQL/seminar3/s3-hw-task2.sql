-- 1. Отсортируйте поле “зарплата” в порядке убывания и возрастания
SELECT *
FROM employees
ORDER by salary ;

SELECT *
FROM employees
ORDER by salary DESC;

-- 2. Отсортируйте по возрастанию поле “Зарплата” и выведите 5 строк с наибольшей заработной платой (возможен подзапрос)
SELECT *
FROM employees
ORDER by salary DESC
LIMIT 5;

--3. Выполните группировку всех сотрудников по специальности , суммарная зарплата которых превышает 100000
SELECT speciality, SUM(salary) AS salary_sum
FROM employees
GROUP BY speciality
HAVING SUM(salary) > 100000;

