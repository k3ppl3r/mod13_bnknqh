import unittest
import re
from datetime import datetime

#validation functions
def validate_symbol(symbol: str) -> bool:
    """
    Symbol must be capitalized A–Z letters, length 1–7.
    """
    return bool(re.fullmatch(r"[A-Z]{1,7}", symbol))


def validate_chart_type(chart_type: str) -> bool:
    """
    Chart type must be '1' or '2'.
    """
    return chart_type in ["1", "2"]


def validate_time_series(time_series: str) -> bool:
    """
    Time series must be 1, 2, 3, or 4.
    """
    return time_series in ["1", "2", "3", "4"]


def validate_date(date_string: str) -> bool:
    """
    Date must be in YYYY-MM-DD format.
    """
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestProject3Inputs(unittest.TestCase):

    #symbol test
    def test_valid_symbol(self):
        self.assertTrue(validate_symbol("A"))
        self.assertTrue(validate_symbol("TSLA"))
        self.assertTrue(validate_symbol("ABCDEFG"))

    def test_invalid_symbol_lowercase(self):
        self.assertFalse(validate_symbol("tsla"))

    def test_invalid_symbol_too_long(self):
        self.assertFalse(validate_symbol("ABCDEFGH"))  # 8 letters

    def test_invalid_symbol_with_numbers(self):
        self.assertFalse(validate_symbol("AAPL1"))

    def test_invalid_symbol_empty(self):
        self.assertFalse(validate_symbol(""))

    #chart type test
    def test_valid_chart_type(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))

    def test_invalid_chart_type(self):
        self.assertFalse(validate_chart_type("0"))
        self.assertFalse(validate_chart_type("3"))
        self.assertFalse(validate_chart_type("10"))
        self.assertFalse(validate_chart_type(""))

    #time series test
    def test_valid_time_series(self):
        for t in ["1", "2", "3", "4"]:
            self.assertTrue(validate_time_series(t))

    def test_invalid_time_series(self):
        self.assertFalse(validate_time_series("5"))
        self.assertFalse(validate_time_series("0"))
        self.assertFalse(validate_time_series(""))
        self.assertFalse(validate_time_series("13"))

    #date test
    def test_valid_date(self):
        self.assertTrue(validate_date("2023-01-01"))
        self.assertTrue(validate_date("1999-12-31"))

    def test_invalid_date_format(self):
        self.assertFalse(validate_date("01-01-2023"))
        self.assertFalse(validate_date("2023/01/01"))
        self.assertFalse(validate_date("20230101"))

    def test_invalid_date_values(self):
        self.assertFalse(validate_date("2023-13-01"))  # invalid month
        self.assertFalse(validate_date("2023-00-10"))  # invalid month
        self.assertFalse(validate_date("2023-02-30"))  # invalid day

    def test_empty_date(self):
        self.assertFalse(validate_date(""))

if __name__ == "__main__":
    unittest.main()