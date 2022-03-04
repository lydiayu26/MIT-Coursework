library(mlbench)
library(Hmisc)
library(DMwR)
library(editrules)
library(mice)


# PROBLEM 1: MISSING VALUES
data(Glass , package = "mlbench")
# keep a copy of the original data
original = Glass

# 1) introduce 30 missing values each in the Si and K variables
set.seed(80)
Glass$Si[sample(1:nrow(Glass), 30)] = NA
Glass$K[sample(1:nrow(Glass), 30)] = NA
md.pattern(Glass)

# 2) impute the variable Si with its mean value
impute(Glass$Si, mean)

# 3) Impute the variable Si with median 
#    report the MAE, MSE and MAPE values to evaluate the accuracy of this imputation
imp = impute(Glass$Si, median)
org = original$Si
# find the cells where we introduced NAs
miss  = is.na(Glass$Si)
MAE(org[miss], imp[miss])
MSE(org[miss], imp[miss])
MAPE(org[miss], imp[miss]) 

# Helper functions:
MAE = function(actual, imputed) {
  abs_errors = abs(actual - imputed)
  return(mean(abs_errors))
}

MSE = function(actual, imputed) {
  sq_errors = (actual - imputed)^2
  return(mean(sq_errors))
}

MAPE = function(actual, imputed) {
  percent_errors = abs(actual - imputed) / abs(actual)
  return(mean(percent_errors))
}

# 4) Impute the variable Si using KNN using the 5 nearest neighbours
#    report the MAE, MSE and MAPE values to evaluate the accuracy of this imputation.
org = original$Si
knnOut = knnImputation(Glass, k = 5)
imp = knnOut$Si
miss  = is.na(Glass$Si)

MAE(org[miss], imp[miss])
MSE(org[miss], imp[miss])
MAPE(org[miss], imp[miss]) 


# PROBLEM 2: Inconsistencies

# 1) Load iris.csv, use the str() function to get a first look at the data
#    check if any columns need to be coerced into a different data type
iris = read.csv('iris.csv')
str(iris)

# 2) Make a histogram for each numeric column
hist(iris$Sepal.Length, breaks=30, xlab = "Sepal Length")           
hist(iris$Sepal.Width, breaks=30, xlab = "Sepal Width") 
hist(iris$Petal.Length, breaks=30, xlab = "Petal Length")
hist(iris$Petal.Width, breaks=30, xlab = "Petal Width") 

# 3) create a simple ruleset that contains the rules that the columns of the dataframe should obey
# Sepal.width should not have values over 10, Petal.Length cannot be negative:
# editset tells which rows follow the rules defined
E = editset(c("Sepal.Width < 10", "Petal.Length > 0"))
# violatededits gives which rows violated the rules (True if violated)
V = violatedEdits(E, iris)

# 4) number of observations that violate each of the rules
# V[, 'num1'] gives which rows violated Sepal.Width < 10
sum(V[,"num1"])
#  V[, 'num2'] gives which rows violated Petal.Length > 0
sum(V[, 'num2'])

# 5) Filter iris to contain only observations that do not violate any of the rules
iris_filtered = na.omit(subset(iris, !V[, 'num1'] & !V[,'num2']))
dim(iris_filtered)





