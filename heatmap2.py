import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# just following your previous post to simulate your data
np.random.seed(0)
dates = np.random.choice(pd.date_range('2015-01-01 00:00:00', '2015-06-30 00:00:00', freq='1h'), 10000)
company = np.random.choice(['company' + x for x in '1 2 3 4 5'.split()], 10000)
df = pd.DataFrame(dict(recvd_dttm=dates, CompanyName=company)).set_index('recvd_dttm').sort_index()
df['C'] = 1
df.columns = ['CompanyName', '']
result = df.groupby([lambda idx: idx.month, 'CompanyName']).agg({df.columns[1]: sum}).reset_index()
result.columns = ['Month', 'CompanyName', 'counts']
pivot_table = result.pivot(index='CompanyName', columns='Month', values='counts')


x_labels = ['Month'+str(x) for x in pivot_table.columns.values]
y_labels = pivot_table.index.values

fig, ax = plt.subplots()
x = ax.imshow(pivot_table, cmap=plt.cm.winter)
plt.colorbar(mappable=x, ax=ax)
ax.set_xticks(np.arange(len(x_labels)))
ax.set_yticks(np.arange(len(y_labels)))
ax.set_xticklabels(x_labels)
ax.set_yticklabels(y_labels)
ax.set_xlabel('Month')
ax.set_ylabel('Company')
ax.set_title('Customer Calls This Year')
