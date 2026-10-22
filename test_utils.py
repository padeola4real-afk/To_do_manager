import unittest
import io
from datetime import date
from unittest.mock import patch

from utils import(
    date_calculator,
    get_description,
    validate_input,
    get_date,
    header_printer 
)



class TestDateCalculator(unittest.TestCase):

    def test_no_due_date(self):
        result = date_calculator(None)
        self.assertEqual(result, "N/A")


    def test_due_today(self):
        today = date.today()
        result = date_calculator(today)
        self.assertEqual(result, "Due Today")

    def test_over_due(self):
        past_date = date(2026, 10, 19)
        result = date_calculator(past_date)
        self.assertEqual(result, "Overdue by 2 days")

    def test_due_in_two_days(self):
        due_date = date(2026, 10, 23)
        result = date_calculator(due_date)
        self.assertEqual(result, "2 days")

class TestGetDescription(unittest.TestCase):

    def test_valid_description(self):

        with patch("builtins.input", return_value="Buy Food"):
            result = get_description()

        self.assertEqual(result, "Buy Food")

    def test_remove_extra_spaces(self):
        with patch("builtins.input", return_value="Buy      Food        "):
            result = get_description()

        self.assertEqual(result, "Buy Food")


    def test_empty_input(self):
        with patch("builtins.input", side_effect=["", "Valid"]):
            result = get_description()
        self.assertEqual(result, "Valid")

    def test_reject_over_30_chars(self):
        with patch("builtins.input", side_effect=["hello this text is greater than 30 character, I am just testing to see if get_description work", "yes it worked"]):
            result = get_description()
        self.assertEqual(result, "yes it worked")


class TestValidateInput(unittest.TestCase):

    def test_valid_input(self):
        with patch("builtins.input", return_value="2"):
            result = validate_input("Enter", 3)
        self.assertEqual(result, 2)

    def test_input_greater_than_valid_range(self):
        with patch("builtins.input", side_effect=["7", "3"]):
            result = validate_input("Enter: ", 5)

        self.assertEqual(result, 3)

    def test_valid_text(self):
        with patch("builtins.input", side_effect=["hello", "4"]):
            result = validate_input("Enter: ", 7)
        self.assertEqual(result, 4)


class  TestGetDate(unittest.TestCase):

    def test_skip_due_date(self):
        with patch("builtins.input", return_value=""):
            result = get_date()
        self.assertIsNone(result)

    def test_past_date(self):
        with patch("builtins.input", side_effect=["19/10/2026", "22/10/2026"]):
            result = get_date()
        self.assertEqual(result, date(2026, 10, 22))

    def test_valid_date(self):
        with patch("builtins.input", return_value="23/10/2026"):
            result = get_date()
        self.assertEqual(result, date(2026, 10, 23))


class TestHeaderPrinter(unittest.TestCase):

    def test_header_printer(self):
        with patch("sys.stdout", new_callable=io.StringIO) as output:
            header_printer("MY TASK MANAGER")

        expected = (
            "=" * 115 + "\n"
            + "MY TASK MANAGER".center(115) + "\n"
            + "=" * 115 + "\n"
            + "\n"
        )

        self.assertEqual(output.getvalue(), expected)

if __name__ == "__main__":
    unittest.main()