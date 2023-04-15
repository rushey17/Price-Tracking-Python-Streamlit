import pandas as pd


def get_ahead_date(date, days=1):
   timestamp_date_obj = pd.Timestamp(date)
   ahead_date_obj = timestamp_date_obj + pd.Timedelta(days=days)
   return str(ahead_date_obj).split(' ')[0]