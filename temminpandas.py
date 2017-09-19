import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




# ts = pd.Series([1, 3, 5, np.nan, 6, 8])
index = pd.date_range('8/1/2017', periods=10)
ts = pd.Series(np.random.randn(10), index=index)
ts = ts.cumsum()
# plt.figure()
# ts.plot()
# plt.plot(ts)
# plt.title('C-5 flow [m3/s]')
# plt.xlabel('Time [hours]')
# plt.show()
#
df = pd.DataFrame(np.random.randn(10, 4), index=index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()

plt.figure()
# df.plot(color='green', linestyle='dashed', marker='o',
#         markerfacecolor='blue', markersize=6)
df.iloc[1].plot(kind='bar')
plt.axhline(0, color='k')
# plt.plot(df, '.-')
plt.axhline(0, color='k')
plt.title('Random flow [m3/s]')
plt.xlabel('Time')
plt.show()
