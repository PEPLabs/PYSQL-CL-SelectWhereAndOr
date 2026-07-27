# Background

SQL sublanguage: DQL (Data Query Language)

Any time we are using WHERE to filter our result set, we can use logical operators such as AND and OR.

SELECT * FROM employee WHERE last_name = 'Jones' OR first_name = 'Steve';

A few more examples:

SELECT * FROM table WHERE condition1 = value1 AND condition2 = value2;
SELECT * FROM table WHERE something > 500 OR something < 100;
SELECT * FROM table WHERE value NOT IN ('value1', 'value2');

## Problem 1

Assume the following table already exists.

| id | first_name | last_name | salary |
|----|------------|-----------|--------|
| 1 | Steve | Garcia | 67400.00 |
| 2 | Alexa | Smith | 42500.00 |
| 3 | Steve | Jones | 99890.99 |
| 4 | Brandon | Smith | 120000 |
| 5 | Adam | Jones | 55050.50 |

Write a statement in `problem1.sql` that will query the above table for all employees named 'Steve' who earn
more than $75,000.

## Problem 2

Using the same table above, write a statement in `problem2.sql` that will query for all employees who earn more
than $100,000 or less than $50,000.

## Problem 3

Using the same table above, write a statement in `problem3.sql` that will query for all employees who earn more
than $50,000 and are NOT named 'Steve'. Hint: look up the NOT and IN logical operators.
