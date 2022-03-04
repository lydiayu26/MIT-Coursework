library(mlogit)

# PROBLEM 1
commute = read.csv('commuteFall2020.csv')

# 1) data preprocessing
# create columns for total travel time -- bus.wait + bus.travel; car.travel
commute$time_CAR = commute$Car.Travel
commute$time_BUS = commute$Bus.Travel + commute$Bus.Wait
# create columns for cost -- BusFare; ParkingCost
commute$cost_CAR = commute$ParkingCost
commute$cost_BUS = commute$BusFare
# drop unnecessary columns from df
commute = subset(commute, select = -c(Car.Travel, Bus.Travel, Bus.Wait, ParkingCost, BusFare))
# data is wide so adding id col is not necessary


# 2) fit MNL model
com = mlogit.data(commute, choice = "Choice", shape = "wide",  varying = 3:6, sep= "_")
head(com)
model = mlogit(Choice ~ time + cost | HHIncome -1, data = com)
summary(model)


# 3) probability that person from group H and L will take a car
car_time_L = 25
car_cost_L = 3
bus_time_L = 40 + 5
bus_cost_L = 0.8
income_L = 40000

car_time_H = 40
car_cost_H = 8
bus_time_H = 60 + 10
bus_cost_H = 2
income_H = 80000

time_coef = coef(model)[1]
cost_coef = coef(model)[2]
income_coef = coef(model)[3]

# get values of car/bus for group L
VC_L = exp(time_coef*car_time_L + cost_coef*car_cost_L + income_coef*income_L)
VB_L = exp(time_coef*bus_time_L + cost_coef*bus_cost_L + income_coef*income_L)
# get probability of choosing car for group L
share_car_L = VC_L / (VC_L + VB_L)
as.numeric(share_car_L)

# get values of car/bus for group H
VC_H = exp(time_coef*car_time_H + cost_coef*car_cost_H + income_coef*income_H)
VB_H = exp(time_coef*bus_time_H + cost_coef*bus_cost_H + income_coef*income_H)
# get probability of choosing car for group L
share_car_H = VC_H / (VC_H + VB_H)
as.numeric(share_car_H)


# 4) strategies for increasing bus ridership
# previous probabilities for riding bus:
share_bus_L = VB_L / (VC_L + VB_L)
share_bus_H = VB_H / (VC_H + VB_H)
as.numeric(share_bus_L)
as.numeric(share_bus_H)

# a) reducing bus fare by 50 cents for both L and H
bus_cost_L = 0.8 - 0.5
bus_cost_H = 2 - 0.5
VC_L = exp(time_coef*car_time_L + cost_coef*car_cost_L + income_coef*income_L)
VB_L = exp(time_coef*bus_time_L + cost_coef*bus_cost_L + income_coef*income_L)
VC_H = exp(time_coef*car_time_H + cost_coef*car_cost_H + income_coef*income_H)
VB_H = exp(time_coef*bus_time_H + cost_coef*bus_cost_H + income_coef*income_H)
share_bus_L = VB_L / (VC_L + VB_L)
share_bus_H = VB_H / (VC_H + VB_H)
as.numeric(share_bus_L)
as.numeric(share_bus_H)

# b) bus waiting times cut in half
# reset bus cost
bus_cost_L = 0.8
bus_cost_H = 2
# change bus time
bus_time_L = 40 + 5/2
bus_time_H = 60 + 10/2
VC_L = exp(time_coef*car_time_L + cost_coef*car_cost_L + income_coef*income_L)
VB_L = exp(time_coef*bus_time_L + cost_coef*bus_cost_L + income_coef*income_L)
VC_H = exp(time_coef*car_time_H + cost_coef*car_cost_H + income_coef*income_H)
VB_H = exp(time_coef*bus_time_H + cost_coef*bus_cost_H + income_coef*income_H)
share_bus_L = VB_L / (VC_L + VB_L)
share_bus_H = VB_H / (VC_H + VB_H)
as.numeric(share_bus_L)
as.numeric(share_bus_H)

# c) doubling parking costs
# reset bus time
bus_time_L = 40 + 5
bus_time_H = 60 + 10
# change car cost
car_cost_L = 3 * 2
car_cost_H = 8 * 2
VC_L = exp(time_coef*car_time_L + cost_coef*car_cost_L + income_coef*income_L)
VB_L = exp(time_coef*bus_time_L + cost_coef*bus_cost_L + income_coef*income_L)
VC_H = exp(time_coef*car_time_H + cost_coef*car_cost_H + income_coef*income_H)
VB_H = exp(time_coef*bus_time_H + cost_coef*bus_cost_H + income_coef*income_H)
share_bus_L = VB_L / (VC_L + VB_L)
share_bus_H = VB_H / (VC_H + VB_H)
as.numeric(share_bus_L)
as.numeric(share_bus_H)




# PROBLEM 2

# 1) get revenues for each possible RO assortment
w_gs99 = 2
r_gs99 = 400
w_gs100 = 2.2
r_gs100 = 499
w_i99 = 2.1
r_i99 = 500
w_i100 = 2.5
r_i100 = 600

# RO set 1: iphone 100
r1 = r_i100 * w_i100 / (1 + w_i100)
r1

# RO set 2: iphone 100, iphone 99
r2 = (r_i100 * w_i100 + r_i99 * w_i99) / (1 + w_i100 + w_i99)
r2

# RO set 3: iphone 100, iphone 99, galaxy s100
r3 = (r_i100 * w_i100 + r_i99 * w_i99 + r_gs100 * w_gs100) /
         (1 + w_i100 + w_i99 + w_gs100)
r3

# RO set 4: iphone 100, iphone 99, galaxy s100, galaxy s99
r4 = (r_i100 * w_i100 + r_i99 * w_i99 + r_gs100 * w_gs100 + r_gs99 * w_gs99) /
  (1 + w_i100 + w_i99 + w_gs100 + w_gs99)
r4


# 2) calculate expected revenue from optimal assortment with NEVER customers
w_gs99 = 0.5 * (0.1 + 2)
r_gs99 = 400
w_gs100 = 0.5 * (0.1 + 2.2)
r_gs100 = 499
w_i99 = 0.5 * (2.1 + 0.01)
r_i99 = 500
w_i100 = 0.5 * (2.5 + 0.01)
r_i100 = 600

r3 = (r_i100 * w_i100 + r_i99 * w_i99 + r_gs100 * w_gs100) /
  (1 + w_i100 + w_i99 + w_gs100)
r3


# 3) show a different assortment for each customer type
# NEVER Galaxy customers:
w_gs99 = 0.1
r_gs99 = 400
w_gs100 = 0.1
r_gs100 = 499
w_i99 = 2.1
r_i99 = 500
w_i100 = 2.5
r_i100 = 600

# RO set 1: iphone 100
r1 = r_i100 * w_i100 / (1 + w_i100)
r1

# RO set 2: iphone 100, iphone 99
r2 = (r_i100 * w_i100 + r_i99 * w_i99) / (1 + w_i100 + w_i99)
r2

# RO set 3: iphone 100, iphone 99, galaxy s100
r3 = (r_i100 * w_i100 + r_i99 * w_i99 + r_gs100 * w_gs100) /
  (1 + w_i100 + w_i99 + w_gs100)
r3

# RO set 4: iphone 100, iphone 99, galaxy s100, galaxy s99
r4 = (r_i100 * w_i100 + r_i99 * w_i99 + r_gs100 * w_gs100 + r_gs99 * w_gs99) /
  (1 + w_i100 + w_i99 + w_gs100 + w_gs99)
r4

# NEVER iPhone customers:
w_gs99 = 2
r_gs99 = 400
w_gs100 = 2.2
r_gs100 = 499
w_i99 = 0.01
r_i99 = 500
w_i100 = 0.01
r_i100 = 600

# RO set 1: iphone 100
r1 = r_i100 * w_i100 / (1 + w_i100)
r1

# RO set 2: iphone 100, iphone 99
r2 = (r_i100 * w_i100 + r_i99 * w_i99) / (1 + w_i100 + w_i99)
r2

# RO set 3: iphone 100, iphone 99, galaxy s100
r3 = (r_i100 * w_i100 + r_i99 * w_i99 + r_gs100 * w_gs100) /
  (1 + w_i100 + w_i99 + w_gs100)
r3

# RO set 4: iphone 100, iphone 99, galaxy s100, galaxy s99
r4 = (r_i100 * w_i100 + r_i99 * w_i99 + r_gs100 * w_gs100 + r_gs99 * w_gs99) /
  (1 + w_i100 + w_i99 + w_gs100 + w_gs99)
r4

# b. expected revenue when showing optimal assortment for each
(365.6705 + 456.1228) / 2
