from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from collections import Counter

# print(plt.style.available)
plt.style.use('ggplot')


data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
print(languages)
print(popularity)


# with open('data.csv') as csv_files:
#     csv_reader = csv.DictReader(csv_files)

#     language_counter = Counter()

#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))

# languages = []
# popularity = []

# for item in language_counter.most_common(15):
#     languages.append(item[0])
#     popularity.append(item[1])
#     # row = next(csv_reader)
#     # print(row['LanguagesWorkedWith'].split(';'))
# languages.reverse()
# popularity.reverse()

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity,color='r')

plt.title('Most Popular Languages')
# plt.ylabel('Programming Languages')
plt.xlabel('Number Of People Who Use')

plt.legend()
plt.tight_layout()
plt.show()













# ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# x_indexs = np.arange(len(ages_x))
# width = 0.25

# dev_y = [38496, 42000, 46752, 49320, 53200,
#          56000, 62316, 64928, 67317, 68748, 73752]

# plt.bar(x_indexs - width,dev_y,width=width,color='b',label='Other Developer')

# py_dev_y = [45372, 48876, 53850, 57287, 63016,
#             65998, 70003, 70000, 71496, 75370, 83640]

# plt.bar(x_indexs,py_dev_y,width=width,color='g',label='Python Developer')

# js_dev_y = [37810, 43515, 46823, 49293, 53437,
#             56373, 62375, 66674, 68745, 68746, 74583]

# plt.bar(x_indexs + width,js_dev_y,width=width,color='y',label='Javascript Developer')

# plt.legend()

# plt.xticks(ticks=x_indexs,labels=ages_x)

# plt.xlabel('Ages')
# plt.ylabel('Median Salary By (USD)')
# plt.title('Median Salary By (USD) ages')

# plt.tight_layout()
# plt.show()






