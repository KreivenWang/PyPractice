import os

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

s = Series([1, 2, 3.0, 'abc'])
print(s)
print(s.name)
print(s.index.name)

# s = Series(data=[1, 3, 5, 7], index=['a', 'b', 'x', 'y'])
# print(s)
# print(s.name)
# print(s.index.name)
# print(s.values)

data = {'state': ['Ohino', 'Ohino', 'Ohino', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# df = DataFrame(data)
# print(df)
#
df = DataFrame(data, index=['i1', 'i2', 'i3', 'i4', 'i5'],
               columns=['year', 'state', 'pop', 'dept'])

# df.reindex(index=['a', 'b', 'c', 'd', 'e', 'f'], columns=['ca', 'cb', 'cc'], method='ffill')
# print(df)

dates = pd.date_range('20170831', periods=6)
print(dates)
df = DataFrame(np.random.randn(6, 2), index=dates, columns=list('ab'))
print(df.iloc[1:3, [1, 2]])

print(df.describe())


