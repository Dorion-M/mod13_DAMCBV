import unittest
import datetime

def validate_input(symbol, chart_type, time_series, start_date, end_date):
    # Validate symbol
    if not (symbol.isalpha() and symbol.isupper() and len(symbol) <= 7):
        return False
    
    # Validate chart_type
    if chart_type not in ['1', '2']:
        return False
    
    # Validate time_series
    if time_series not in ['1', '2', '3', '4']:
        return False
    
    # Validate start_date and end_date format (YYYY-MM-DD)
    date_format = '%Y-%m-%d'
    try:
        start_date_obj = datetime.datetime.strptime(start_date, date_format)
        end_date_obj = datetime.datetime.strptime(end_date, date_format)
    except ValueError:
        return False
    
    # Validate end_date is after start_date
    if end_date_obj < start_date_obj:
        return False
    
    return True


class TestProject3Inputs(unittest.TestCase):

    def test_valid_input(self):
        # Simulate valid form input
        symbol = 'AAPL'
        chart_type = '1'
        time_series = '2'
        start_date = '2024-01-01'
        end_date = '2024-04-01'
        self.assertTrue(validate_input(symbol, chart_type, time_series, start_date, end_date))

    def test_invalid_symbol(self):
        # Simulate invalid symbol (not capitalized)
        symbol = 'msft'
        chart_type = '1'
        time_series = '2'
        start_date = '2024-01-01'
        end_date = '2024-04-01'
        self.assertFalse(validate_input(symbol, chart_type, time_series, start_date, end_date))

    def test_invalid_chart_type(self):
        # Simulate invalid chart type
        symbol = 'AAPL'
        chart_type = '3'
        time_series = '2'
        start_date = '2024-01-01'
        end_date = '2024-04-01'
        self.assertFalse(validate_input(symbol, chart_type, time_series, start_date, end_date))

    def test_invalid_time_series(self):
        # Simulate invalid time series
        symbol = 'AAPL'
        chart_type = '1'
        time_series = '5'
        start_date = '2024-01-01'
        end_date = '2024-04-01'
        self.assertFalse(validate_input(symbol, chart_type, time_series, start_date, end_date))

    def test_invalid_date_range(self):
        # Simulate invalid date range (end_date before start_date)
        symbol = 'AAPL'
        chart_type = '1'
        time_series = '1'
        start_date = '2024-04-01'
        end_date = '2024-01-01'
        self.assertFalse(validate_input(symbol, chart_type, time_series, start_date, end_date))

if __name__ == '__main__':
    unittest.main()
