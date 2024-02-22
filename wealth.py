import pandas as pd

weight = pd.read_csv(
    '~/Documents/wealth/data/WeightWatcher.csv',
    header=None,
    names=['Date', 'Before', 'After', 'took_med'],
    index_col=0,
    parse_dates=True,
    na_values='?')

print(weight.head())
