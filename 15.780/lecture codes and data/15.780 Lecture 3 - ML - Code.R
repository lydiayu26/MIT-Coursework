##########
#Polynomial Regression
#########

nonlinear = read.csv("nonlinear.csv")
x = nonlinear$x
y = nonlinear$y

plot(x, y, pch = 16, main = "Nonlinear Relationship")



#This will allow us to plot the resulting polynomial
polyplot = function(x, reg)
{
  co = reg$coef
  deg = 0:(length(co)-1)
  sum(co*x^deg)
}
PolyPlot = Vectorize(polyplot, vectorize.args = "x")


#Run Polynomial Regressions with degrees 1,2,3,4, and 15
plot(x,y, main = "Nonlinear Function", ylim = c(-20, 40), pch = 16)
line = lm(y~x)
abline(line, col = "black", lwd = 2)

quad = lm(y~poly(x, degree = 2, raw = T))

quad #our quadratic is 4.025 + 3.972 x + 4.162*x^2

curve(PolyPlot(x,quad), add = T, col = "forestgreen", lty = 2, lwd = 2)

cube = lm(y~poly(x, degree=3, raw = T))
curve(PolyPlot(x, cube), add = T, col = "orange", lty = 3, lwd=2)

quartic = lm(y~poly(x, degree=4, raw = T))
curve(PolyPlot(x, quartic), add = T, col = "blue", lty = 4, lwd = 2)

fifteenth = lm(y~poly(x, degree=15, raw = T))
curve(PolyPlot(x, fifteenth), add = T, col = "purple", lty = 5, lwd = 2)
legend("top", c("1st", "2nd", "3rd", "4th", "15th"), col = c("black", "forestgreen", "orange", "blue", "purple"), lty = c(1,2,3,4,5), bty = "n")

summary(line)$r.squared
summary(quad)$r.squared
summary(cube)$r.squared
summary(quartic)$r.squared
summary(fifteenth)$r.squared


#this is the expectation for the function
EY = function(x) 
{
  x + 2*x^2 + x^3 + 10*x*sin(1.25*x)
}

plot(x,y, main = "Nonlinear Function, True Expectation", type = "n", ylim = c(-20, 40))
curve(EY, add = T, col = "red", lwd = 3)
abline(line, col = "black", lwd = 2)
curve(PolyPlot(x,quad), add = T, col = "forestgreen", lty = 2, lwd = 2)
curve(PolyPlot(x, cube), add = T, col = "orange", lty = 3, lwd=2)
curve(PolyPlot(x, quartic), add = T, col = "blue", lty = 4, lwd = 2)
curve(PolyPlot(x, fifteenth), add = T, col = "purple", lty = 5, lwd = 2)
legend("top", c("Truth", "1st", "2nd", "3rd", "4th", "15th"), col = c("red", "black", "forestgreen", "orange", "blue", "purple"), lty = c(1,1,2,3,4,5), bty = "n")

#Logistic Regression

ost = read.csv("osteo.csv")

#Be sure to set the seed first before test/training split! 
#otherwise output won't match lecture notes
set.seed(800)
idx = sample(1:nrow(ost), size = .7*nrow(ost))
train = ost[idx, ]
test = ost[-idx,]

#Here's the logit with just weight as the predictor
logit.ost = glm(Osteo~Weight, family = "binomial", data = train)
plot(jitter(train$Weight,2), jitter(train$Osteo,.2), pch =  16, ylab = "Osteoperosis", xlab = "Weight (lbs)", cex = .5, main = "Logstic Fit (Points Jittered to Avoid Overplotting)", ylim = c(-.1, 1.1), xlim = c(90, 350))
bvec = logit.ost$coef

#here's the resulting function for p(x)
curve(exp(bvec[1] + bvec[2]*x)/(1+exp(bvec[1] + bvec[2]*x)), add = T)

#Here's our logistic regression model
mult.logit= glm(Osteo~., family = "binomial", data = train)
mult.logit
summary(mult.logit)


#Here are our predictions on the training set
predict.train = predict(mult.logit, newdata= train, type = "response")

#Based on a cost analysis, we decided to classify 
#an individual as having osteoporosis if 
#p >= 0.1

Classify.Osteo = (predict.train >= 0.1)*1
Actual.Osteo = train$Osteo
table(Actual.Osteo, Classify.Osteo)


#this is a quick way to assign costs to the test set based
#on what a mistake would mean

cost.vector = ifelse(test$Osteo==1, 3600, 400)

#if Osteoporosis - mistake gives rise to cost of 3600
#otherwise - mistake gives rise to 400 in cost

prediction.test  = predict(mult.logit, newdata= test, type = "response")

#classify the test set as having osteoporosis if 
classify.test = (prediction.test >= 0.1)

Osteo.test = test$Osteo
cost.simple = sum(cost.vector*(Osteo.test != classify.test))
cost.simple
