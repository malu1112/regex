from re import match
from datetime import datetime

patterns = {
    '%Y/%m/%d': r'^\s*\d{4}\/\d{2}\/\d{2}\s*$',
    '%d/%m/%Y': r'^\s*\d{2}\/\d{2}\/\d{4}\s*$',
    '%Y-%m-%d': r'^\s*\d{4}-\d{2}-\d{2}\s*$',
    '%d-%m-%Y': r'^\s*\d{2}-\d{2}-\d{4}\s*$',
}


def date_matcher(input_date):
    try:
        for expected_format, pattern in patterns.items():
            if match(pattern, input_date):
                return 'CONVERTED', datetime.strptime(input_date, expected_format)
    except Exception as e:
        return 'EXCEPTION', datetime.now()


if __name__ == '__main__':
    sample_date = ['2020/11/19', '10/02/2020', '2020-12-01', '01-01-2020']
    for date in sample_date:
        status, date_obj = date_matcher(date)
        print(f'Input Date: [{date}] [{status}] to [{date_obj}]')
# -------- Sample Output ----------------->
# Input Date: [2020/11/19] [CONVERTED] to [2020-11-19 00:00:00]
# Input Date: [10/02/2020] [CONVERTED] to [2020-02-10 00:00:00]
# Input Date: [2020-12-01] [CONVERTED] to [2020-12-01 00:00:00]
# Input Date: [01-01-2020] [CONVERTED] to [2020-01-01 00:00:00]
