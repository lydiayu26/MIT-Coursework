#' -----------------------------------------------------------------
#' `15.774/780 Fall 2021`
#' `Recitation 3 - Regression & Time Series`
#' 
#' By the end of this recitation, you should know:
#'     - How to run linear regression in R
#'     - The intuition behind AR and MA models
#'     - How to create ARIMA models in R
#' -----------------------------------------------------------------

#' -----------------------------------------------------------------
#' REGRESSION
#' -----------------------------------------------------------------
#' Let's load the `abalone` dataset from last time and do some 
#' regression! If you haven't already, you will need to install
#' the `PivotalR` package:
#' install.packages("PivotalR")
data(abalone, package="PivotalR")

#' Our first step is always to understand our data (see last Recitation).
#' I'll just remove some unnecessary columns to make things easier...
abalone = abalone[,c("shucked","whole", "length", "height", "diameter")]

#' Next we always want to split our data into a *training* and *test*
#' set. There's many ways (and packages to do this) but let's do it
#' randomly. We use `sample()` to pick out ~70% of rows (or rather 
#' their indices) to be in the training set:
set.seed(15)
idx_train = sample(1:nrow(abalone), round(0.7 * nrow(abalone)))
train = abalone[idx_train, ]
test = abalone[-idx_train, ] # keeps all indices that are not in idx_train

#' The `cor()` function can help us figure out correlations (and examine
#' colinearity) in our training set:
cor(train$whole, train$length)

#' Or more importantly, do a pairwise correlation matrix:
cor(train)
cor(train[,-1]) #' Except for the first column (dependent variable)

#' Nearly all of our features are highly correlated, so let's build
#' just a simple model predicting `shucked` weight from `whole` weight:
#' formula: y ~ x, data to train on
#' don't need dollar signs bc pass in dataframe as an arg
mod = lm(shucked ~ whole, data = train)
mod

#' We can look at the model using `summary()`:
summary(mod) 

#' The `~` notation is known in R as a formula, and is very versatile.
#' We can build models with multiple variables:
lm(shucked ~ whole + diameter + length, data = train)

#' Or even use the shorthand `.` to use all variables:
lm(shucked ~ ., data = train)

#' We can also extract elements of the model using the *$* notation:
mod$coefficients 
mod$fitted.values #' Predicted values in the training set
mod$residuals     #' Prediction errors in the training set

#' We always want to check linearity of our model (is the relationship
#' truly linear)? We can look at the `Fitted Values vs Residuals` plot
#' (see Lecture 2) .
plot(mod$fitted.values, mod$residuals)
abline(h = 0, col = "red")

#' The `predict` function makes... drum roll... predictions on a new df:
predict(mod, newdata = train)
predict(mod, newdata = train) - mod$fitted.values # basically the same

#' More importantly we want to make predictions on the test set:
test_pred = predict(mod, newdata = test)

#' Let's calculate the MAPE for this prediction:
mean( abs(test$shucked - test_pred)  /  abs(test$shucked) )


#' -----------------------------------------------------------------
#' TIME SERIES
#' -----------------------------------------------------------------
#' Let's read in some data on Monthly Average Temperature in Alaska.
#' Source: https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data

df = read.csv("Alaska_AvgTemp.csv")
View(df)
class(df$Date)

#' Working with dates is easy in R with the `anytime` package. 
#' install.packages("anytime")
library(anytime)
df$Date = anytime(df$Date)
class(df$Date) # POSIXct is a special data type for time/dates

#' Having a specialized data type, makes plotting labels nice: 
plot(df$Date, df$AverageTemperature, 
     type = "l",  # Use lines instead of scatter plot
     xlab = "Date", ylab = "Average Temperature")

#' If you want easy date manipulation (addition, subtraction etc.)
#' then look into the `lubridate` package. 


#' Whenever we make time series models, we want to use the 
#' special time-series data type `ts`. The reason is that, 
#' beyond the values, we also tell R what seasonal  *frequency* 
#' to use, so that models know every how many periods patterns 
#' might repeat. So if we have monthly data we would specify
#' you need to tell the model how often you expect seasonal patterns to occur
#' model will not figure this out itself
#' *frequency = 12*:
temp = ts(df$AverageTemperature, frequency = 12)


#' `temp` now acts sort of like a vector, but with nicer formatting:
temp
length(temp)

#' The `decompose()` function can do a simple decomposition 
#' into trend, seasonal and residual components (see Lecture 5):
decomp = decompose(temp)
decomp$trend    #' Smoothed moving average
decomp$seasonal #' Seasonal amount below or above average
decomp$random   #' The rest

#' With nice plotting functionality:
plot(decomp)

#' Let's load the *forecast* library and run some models:
#' install.packages("forecast")
library(forecast)

#' The `arima()` function let's use fit an ARIMA model with 
#' *order = (p, d, q)*:
mod1 = arima(temp, order = c(2, 1, 1))
mod1

#' The `summary()` gives us more detailed information, including
#' a variety of training accuracy metrics:
summary(mod1)

#' You can also get this with `accuracy()`:
accuracy(mod1)

#' We can use the `forecast()` to predict the next *h* values 
#' of the time series (including confidence interval):
forecast(mod1, h = 4)

#' So if you want to do out-of-sample prediction, you can 
#' cut off the training data, forecast ahead and compute accuracy.



#' The `auto.arima()` does automatic model selection for us, and 
#' computes the "best-fit" (p, d, q)(P, D, Q)
?auto.arima
mod2 = auto.arima(temp) # This takes ~30secs

#' We can see what the best-fit parameters were:
arimaorder(mod2)

#' We can also read them (and training accuracy metrics)
#' from the `summary()`:
summary(mod2)

#' As with regression, we can extract the fitted values and 
#' residuals: 
mod2$fitted
mod2$residuals

#' Keep in mind that these are stored as `ts` objects. You can 
#' convert them back with `as.vector()`:
train_pred = as.vector(mod2$fitted)
class(train_pred)

#' And now we can calculate MAPE by ourselves:
mean(abs(train_pred - df$AverageTemperature) / abs(df$AverageTemperature))

