import pandas as pd
import numpy as np
import datetime
import math

# 文本形式的日期转成时间戳
# input: 'Apr-16-2017 21:01:36', output: 1492347696
def object2timestamp(timestampStr):
  return math.floor(int(datetime.datetime.strptime(timestampStr, '%Y-%m-%d %H:%M:%S').timestamp()) / 3600)


def readBeijingAq(filename):
  df = pd.read_csv(filename)
  future_num = 4
  # get numpy array
  values = df.values
  total = len(values)
  proper_data = {}
  for i in range(1, total):
    proper = True
    for j in range(6):
      if np.isnan(values[i][j + 2]):
        proper = False
        break
    if proper:
      if not values[i][0] in proper_data:
        proper_data[values[i][0]] = []
      proper_data[values[i][0]].append((object2timestamp(values[i][1]), values[i][2:]))
  dataset = {}
  for station in proper_data.keys():
    aq_data = proper_data[station]
    dataset[station] = [[], []]
    begin_index = 0
    end_index = -1
    while begin_index < len(aq_data):
      end_index = begin_index + 1
      while end_index < len(aq_data) and (aq_data[end_index][0] - aq_data[end_index - 1][0] == 1):
        end_index += 1
      for begin in range(begin_index, end_index - future_num - 1):
        data = []
        for index in range(begin, begin + future_num):
          data += list(aq_data[index][1])
        dataset[station][0].append(data)
        dataset[station][1].append(aq_data[begin + future_num][1])
      begin_index = end_index
  return dataset

if __name__ == '__main__':
  dataset = readBeijingAq('../../data/beijing_17_18_aq.csv')

