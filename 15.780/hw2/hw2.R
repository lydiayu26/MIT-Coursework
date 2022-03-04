
# PROBLEM 1
ufc = read.csv('UFC_data.csv')

# 1) check collinearity
cor(ufc[, 3:ncol(ufc)-1])


#2) lin reg to predict buyrate using tweets
train = ufc[1:7, ]
test = ufc[8:nrow(ufc), ]
mod = lm(Buyrate ~ Tweets, data = train)

# a. model slope estimate, p value, and in-sample R^2
summary(mod)

# b. plot of fitted values vs residuals in training set
plot(mod$fitted.values, mod$residuals)
abline(h = 0, col = "red")


# 3) MSE, MAE, and MAPE of the model on training and test
# Helper functions:
MAE = function(actual, pred) {
  abs_errors = abs(actual - pred)
  return(mean(abs_errors))
}

MSE = function(actual, pred) {
  sq_errors = (actual - pred)^2
  return(mean(sq_errors))
}

MAPE = function(actual, pred) {
  percent_errors = abs(actual - pred) / abs(actual)
  return(mean(percent_errors))
}
# get training and test predictions:
train_pred = predict(mod, newdata = train)
test_pred = predict(mod, newdata = test)
# training errors:
MAE(train$Buyrate, train_pred)
MSE(train$Buyrate, train_pred)
MAPE(train$Buyrate, train_pred)
# test errors:
MAE(test$Buyrate, test_pred)
MSE(test$Buyrate, test_pred)
MAPE(test$Buyrate, test_pred)



library(anytime)
library(forecast)
# PROBLEM 2
sales = read.csv('MoisturizerSalesGoogleTrend.csv')
sales$Date = anytime(sales$Date)

# 1) plot sales vs time and trend vs time
plot(sales$Date, sales$MoisturizerSales, type = "l",
     xlab = "Date", ylab = "Moisturizer Sales")
plot(sales$Date, sales$GoogleTrendVolumeEczema, type = "l",
     xlab = "Date", ylab = "Eczema Trend")


# 2) lin reg to pred moisturizer sales w/ trends data
train = sales[1:177, ]
test = sales[178:nrow(sales), ]
mod = lm(MoisturizerSales ~ GoogleTrendVolumeEczema, data = train)
# slope, p-value
summary(mod)
# MAPE for train/test
train_pred = predict(mod, newdata = train)
test_pred = predict(mod, newdata = test)
MAPE(train$GoogleTrendVolumeEczema, train_pred)
MAPE(test$GoogleTrendVolumeEczema, test_pred)


# 3) plot resids
plot(train$Date, mod$residuals)
abline(h = 0, col = "red")


# 4) build time series
# convert google eczema trend to ts (weekly data => freq=52)
eczema = ts(train$GoogleTrendVolumeEczema, frequency = 52)
mod2 = auto.arima(eczema)

# a) get params p,d,q of arima model
arimaorder(mod2)

# b) training MAPE
train_pred = as.vector(mod2$fitted)
MAPE(train$MoisturizerSales, train_pred)


# 5) reg model to predict resids from eczema trend
# create resid df
resid = data.frame(train$Date, train$GoogleTrendVolumeEczema, as.vector(mod2$residuals))
colnames(resid) = c("Date", "GoogleTrendVolumeEczema", "residuals")
# build reg model
mod3 = lm(residuals ~ GoogleTrendVolumeEczema, data = resid)
summary(mod3)


# 6) add together arima and lin reg preds
# get mod3 resid predictions for the train data
mod3_train_pred = predict(mod3, newdata = resid)
# get arima predictions for the train data
arima_train_pred = predict(mod2, new_data = train)
arima_lm = mod2$fitted + mod3_train_pred
MAPE(train$MoisturizerSales, arima_lm)
