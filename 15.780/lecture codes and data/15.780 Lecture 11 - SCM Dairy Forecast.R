cat("\014")
rm(list = ls(all.names = TRUE))
data = read.csv("dairy_demand_data.csv") 
head(data)

#Create column for average for each month
data$average = (data$Year.1 + data$Year.2 + data$Year.3) / 3

#Divide each monthly average by the average of all monthly averages to get the seasonality index
data$season.index = data$average/mean(data$average)
head(data)

#Deseasonalize the data for each year
Year.1.deseason = data$Year.1/data$season.index
Year.2.deseason = data$Year.2/data$season.index
Year.3.deseason = data$Year.3/data$season.index
#Combine the deasonalized data into its own dataframe
deseason.data = data.frame(data$Month, Year.1.deseason, Year.2.deseason, Year.3.deseason)
head(deseason.data)

#Create a single vector (36x1) of the deasonalized data from April 2008 through March 2011
deseason.data.vector = as.vector(c(Year.1.deseason, Year.2.deseason, Year.3.deseason))
deseason.data.vector
#Create a sequence for the month number (also 36x1)
month.number <- seq(1,36,1)
month.number

#Regress the demand data on the month number
model <- lm(deseason.data.vector~month.number)
model$coefficients
summary(model)

#Use this model to predict the deasonalized demand from April 2011 through March 2012 (the next 12 months)
deseason.Year.4.estimate <- rep(0,12)
for (i in (1:12))
  deseason.Year.4.estimate[i] <- 7216159.37 + 69804.38*(i+36)
deseason.Year.4.estimate

#Reseasonalize the data
Year.4.estimate <- deseason.Year.4.estimate * data$season.index
Year.4.estimate
#Total demand from April through Septebmer 2011
sum(Year.4.estimate[1:6])




#Extra...
image <- data.frame(data$Month, deseason.Year.4.estimate, data$season.index, Year.4.estimate)
myts <- ts(deseason.data.vector, start=c(2008, 4), end=c(2011, 3), frequency=12) 
plot.ts(myts)

