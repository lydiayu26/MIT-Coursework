library(ggfortify)
## Loading required package: ggplot2
library(tseries)
library(forecast)

data(AirPassengers)
AP <- AirPassengers
# Take a look at the class of the dataset AirPassengers
class(AP)


AP.SMA10 <- SMA(AP, n=10)
plot.ts(AP)
lines(AP.SMA10, col="blue")
# What if we increase N in moving average?
AP.SMA20 <- SMA(AP, n=20)
lines(AP.SMA20, col="red")
title(expression("AP Forecasts - Moving Average with N = " * phantom("10") * " and " * phantom("20") ), col.main = "black")
title(expression(phantom("AP Forecasts - Moving Average with N = ") * "10" * phantom(" and 20") ), col.main = "blue")
title(expression(phantom("AP Forecasts - Moving Average with N = 10 and ") * "20" ), col.main = "red")


# AP forecast - Exponential Smoothing
?HoltWinters	# This gets the help documentation for function HoltWinters - a general exponential smoothing function that can also accommodate trend and seasonality
AP.ES02 <- HoltWinters(AP, alpha = 0.2, beta=FALSE, gamma=FALSE)
AP.ES06 <- HoltWinters(AP, alpha = 0.6, beta=FALSE, gamma=FALSE)
AP.ES.forecast <- HoltWinters(AP, beta=FALSE, gamma=FALSE)		# without specifying the smoothing constant alpha, the function chooses the optimal one
quartz()
plot.ts(AP)
lines(AP.ES02$fitted[,1], col = "blue")
lines(AP.ES06$fitted[,1], col = "red")
lines(AP.ES.forecast$fitted[,1], col = "green")
title(expression("AP Forecasts - Exponential Smoothing with alpha = " * phantom("0.2") * ", " * phantom("0.6") * " and " * phantom("best fitted value") ), col.main = "black")
title(expression(phantom("AP Forecasts - Exponential Smoothing with alpha = ") * "0.2" * phantom(", 0.6 and best fitted value") ), col.main = "blue")
title(expression(phantom("AP Forecasts - Exponential Smoothing with alpha = 0.2, ") * "0.6" * phantom(" and best fitted value") ), col.main = "red")
title(expression(phantom("AP Forecasts - Exponential Smoothing with alpha = 0.2, 0.6 and ") * "best fitted value" ), col.main = "green")


components.ts= decompose(AP) 
plot(components.ts)
dtrended.AP=AP-components.ts$trend # removing the trend
plot(dtrended.AP) # 

random.part<-components.ts$random
random.part <- na.omit(random.part)
autoplot(acf(random.part,plot=FALSE), )+ labs(title="ACF of Random Part") %acf of the random part 

arimaAP <- auto.arima(random.part)
arimaAP
ggtsdiag(arimaAP)

forecast.random<-forecast(arimaAP, level = c(95), h = 36)
autoplot(forecast.random)
