import numpy as np
from sklearn import linear_model
import math
import data

def smape(actual, predicted):
    a = np.abs(np.array(actual) - np.array(predicted))
    b = np.array(actual) + np.array(predicted)
    return 2 * np.mean(np.divide(a, b, out=np.zeros_like(a), where=b!=0, casting='unsafe'))
      
def train_interface(dataset, method):
  print('train with model ' + method)
  data = process_dataset(dataset)
  print('datasize: ' + str(len(data[0])))
  train_num = math.floor(len(data[0]) * 0.8)
  train_features = data[0][:train_num]
  train_tags = data[1][:train_num]
  test_features = data[0][train_num:]
  test_tags = data[1][train_num:]
  model = None
  if method == 'linear regression':
    model = linear_model.LinearRegression()
  if not model:
    print("incorrect model")
    return
  model.fit(train_features, train_tags)
  predicted = model.predict(test_features)
  for i in range(len(predicted)):
    for j in range(len(predicted[i])):
      predicted[i][j] = max(predicted[i][j], 0.0)
  score = smape(test_tags, predicted)
  print('test score: ', score)

def process_dataset(dataset):
  ret = [[], []]
  for key in dataset:
    ret[0] += dataset[key][0]
    ret[1] += dataset[key][1]
  return ret

if __name__ == '__main__':
  dataset = data.readBeijingAq('../../data/beijing_17_18_aq.csv')
  train_interface(dataset, 'linear regression')
