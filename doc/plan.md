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

#### methods
* linear regression
* logistic regression
* RNN / LSTM
* 时序方法