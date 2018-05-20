""" 
Simple Poloniex API request for a chart, returned as a DataFrame.

Usage:

import poloniex as plnx
import pandas as pd 
from datetime import datetime, timedelta
pair = 'USDT_BTC'
timeframe = 15 * 60
end = datetime.utcnow()
start = end - timedelta(days=7)
verbose_logging = True
chart = plnx.get_chart(pair, timeframe, start, end, verbose_logging)
chart
"""

import calendar
import requests
import pandas as pd 
from datetime import datetime, timedelta

def unix_epoch_to_timestamp(epoch):
    return datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')

def timestamp_to_unix_epoch(ts):
    return calendar.timegm(ts.timetuple())

def get_chart(pair, timeframe, start, end, verbose = False):
    start = timestamp_to_unix_epoch(start)
    end = timestamp_to_unix_epoch(end)
    url = 'https://poloniex.com/public?command=returnChartData&currencyPair={}&start={}&end={}&period={}'.format(pair, start, end, timeframe) 
    if verbose: print(url)
    json = requests.get(url)
    data = json.json()
    date, o, h, l, c = zip(*[(unix_epoch_to_timestamp(x['date']), x['open'], x['high'], x['low'], x['close']) for x in data])
    d = {'date': date, 'open': o, 'high': h, 'low': l, 'close': c}
    if verbose: print('Retrieved {} records.'.format(len(data)))
    return pd.DataFrame(data=d)

