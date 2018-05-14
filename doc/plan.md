## KDDCup 2018

#### goal
* 预测北京和伦敦共48个站点未来48小时的空气质量

#### data
* 17/1/30 - 18/1/31 北京各站点的天气情况
  * station_id,longitude,latitude,utc_time,temperature,pressure,humidity,wind_direction,wind_speed,weather
* 17/1/1 - 18/2/28 北京各站点的空气质量
  * stationId,utc_time,PM2.5,PM10,NO2,CO,O3,SO2
* 17/1/1 - 18/3/27 北京网格数据
  * stationName,longitude,latitude,utc_time,temperature,pressure,humidity,wind_direction,wind_speed/kph
* 17/1/1 - 18/3/31 伦敦各站点空气质量
  * ,MeasurementDateGMT,station_id,PM2.5 (ug/m3),PM10 (ug/m3),NO2 (ug/m3)
* 17/3/31 -  北京 伦敦各站点空气质量、天气情况

#### 数据处理
* 基本空气污染物数据
  * 整理好每个站点的数据
    * 如何处理缺失数据
      * 平滑方法，前后正常数据线性插值
      * 或者直接使用pandas的向前向后填充
      * 某一段数据缺失太多则丢弃
    * 数据异常如何处理
      * 设置每个字段最大最小值，超出按最值处理
    * 各个站点各自预测，还是一起预测
      * 一起预测效果可能会好，但是速度会慢很多
  * 数据整理后的格式
    * 每个站点一个数据集
    * 没个数据集包括两个维度，第一个维度为时间，第二个维度为污染物
    * 根据数据集划分训练集、测试集
      * 每组数据的输入维度为 forward_hours * aq_num, 表示前forword_hours小时，每小时的污染情况
      * 输出为下一个小时污染物的情况，维度为 aq_num
#### methods
* linear regression
  * 利用前 n个小时的六种污染物的值作为自变量，预测下一小时的六种污染物的值，循环48次，预测未来48小时污染物的值
* 全联接层(MLP)
  * 输入输出和 线性回归一样
* logistic regression
  * 输入输出和线性回归一样
* RNN / LSTM
* 时序方法
* 集成学习方法
  * xgboost

#### progress
* todos
  * 数据预处理得到训练集、测试集
  * 利用线性回归完成基本baseline
  * 跑通提交的过程
* doing

* done
