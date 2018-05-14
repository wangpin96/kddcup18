import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd

def plot(x, y):
  x = list(map(lambda stamp: datetime.datetime.fromtimestamp(int(stamp)), x))
  plt.plot(x, y)
  plt.show()

def processNa(df):
  df = df.fillna(method='ffill')
  df = df.fillna(method='bfill')
  return df

def plotCSV(filename):
  df = pd.read_csv(filename)
  plot(list(df['timestamp'].values), list(df['value']))
