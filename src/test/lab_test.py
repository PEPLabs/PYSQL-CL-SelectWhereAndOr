import unittest

from src.main.employee import Employee
from src.main.lab import problem1, problem2, problem3


class LabTest(unittest.TestCase):
    def test_activity_find_employees_and(self):
        """
        Note the seed data includes a "Steve" at exactly $75000 (id 6). That employee must NOT appear here
        (75000 is not "greater than" 75000) - this is what actually catches a ">=" mistake, since Steve Garcia
        and Steve Jones alone never sit exactly on the $75000 boundary.
        """
        expected_set = {Employee(3, "Steve", "Jones", 99890.99)}

        result_set = problem1()

        self.assertEqual(expected_set, result_set)

    def test_activity_find_employees_or(self):
        """
        Note the seed data includes boundary employees at exactly $100000 (Jordan) and $50000 (Casey). Neither
        should appear here (100000 is not "greater than" 100000, and 50000 is not "less than" 50000) - this is
        what actually catches a ">=" or "<=" mistake on either threshold.
        """
        expected_set = {
            Employee(2, "Alexa", "Smith", 42500),
            Employee(4, "Brandon", "Smith", 120000),
        }

        result_set = problem2()

        self.assertEqual(expected_set, result_set)

    def test_activity_find_employees_not_in(self):
        """
        Note the seed data includes boundary employees at exactly $50000 (Casey) and $75000 (Steve). Casey must
        NOT appear here (50000 is not "greater than" 50000), and the Steve boundary employee is excluded
        anyway by the NOT IN clause - this is what actually catches a ">=" mistake on the $50000 threshold.
        """
        expected_set = {
            Employee(5, "Adam", "Jones", 55050.50),
            Employee(4, "Brandon", "Smith", 120000),
            Employee(8, "Jordan", "Reyes", 100000.00),
        }

        result_set = problem3()

        self.assertEqual(expected_set, result_set)


if __name__ == "__main__":
    unittest.main()
