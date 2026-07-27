import os
import sqlite3

from src.main.employee import Employee

"""
SQL sublanguage: DQL (Data Query Language)

Any time we are using WHERE to filter our results set, we can use logical operators, for instance: AND, OR.

Consider the example:
     SELECT * FROM employee WHERE last_name = 'Jones' OR first_name = 'Steve';

Here are a few examples of using some logical operators in a WHERE clause:
     SELECT * FROM table WHERE condition1 = value1 AND condition2 = value2;
     SELECT * FROM table WHERE something > 500 OR something < 100;
     SELECT * FROM table WHERE value NOT IN ('value1', 'value2');
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()



def _seeded_connection():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE employee(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        salary DOUBLE PRECISION
    );
    """)
    cur.execute(
        "INSERT INTO employee (first_name, last_name, salary) VALUES "
        "('Steve', 'Garcia', 67400.00),"
        "('Alexa', 'Smith', 42500.00),"
        "('Steve', 'Jones', 99890.99),"
        "('Brandon', 'Smith', 120000),"
        "('Adam', 'Jones', 55050.50),"
        # boundary rows below - each sits exactly on a threshold used somewhere in this lab, and each also
        # matches every OTHER condition in the query it's meant to test, so it actually catches ">" vs ">="
        # (and "<" vs "<=") mistakes instead of being silently filtered out for an unrelated reason:
        "('Steve', 'Cutoff75', 75000.00),"
        "('Casey', 'Cutoff50', 50000.00),"
        "('Jordan', 'Cutoff100', 100000.00);"
    )
    conn.commit()
    return conn, cur


def problem1():
    """
    employee table
    |  id  |   first_name   |   last_name   |  salary  |
    --------------------------------------------------
    |1     |'Steve'         |'Garcia'       |67400.00  |
    |2     |'Alexa'         |'Smith'        |42500.00  |
    |3     |'Steve'         |'Jones'        |99890.99  |
    |4     |'Brandon'       |'Smith'        |120000    |
    |5     |'Adam'          |'Jones'        |55050.50  |
    |6     |'Casey'         |'Boundary'     |75000.00  |

    Problem 1: Write a statement that will query the above table for all employees named 'Steve' who earn
    more than $75,000.
    """
    sql = _read_sql("problem1.sql")

    conn, cur = _seeded_connection()

    results_set = set()
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            results_set.add(Employee(row[0], row[1], row[2], row[3]))
    except Exception as e:
        print(f"problem1: {e}\n")
    finally:
        conn.close()

    return results_set


def problem2():
    """
    Problem 2: Write a statement that will query the above table for all employees who earn more than $100,000 or
    less than $50,000
    """
    sql = _read_sql("problem2.sql")

    conn, cur = _seeded_connection()

    results_set = set()
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            results_set.add(Employee(row[0], row[1], row[2], row[3]))
    except Exception as e:
        print(f"problem2: {e}\n")
    finally:
        conn.close()

    return results_set


def problem3():
    """
    Problem 3: Write a statement that will query the above table for all employees who earn more than $50,000 and
    are NOT named 'Steve'
    Hint: Look up the NOT and IN logical operators.
    """
    sql = _read_sql("problem3.sql")

    conn, cur = _seeded_connection()

    results_set = set()
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            results_set.add(Employee(row[0], row[1], row[2], row[3]))
    except Exception as e:
        print(f"problem3: {e}\n")
    finally:
        conn.close()

    return results_set
