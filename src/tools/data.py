import pandas as pd
import numpy as np
import datetime
import math

# 文本形式的日期转成时间戳
# input: 'Apr-16-2017 21:01:36', output: 1492347696
def BeijingObject2timestamp(timestampStr):
  return math.floor(int(datetime.datetime.strptime(timestampStr, '%Y-%m-%d %H:%M:%S').timestamp()) / 3600)


def readBeijingAq(filename):
  df = pd.read_csv(filename)
  past_aq_pick_num = 4
  # get numpy array
  values = df.values
  total = len(values)

  # fill na
  max_gap = 3
  for j in range(6):
    begin = -1
    for index in range(total):
      if not np.isnan(values[index][j + 2]):
        begin = index
        break
    if begin == -1:
      continue
    while begin < total:
      end = begin + 1
      while end < total and np.isnan(values[end][j + 2]):
        end += 1
      if end - begin <= max_gap + 1 and end < total:
        for index in range(begin + 1, end):
          values[index][j + 2] = (values[end][j + 2] - values[begin][j + 2]) * (index - begin) / (end - begin) + values[begin][j + 2]
      begin = end

  # filter empty data
  proper_data = {}
  for i in range(total):
    proper = True
    for j in range(6):
      if np.isnan(values[i][j + 2]):
        proper = False
        break
    if proper:
      if not values[i][0] in proper_data:
        proper_data[values[i][0]] = []
      proper_data[values[i][0]].append((BeijingObject2timestamp(values[i][1]), values[i][2:]))
  
  dataset = {}
  for station in proper_data:
    aq_data = proper_data[station]
    dataset[station] = [[], []]
    begin_index = 0
    end_index = -1
    while begin_index < len(aq_data):
      end_index = begin_index + 1
      while end_index < len(aq_data) and (aq_data[end_index][0] - aq_data[end_index - 1][0] == 1):
        end_index += 1
      for begin in range(begin_index, end_index - past_aq_pick_num - 1):
        data = []
        for index in range(begin, begin + past_aq_pick_num):
          data += list(aq_data[index][1])
        dataset[station][0].append(data)
        dataset[station][1].append(aq_data[begin + past_aq_pick_num][1])
      begin_index = end_index
  return dataset

def LondonObject2timestamp(timestampStr):
  return math.floor(int(datetime.datetime.strptime(timestampStr, '%Y/%m/%d %H:%M').timestamp()) / 3600)

def readLondonAq(filename):
  df = pd.read_csv(filename)
  past_aq_pick_num = 4
  # get numpy array
  values = df.values
  total = len(values)

  # fill na
  max_gap = 3
  for j in range(3):
    begin = -1
    for index in range(total):
      if not np.isnan(values[index][j + 3]):
        begin = index
        break
    if begin == -1:
      continue
    while begin < total:
      end = begin + 1
      while end < total and np.isnan(values[end][j + 3]):
        end += 1
      if end - begin <= max_gap + 1 and end < total:
        for index in range(begin + 1, end):
          values[index][j + 3] = (values[end][j + 3] - values[begin][j + 3]) * (index - begin) / (end - begin) + values[begin][j + 3]
      begin = end

  # filter empty data
  proper_data = {}
  for i in range(total):
    proper = True
    for j in range(3):
      if np.isnan(values[i][j + 3]):
        proper = False
        break
    if proper:
      if not values[i][2] in proper_data:
        proper_data[values[i][2]] = []
      proper_data[values[i][2]].append((LondonObject2timestamp(values[i][1]), values[i][3:]))

  dataset = {}
  for station in proper_data:
    aq_data = proper_data[station]
    dataset[station] = [[], []]
    begin_index = 0
    end_index = -1
    while begin_index < len(aq_data):
      end_index = begin_index + 1
      while end_index < len(aq_data) and (aq_data[end_index][0] - aq_data[end_index - 1][0] == 1):
        end_index += 1
      for begin in range(begin_index, end_index - past_aq_pick_num - 1):
        data = []
        for index in range(begin, begin + past_aq_pick_num):
          data += list(aq_data[index][1])
        dataset[station][0].append(data)
        dataset[station][1].append(aq_data[begin + past_aq_pick_num][1])
      begin_index = end_index
  return dataset