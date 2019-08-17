from datetime import datetime


def convert_str_date(str_date:str):
    return datetime.strptime(str_date, '%Y-%m-%d')


def convert_date_str(date: datetime):
    return date.strftime('%Y-%m-%d')

