#' ----------------------------------------------------------------------

#' `15.774/780 Fall 2021`
#' `Recitation 4 - Choice modeling & Assortment Optimization`
#' 
#' By the end of this recitation, you should know:
#'     - How to run MNL models in R
#'     - Know how to use the model in different scenarios (wide vs long)
#'     - Predict market shares of products given an assortment!
#' ----------------------------------------------------------------------

#' ----------------------------------------------------------------------

#' Multinomial Logit Model: TravelMode 'long' format example
#' ----------------------------------------------------------------------

#' installing the packages we are going to use: mlogit and AER
#' install.packages("mlogit") 
#' install.packages("AER")

#' Let's load them
library("mlogit")
library("AER")

data("TravelMode", package = "AER")
help("TravelMode") #' always a good habit to study our data before we work on it

#' how many total 'products' do we have here? 
#' 840 because each observation has different features

travel = TravelMode

#' *mlogit.data* function: https://www.rdocumentation.org/packages/mlogit/versions/0.1-0/topics/mlogit.data
#' `wide format` - e.g. price of choice A and choice B shown in one row, like in lecture
#' `long format` - see choice attributes across 4 rows (e.g. options A,B,C,D -> 4 rows in long format)
# alt.levels are the names of the different options
tm = mlogit.data(travel, choice = "choice", shape = "long", alt.levels = c("air", "train", "bus", "car"))
head(tm)

#' use the MNL model to estimate our parameters, if you want to know how this is being done
#' check out maximum likelihood estimator
#' -1: no intercept
#' right side of | any user features
#' left side of | features of the alternatives
model = mlogit(choice ~ wait + vcost + travel + gcost | -1 , data = tm)
help("mlogit")
summary(model)

#' PREDICTION & SENSITIVITY ANALYSIS

#' let's predict market share! 
#' Suppose we offer four transportation options with the following attributes:

air.wait = 69    
air.vcost = 59   
air.travel = 100    
air.gcost = 70    

train.wait = 44    
train.vcost = 31    
train.travel = 354    
train.gcost = 84 

bus.wait = 35  
bus.vcost = 25  
bus.travel = 417   
bus.gcost =  70   

car.wait = 0    
car.vcost = 10    
car.travel = 180   
car.gcost = 30

#' What would the predicted market share of each ticket?
# numberators of each equation, eg the weights
VT1 = exp(coef(model)[1]*air.wait + coef(model)[2]*air.vcost + coef(model)[3]*air.travel + 
            coef(model)[4]*air.gcost) #' air
VT2 = exp(coef(model)[1]*train.wait + coef(model)[2]*train.vcost + 
            coef(model)[3]*train.travel+ coef(model)[4]*train.gcost) #' train
VT3 = exp(coef(model)[1]*bus.wait + coef(model)[2]*bus.vcost + 
            coef(model)[3]*bus.travel + coef(model)[4]*bus.gcost) #' bus
VT4 = exp(coef(model)[1]*car.wait + coef(model)[2]*car.vcost + 
            coef(model)[3]*car.travel + coef(model)[4]*car.gcost) #' car

#' shares, according to the MNL formula P(i|S) from the slides
ShareAir = VT1 / (VT1 + VT2 + VT3 + VT4)
as.numeric(ShareAir)
ShareTrain= VT2 / (VT1 + VT2 + VT3 + VT4)
as.numeric(ShareTrain)
ShareBus = VT3 / (VT1 + VT2 + VT3 + VT4)
as.numeric(ShareBus)
ShareCar = VT4 / (VT1 + VT2 + VT3 + VT4)
as.numeric(ShareCar)

#' what would the sum of shares be?
sum(ShareAir + ShareTrain + ShareBus + ShareCar)


#' `Intercept & user features`: extensions to this model

#' what if all options have same attributes? (e.g. cost, wait), intuitively, which one would you pick?
#' | -1 = discard the external 1 in the utility function - every user will choose something

model = mlogit(choice ~ wait + vcost + travel + gcost, data = tm)
summary(model)

#' why shouldn't we incorporate user features as well? which choice would a really rich person pick here?
#' how does my income affect how likely i am to choose train/bus/car relative to air?
model = mlogit(choice ~ wait + vcost + travel + gcost | income -1 , data = tm)
summary(model)


#' Multinomial Logit Model: Train 'wide' format example
#' ----------------------------------------------------------------------

rm(list=ls()) #' clear global environment

#' load 'Train' data from 'mlogit' package
data("Train", package = "mlogit")
help("Train")
train = Train

#' again, how many 'products' do we have here?

#' massage the data to MNL-ready format
#' note that in the "wide" format, column names should match per option
#' i.e. if we look at price for ticket A and ticket B, the appropriate column 
#' names should be price_A and price_B, or price.A and price.B (the "sep" 
#' parameter lets you tell the model how to parse the data)
tr = mlogit.data(Train, choice = "choice", shape = "wide",  varying = 4:11, sep= "_", id="id")
head(tr) #' notice: each row in our original data is broken down to two

#' Converting price to euros and time to hours 
tr$price = (tr$price / 100) * 2.20371	# Original price in Netherlands Antillean Guilder
tr$time = tr$time / 60

#' use MNL model to estimate our parameters 
#' include intercept if for options with the same features eg cost, wait time, the value is different
model = mlogit(choice ~ price + time + change + comfort | -1, data = tr)
summary(model) #' do the coefficients make sense?

#' how much would a person pay per 1 unit increase on the other features?
coef(model)[-1] / coef(model)[1]

#' PREDICTION & SENSITIVITY ANALYSIS

#' Suppose we give a person two train ticket options:

ticketA.price= 60   
ticketA.time = 2.5   
ticketA.change =  1    
ticketA.comfort = 1    

ticketB.price= 100    
ticketB.time = 2.5   
ticketB.change =  1    
ticketB.comfort = 0   


VT1 = exp(coef(model)[1]*ticketA.price + coef(model)[2]*ticketA.time +
            coef(model)[3]*ticketA.change + coef(model)[4]*ticketA.comfort)
VT2 = exp(coef(model)[1]*ticketB.price + coef(model)[2]*ticketB.time +
            coef(model)[3]*ticketB.change + coef(model)[4]*ticketB.comfort)

Share2 = VT2/(VT1 + VT2)
as.numeric(Share2)

#' let's play around, reduce the price of ticket B to 80 and see how its market share changes
VT2 = exp(coef(model)[1]*80 + coef(model)[2]*ticketB.time +
            coef(model)[3]*ticketB.change + coef(model)[4]*ticketB.comfort)

Share2 = VT2/(VT1 + VT2)
as.numeric(Share2)


