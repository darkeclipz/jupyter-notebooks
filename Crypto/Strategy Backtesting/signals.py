import numpy as np

def init(df):
    df['open_long'] = df['close_long'] = df['open_short'] = df['close_short'] = 0

def moving_average_crossover(df, ma_low, ma_high):
    for i in range(1, len(df)):
        previous = df.iloc[i-1]
        current = df.iloc[i]
        
        if np.isnan(previous[ma_low]) or np.isnan(previous[ma_high]) \
            or np.isnan(current[ma_low]) or np.isnan(current[ma_high]): continue
        
        ma_prev = previous[ma_low] - previous[ma_high]
        ma_current = current[ma_low] - current[ma_high]
        
        if ma_prev > 0 and ma_current < 0: df.loc[i, 'open_short'] = 1
        if ma_prev < 0 and ma_current > 0: df.loc[i, 'open_long'] = 1

