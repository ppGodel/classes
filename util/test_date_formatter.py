from datetime import datetime
from unittest import TestCase

from util.date_formatter import convert_str_date, convert_date_str


class TestDate_formatter(TestCase):
    def test_convert_str_date(self):
        expected_date = datetime(2019, 1, 1, 0, 1)
        date = convert_str_date('2019-01-01')
        self.assertEqual(expected_date, date)

    def test_convert_str_date_wrong(self):
        self.assertRaises(ValueError, convert_str_date, 'not a date')

    def test_convert_date_str(self):
        expected_date = '2019-01-01'
        str_date = convert_date_str(datetime(2019, 1, 1, 0, 1))
        self.assertEqual(expected_date, str_date)
