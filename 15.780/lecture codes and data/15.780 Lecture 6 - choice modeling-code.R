# R script for Lecture 4: Choice Modeling
# Examples taken from mlogit documentation: https://cran.r-project.org/web/packages/mlogit/vignettes/mlogit.pdf

# In case we want graphics
library("grDevices")
# Open windows properly in OS/Windows
if(.Platform$OS.type=="windows") {
  quartz<-function() windows()
}

# if needed: install.packages("mlogit")
library("mlogit")

# Load and view data
data("Train", package = "mlogit")
head(Train, 6)	# show the first six rows of data

# Tell R about the data
# Data for individual choices between two train tickets that vary in 4 attributes: 
# price, duration, number of changes, comfort level (lower level means more comfortable)
# The same individual made multiple choices:
# 	an individual is labeled by id, 
#	the different choice scenarios experienced by an individual are labeled by choiceid, 
#	the choice made in each scenario was stored in the column choice
# The two ticket options are labeled choice1 and choice2
Tr <- mlogit.data(Train, choice = "choice", shape = "wide",
                  varying = 4:11, alt.levels = c("A", "B"), sep = "_", id="id")
head(Tr, 6)

# Converting units to hours and euros
Tr$price <- Tr$price/100 * 2.20371	# Original price in Netherlands Antillean Guilder
Tr$time <- Tr$time/60

# Standard MNL model with 4 attributes and no intercept
# generic coefficient for alternative specific variable |
# individual specific variable |
# alternative specific coefficient for alternative specific variable
Train.ml <- mlogit(choice ~ price + time + change + comfort | -1, Tr)
summary(Train.ml)

# Coefficients - interpret by comparing to price
coef(Train.ml)[-1]/coef(Train.ml)[1]

# Prediction and sensitivity analysis
# Suppose we offer two ticket options with the following attributes:
#	Ticket 1: price = 60 euros, time = 2.5 hours, no. of changes = 1, comfort level = 1
#	Ticket 2: price = 100 euros, time = 2.5 hours, no. of changes = 1, comfort level = 0
# What is the predicted market share of each ticket?
VT1 = exp(coef(Train.ml)[1]*60 + coef(Train.ml)[2]*2.5 + coef(Train.ml)[3]*1 + coef(Train.ml)[4]*1)
VT2 = exp(coef(Train.ml)[1]*100 + coef(Train.ml)[2]*2.5 + coef(Train.ml)[3]*1 + coef(Train.ml)[4]*0)
Share2 = VT2/(VT1 + VT2)
as.numeric(Share2)

# Suppose now we reduce Ticket 2's price to 80 euros, how much increase in market share would we expect?
VT22 = exp(coef(Train.ml)[1]*80 + coef(Train.ml)[2]*2.5 + coef(Train.ml)[3]*1 + coef(Train.ml)[4]*0)
Share22 = VT22/(VT1 + VT22)
as.numeric(Share22)
as.numeric((Share22/Share2 - 1)*100)
