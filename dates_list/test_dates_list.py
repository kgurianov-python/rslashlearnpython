import unittest

from dates_list.impl_dates_list import get_first_days, get_last_days


class MyTestCase(unittest.TestCase):
    def test_first_days_end_to_end(self):
        start_date = '2022-06-01'
        end_date = '2023-05-31'
        expected = ['2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01',
                    '2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01']
        self.assertEqual(expected, get_first_days(start_date, end_date))  # add assertion here

    def test_last_days_end_to_end(self):
        start_date = '2022-06-01'
        end_date = '2023-05-31'
        expected = ['2022-06-30', '2022-07-31', '2022-08-31', '2022-09-30', '2022-10-31', '2022-11-30', '2022-12-31',
                    '2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30', '2023-05-31']
        self.assertEqual(expected, get_last_days(start_date, end_date))  # add assertion here

    def test_first_days_miss_first(self):
        start_date = '2022-06-02'
        end_date = '2023-05-30'
        expected = ['2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01',
                    '2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01']
        self.assertEqual(expected, get_first_days(start_date, end_date))  # add assertion here

    def test_last_days_miss_last(self):
        start_date = '2022-06-02'
        end_date = '2023-05-30'
        expected = ['2022-06-30', '2022-07-31', '2022-08-31', '2022-09-30', '2022-10-31', '2022-11-30', '2022-12-31',
                    '2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30']
        self.assertEqual(expected, get_last_days(start_date, end_date))  # add assertion here


if __name__ == '__main__':
    unittest.main()
