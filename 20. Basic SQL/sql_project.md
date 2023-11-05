# Basic SQL (PostgreSQL)

## Course Topics
1. Introduction to databases(SELECT, FROM)
2. Data slices in SQL (LIMIT, OFFSET, CAST, data type, WHERE, primary and foreign keys, BOOL, IN, LIKE, BETWEEN, date, CASE)
3. Aggregating functions. Grouping and sorting data (math and aggregating operations, GROUP BY, ORDER BY, HAVING, AS)
4. Relationships between tables. Types of table joins (one-to-one, one-to-many, many-to-many, ER diagrams, JOIN, UNION)
5. Subqueries and temporary tables (sub FROM,sub WHERE,sub JOIN, WITH, operator execution order, variability)
6. PySpark (scaling, resilient distributed datasets, dataframes, missing values, spark.sql)
7. Data schemas and window functions (OVER, PARTITION BY, ORDER BY, RANK, NTILE, agg. window func., LEAD, LAG)

Project database stores information about venture funds and investments in startup companies. This database is based on the [Startup Investments](https://www.kaggle.com/datasets/justinas/startup-investments) dataset published on the popular data mining competition platform Kaggle.

![](1_Baza_dannykh_1673427255.png)

## Table of contents:

- primary key id - identifier or unique purchase number;
- foreign key acquiring_company_id - refers to the company table - the identifier of the acquiring company, that is, the one that buys another company;
- foreign key acquired_company_id - refers to the company table - the identifier of the company that is being purchased;
- term_code — transaction payment method:
	- cash - in cash;
	- stock - company shares;
	- cash_and_stock - mixed.
- price_amount — purchase amount in dollars;
- acquired_at — transaction date;
- created_at — date and time of creation of a record in the table;
- updated_at — date and time the record in the table was updated.

**company**

Contains information about startup companies.

- primary key id - identifier, or unique company number;
- name — company name;
- category_code — category of the company’s activity, for example:
	- news - specializes in working with news;
	- social - specializes in social work.
- status — company status:
	- acquired - acquired;
	- operating - operates;
	- ipo - went to IPO;
	- closed - ceased to exist.
- founded_at — date of foundation of the company;
- closed_at — company closing date, which is indicated if the company no longer exists;
- domain — domain of the company website;
- twitter_username — the name of the company’s Twitter profile;
- country_code — country code, for example, USA for the USA, GBR for the UK;
- investment_rounds — the number of rounds in which the company participated as an investor;
- funding_rounds — the number of rounds in which the company attracted investments;
- funding_total — the amount of attracted investments in dollars;
- milestones — the number of important stages in the company’s history;
- created_at — date and time of creation of a record in the table;
- updated_at — date and time the record in the table was updated.

**education**

Stores information about the educational level of company employees.

- primary key id - unique record number with information about education;
- foreign key person_id - refers to the people table - identifier of the person whose information is presented in the record;
- degree_type — academic degree, for example:
	- BA - Bachelor of Arts
	- MS - Master of Scienc
- instituition - educational institution, name of the university;
- graduated_at — date of completion of training, graduation;
- created_at — date and time of creation of a record in the table;
- updated_at — date and time the record in the table was updated.

**fund**

Stores information about venture funds.

- primary key id - unique number of the venture fund;
- name — name of the venture fund;
- founded_at — fund foundation date;
- domain — domain of the fund’s website;
- twitter_username — fund’s Twitter profile;
- country_code — fund country code;
- investment_rounds — the number of investment rounds in which the fund took part;
- invested_companies — the number of companies in which the fund has invested;
- milestones — the number of important stages in the fund’s history;
- created_at — date and time of creation of a record in the table;
- updated_at — date and time the record in the table was updated.

**funding_round**

Contains information about investment rounds.

- primary key id - unique number of the investment round;
- foreign key company_id - refers to the company table - a unique number of the company that participated in the investment round;
- funded_at — date of the round;
- funding_round_type — type of investment round, for example:
	- venture - venture round;
	- angel - angel round;
	- series_a — round A.
- raised_amount — the amount of investment that the company raised in this round in dollars;
- pre_money_valuation — preliminary assessment of the company’s value in dollars, carried out before investment;
- participants — number of participants in the investment round;
- is_first_round — whether this round is the first for the company;
- is_last_round — whether this round is the last for the company;
- created_at — date and time of creation of a record in the table;
- updated_at — date and time the record in the table was updated.

**investment**

Contains information about investments of venture funds in startup companies.

- primary key id - unique investment number;
- foreign key funding_round_id - refers to the table funding_round - unique number of the investment round;
- foreign key company_id - refers to the company table - the unique number of the startup company in which they invest;
- foreign key fund_id - refers to the fund table - the unique number of the fund investing in the startup company;
- created_at — date and time of creation of a record in the table;
- updated_at — date and time the record in the table was updated.

**people**

Contains information about employees of startup companies.

- primary key id - unique employee number;
- first_name — employee name;
- last_name — employee’s last name;
- foreign key company_id - refers to the company table - a unique number of the startup company;
- twitter_username — employee’s Twitter profile;
- created_at — date and time of creation of a record in the table;
- updated_at — date and time the record in the table was updated.

## Task 1. 
Count how many companies have closed.

```sql
SELECT COUNT(status)
FROM company
WHERE status = 'closed'
```

## Task 2. 
Display the number of funds raised for US news companies. Use data from the company table. Sort the table in descending order of the values in the funding_total field.

```sql
SELECT funding_total
FROM company
WHERE category_code = 'news' AND country_code = 'USA'
ORDER BY funding_total DESC
```

## Task 3. 
Find the total dollar amount of transactions involving the purchase of one company by another. Select transactions that were carried out only in cash from 2011 to 2013 inclusive.

```sql
SELECT SUM(price_amount)
FROM acquisition
WHERE term_code = 'cash' and EXTRACT(YEAR FROM acquired_at) BETWEEN 2011 AND 2013
```

## Task 4. 
Display the first name, last name, and Twitter account names of people whose account names begin with 'Silver'.

```sql
SELECT first_name, last_name, twitter_username
FROM people
WHERE twitter_username LIKE 'Silver%'
```

## Task 5. 
Display all the information about people whose Twitter account names contain the substring 'money' and whose last name begins with 'K'.

```sql
SELECT *
FROM people
WHERE twitter_username LIKE '%money%' AND last_name LIKE 'K%'
```

## Task 6. 
For each country, display the total amount of investment raised by companies registered in that country. The country in which the company is registered can be determined by the country code. Sort the data in descending order of amount.

```sql
SELECT country_code, SUM(funding_total)
FROM company
GROUP BY country_code
ORDER BY sum DESC
```

## Task 7. 
Make a table that includes the date of the round, as well as the minimum and maximum values of the amount of investment raised on this date.

Leave in the final table only those records in which the minimum value of the investment amount is not equal to zero and not equal to the maximum value.

```sql
SELECT funded_at, MIN(raised_amount), MAX(raised_amount)
FROM funding_round
GROUP BY funded_at
HAVING MIN(raised_amount) != 0 AND MIN(raised_amount) != MAX(raised_amount)
```

## Task 8. 
Create categories:
- For funds that invest in 100 or more companies, assign the category high_activity.
- For funds that invest in 20 or more companies up to 100, assign the middle_activity category.
- If the number of invested fund companies does not reach 20, assign the category low_activity.

```sql
SELECT *,
    CASE
        WHEN invested_companies > 100 THEN 'high_activity'
        WHEN invested_companies > 19 THEN 'middle_activity'
        ELSE 'low_activity'
    END
FROM fund
```

## Task 9. 
For each of the categories assigned in the previous task, calculate the average number of investment rounds in which the fund participated, rounded to the nearest whole number. Display categories and average number of investment rounds. Sort the table in ascending order of average.

```sql
SELECT CASE
           WHEN invested_companies>=100 THEN 'high_activity'
           WHEN invested_companies>=20 THEN 'middle_activity'
           ELSE 'low_activity'
       END AS activity,
   ROUND(AVG(investment_rounds)) as avg
FROM fund
GROUP BY activity
ORDER BY avg;
```

## Task 10. 
Analyze in which countries the funds that most often invest in startups are located.

For each country, calculate the minimum, maximum and average number of companies in which funds in that country invested, founded from 2010 to 2012 inclusive. Exclude countries with funds whose minimum number of companies receiving investments is zero.

Unload the ten most active investing countries: sort the table by average number of companies from largest to smallest. Then add sorting by country code in lexicographical order.

```sql
SELECT country_code,
    MIN(invested_companies),
    MAX(invested_companies),
    AVG(invested_companies)
FROM fund
WHERE EXTRACT(YEAR FROM founded_at) BETWEEN 2010 AND 2012
GROUP BY country_code
HAVING MIN(invested_companies) != 0
ORDER BY avg DESC, country_code
LIMIT 10
```

## Task 11. 
Display the first and last name of all startup employees. Add a field with the name of the educational institution from which the employee graduated, if this information is known.

```sql
SELECT p.first_name, p.last_name, e.instituition
FROM people as p
LEFT JOIN (SELECT person_id, instituition FROM education) as e ON p.id = e.person_id
```

## Task 12. 
For each company, find the number of educational institutions that its employees graduated from. Print the company name and the number of unique names of educational institutions. List the top 5 companies by number of universities.

```sql
SELECT c.name, COUNT(DISTINCT e.instituition)
FROM company as c
INNER JOIN (SELECT id, company_id FROM people) AS p ON c.id = p.company_id
INNER JOIN (SELECT person_id, instituition FROM education) AS e ON p.id = e.person_id
GROUP BY c.name
ORDER BY count DESC
LIMIT 5;
```

## Task 13. 
Make a list of unique names of closed companies whose first round of funding was their last.

```sql
SELECT DISTINCT c.name
FROM company as c
INNER JOIN (SELECT DISTINCT company_id FROM funding_round 
            WHERE is_first_round = 1 AND is_last_round = 1) AS fr ON c.id = fr.company_id
WHERE c.status = 'closed'
```

## Task 14. 
Make a list of unique numbers of employees who work in the companies selected in the previous task.

```sql
SELECT DISTINCT p.id
FROM company as c
INNER JOIN (SELECT DISTINCT company_id FROM funding_round 
            WHERE is_first_round = 1 AND is_last_round = 1) AS fr ON c.id = fr.company_id
INNER JOIN (SELECT id, company_id FROM people) AS p ON c.id = p.company_id
WHERE c.status = 'closed'
```

## Task 15. 
Make a table that includes unique pairs with employee numbers from the previous task and the educational institution from which the employee graduated.

```sql
SELECT p.id, e.instituition
FROM company as c
INNER JOIN (SELECT DISTINCT company_id FROM funding_round 
            WHERE is_first_round = 1 AND is_last_round = 1) AS fr ON c.id = fr.company_id
INNER JOIN (SELECT id, company_id FROM people) AS p ON c.id = p.company_id
INNER JOIN (SELECT person_id, instituition FROM education) AS e ON p.id = e.person_id
WHERE c.status = 'closed'
GROUP BY p.id, e.instituition
```

## Task 16. 
Count the number of educational institutions for each employee from the previous task. When calculating, keep in mind that some employees could graduate from the same institution twice.

```sql
SELECT p.id, COUNT(e.instituition)
FROM company as c
INNER JOIN (SELECT DISTINCT company_id FROM funding_round 
            WHERE is_first_round = 1 AND is_last_round = 1) AS fr ON c.id = fr.company_id
INNER JOIN (SELECT id, company_id FROM people) AS p ON c.id = p.company_id
INNER JOIN (SELECT person_id, instituition FROM education) AS e ON p.id = e.person_id
WHERE c.status = 'closed'
GROUP BY p.id
```

## Task 17. 
Complete the previous query and display the average number of educational institutions (all, not just unique ones) that employees of different companies graduated from. You only need to display one record; grouping is not needed here.

```sql
SELECT AVG(i.count) FROM(
SELECT p.id, COUNT(e.instituition)
FROM company as c
INNER JOIN (SELECT DISTINCT company_id FROM funding_round 
            WHERE is_first_round = 1 AND is_last_round = 1) AS fr ON c.id = fr.company_id
INNER JOIN (SELECT id, company_id FROM people) AS p ON c.id = p.company_id
INNER JOIN (SELECT person_id, instituition FROM education) AS e ON p.id = e.person_id
WHERE c.status = 'closed'
GROUP BY p.id) as i
```

## Task 18. 
Write a similar query: print the average number of educational institutions (all, not just unique ones) that Facebook employees graduated from.

```sql
SELECT AVG(i.count) FROM(
SELECT p.id, COUNT(e.instituition)
FROM company as c
INNER JOIN (SELECT DISTINCT company_id FROM funding_round) AS fr ON c.id = fr.company_id
INNER JOIN (SELECT id, company_id FROM people) AS p ON c.id = p.company_id
INNER JOIN (SELECT person_id, instituition FROM education) AS e ON p.id = e.person_id
WHERE c.name = 'Facebook'
GROUP BY p.id) as i
```

## Task 19. 
Make a table from the fields:

- name_of_fund — name of the fund;
- name_of_company — company name;
- amount — the amount of investment that the company attracted in the round.

The table will include data on companies whose history had more than six important stages, and funding rounds took place from 2012 to 2013 inclusive.

```sql
SELECT f.name as name_of_fund, c.name as name_of_company, fr.raised_amount as amount
FROM fund as f
INNER JOIN (SELECT fund_id, funding_round_id, company_id FROM investment) AS i ON f.id = i.fund_id
INNER JOIN (SELECT id, raised_amount, funded_at FROM funding_round) AS fr ON i.funding_round_id = fr.id
INNER JOIN (SELECT id, name, milestones FROM company) AS c ON i.company_id = c.id
WHERE c.milestones > 6 AND EXTRACT(YEAR FROM fr.funded_at) BETWEEN 2012 AND 2013
```

## Task 20. 
Unload a table containing the following fields:
- name of the purchasing company;
- transaction amount;
- the name of the company that was purchased;
- the amount of investment made in the acquired company;
- a share that reflects how many times the purchase amount exceeded the amount of investment made in the company, rounded to the nearest whole number.

Do not take into account those transactions in which the purchase amount is zero. If the amount invested in a company is zero, exclude that company from the table.

Sort the table by transaction amount from highest to lowest, and then by the name of the purchased company in lexicographic order. Limit the table to the first ten records.

```sql
SELECT c1.name AS acquiring, 
    a.price_amount, 
    c2.name AS acquired, 
    c2.investments, 
    ROUND(a.price_amount/(c2.investments)) AS price_to_investments
FROM acquisition AS a
JOIN (SELECT id, name FROM company) AS c1 ON a.acquiring_company_id = c1.id
JOIN (SELECT id, name, funding_total AS investments FROM company) AS c2 ON a.acquired_company_id = c2.id
WHERE a.price_amount > 0 AND c2.investments > 0
ORDER BY a.price_amount DESC
LIMIT 10;
```

## Task 21. 
Unload a table that will include the names of companies from the social category that received funding from 2010 to 2013 inclusive. Check that the investment amount is not zero. Also print the number of the month in which the funding round took place.

```sql
SELECT c.name, EXTRACT(MONTH FROM fr.funded_at)
FROM company as c
JOIN (SELECT company_id, funded_at, raised_amount FROM funding_round) AS fr ON c.id = fr.company_id
WHERE c.category_code = 'social' AND EXTRACT(YEAR FROM funded_at) BETWEEN 2010 AND 2013 AND c.funding_total > 0 AND fr.raised_amount > 0
ORDER BY name
```

## Task 22. 
Select data by month from 2010 to 2013 when investment rounds took place. Group the data by month number and get a table containing the following fields:

- number of the month in which the rounds took place;
- number of unique US fund names that invested this month;
- number of companies purchased this month;
- total amount of purchase transactions this month.

```sql
WITH a AS (
    SELECT EXTRACT(MONTH FROM acquired_at) AS month, COUNT(*) AS sells, SUM(price_amount) AS sums
    FROM acquisition
    WHERE EXTRACT(YEAR FROM acquired_at) BETWEEN 2010 AND 2013
    GROUP BY month
),
b AS (SELECT EXTRACT(MONTH FROM fr.funded_at) AS months, 
    COUNT(DISTINCT i.fund_id) AS funds
FROM funding_round AS fr
JOIN investment AS i ON fr.id = i.funding_round_id
JOIN fund as f ON i.fund_id = f.id
WHERE EXTRACT(YEAR FROM fr.funded_at) BETWEEN 2010 AND 2013 AND f.country_code = 'USA'
GROUP BY months)
SELECT month, funds, sells, sums
FROM b
JOIN a ON a.month = b.months
```

## Task 23. 
Compile a pivot table and display the average investment amount for countries that have startups registered in 2011, 2012 and 2013. Data for each year should be in a separate field. Sort the table by average investment for 2011 from highest to lowest.

```sql
SELECT
  country_code,
  COALESCE(AVG(CASE WHEN EXTRACT(YEAR FROM founded_at) = 2011 THEN funding_total END), 0) AS avg_funding_2011,
  COALESCE(AVG(CASE WHEN EXTRACT(YEAR FROM founded_at) = 2012 THEN funding_total END), 0) AS avg_funding_2012,
  COALESCE(AVG(CASE WHEN EXTRACT(YEAR FROM founded_at) = 2013 THEN funding_total END), 0) AS avg_funding_2013
FROM company
WHERE EXTRACT(YEAR FROM founded_at) BETWEEN 2011 AND 2013
GROUP BY country_code
HAVING SUM(CASE WHEN EXTRACT(YEAR FROM founded_at) BETWEEN 2011 AND 2013 THEN funding_total ELSE 0 END) > 0
ORDER BY avg_funding_2011 DESC;
```