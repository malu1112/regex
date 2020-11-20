from re import match
from datetime import datetime

sample_date = ['2020/11/19', '10/2/2020', '2020-12-01', '1-01-2020']
# regex patterns to identify the type of date format.
patterns = {
    '%Y/%m/%d': r'^\s*\d{4}\/\d{1,2}\/\d{1,2}\s*$',
    '%d/%m/%Y': r'^\s*\d{1,2}\/\d{1,2}\/\d{4}\s*$',
    '%Y-%m-%d': r'^\s*\d{4}-\d{1,2}-\d{1,2}\s*$',
    '%d-%m-%Y': r'^\s*\d{1,2}-\d{1,2}-\d{4}\s*$',
}


def date_matcher(input_date):
    """
    Identify the format of input date and convert to datetime.
    Along with that track the status of conversion
    """
    try:
        for expected_format, pattern in patterns.items():
            if match(pattern, input_date):
                return 'CONVERTED', datetime.strptime(input_date, expected_format)
    except Exception as e:
        return 'EXCEPTION', datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)
    return 'NOT CONVERTED', datetime.now().replace(microsecond=0, second=0, minute=0, hour=0)


if __name__ == '__main__':
    for date in sample_date:
        status, date_obj = date_matcher(date)
        print(f'Input Date: [{date}] [{status}] to [{date_obj}]')

# -------- Sample Output ----------------->
# Input Date: [2020/11/19] [CONVERTED] to [2020-11-19 00:00:00]
# Input Date: [10/02/2020] [CONVERTED] to [2020-02-10 00:00:00]
# Input Date: [2020-12-01] [CONVERTED] to [2020-12-01 00:00:00]
# Input Date: [01-01-2020] [CONVERTED] to [2020-01-01 00:00:00]
