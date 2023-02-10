# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import numpy as np

fig = plt.figure()

#linear_data = np.array([1, 20, 40, 60, 80, 100])
# x = np.array([11, 22, 12, 9, 10.5, 9.75, 44, 11, 341234])
# y = x
# colors = ['pink'] * (len(x) - 1)
# colors.append('purple')
# plt.scatter(x, y, c = colors)
# #plt.plot(linear_data, '-x')
# # plt.bar([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
# fig.savefig('scatter.png')
                 # ---------------
# languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']

# pos = np.arange(len(languages))
# popularity = [56, 39, 34, 34, 29]
# plt.bar(pos, popularity, align = 'center')
# plt.xticks(pos.languages)
# plt.ylabel('%popularity')
# plt.title('Top 5 programming languages')
# fig.savefig('lang.png')



#                ----------------------


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
import datetime as DT

df=pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')


now  = pd.Timestamp(DT.datetime.now())
df['dob'] = pd.to_datetime(df['dob'])
df['dob'] = df['dob'].where(df['dob'] < now, df['dob'] - np.timedelta64(100,"Y"))