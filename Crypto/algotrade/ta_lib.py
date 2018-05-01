import pandas as pd 
import numpy as np
from scipy.ndimage.interpolation import shift
from pandas import Series

def daily_returns(df, source_column = 'close', target_column = 'daily_return'): 
    df[target_column] = df[source_column] - df[source_column].shift(1)

def sma(df, periods = 7, source_column = 'close', target_column = 'sma'):
    df['{}{}'.format(target_column, periods)] = df[source_column].rolling(window=periods).mean()

def triangular(n): return n * (n + 1) / 2
def wma(df, periods = 7, source_column = 'close', target_column = 'wma'):
    x = np.linspace(1, periods, periods)
    weights = (periods-x+1) / triangular(periods)
    wma = np.convolve(weights, df[source_column], 'valid')
    wma.resize(len(wma)+periods-1)
    wma = Series(wma)
    wma = wma.shift(periods-1)
    df['{}{}'.format(target_column, periods)] = wma  

def ema(df, periods = 7, source_column = 'close', target_column = 'ema'):
    weights = np.exp(1-np.linspace(-1, 1, periods))
    weights /= weights.sum()
    ema = np.convolve(weights, df[source_column], 'valid')
    ema.resize(len(ema)+periods-1)
    ema = Series(ema)
    ema = ema.shift(periods-1)
    df['{}{}'.format(target_column, periods)] = ema  

def std(df, periods = 20, source_column = 'close', target_column = 'std'):
    df['{}{}'.format(target_column, periods)] = df[source_column].rolling(window=periods).std()

def bbands(df, periods = 20, source_column = 'close', target_column = 'bb'):
    temp_df = pd.DataFrame(df[source_column])
    std(temp_df, periods)
    ema(temp_df, periods)
    df['{}_mid'.format(target_column)] = temp_df['ema{}'.format(periods)]
    df['{}_upper'.format(target_column)] = temp_df['ema{}'.format(periods)] + 2*temp_df['std{}'.format(periods)]
    df['{}_lower'.format(target_column)] = temp_df['ema{}'.format(periods)] - 2*temp_df['std{}'.format(periods)]

def rsi(df, periods = 14, source_column='daily_return', target_column='rsi'):
    temp_df = pd.DataFrame(df[source_column])
    temp_df['closing_gains'] = temp_df[source_column].apply(lambda x: max(x, 0))
    temp_df['closing_losses'] = temp_df[source_column].apply(lambda x: abs(min(x, 0)))
    ema(temp_df, periods, 'closing_gains', 'closing_gains_ema')
    ema(temp_df, periods, 'closing_losses', 'closing_losses_ema')
    temp_df['rs'] = temp_df['closing_gains_ema{}'.format(periods)] / temp_df['closing_losses_ema{}'.format(periods)]
    df[target_column] = 100 - 100 / (1 + temp_df['rs'])