#' -----------------------------------------------------------------
#' `15.774/780 Fall 2021`
#' `Recitation 2 - Data Quality`
#' 
#' By the end of this recitation, you should know:
#'     - How to work with NA values in R
#'     - How to do basic imputation for missing values
#'     - Looking for data inconsistencies
#'     - Some ways to detect outliers in R
#' -----------------------------------------------------------------

#' We will be using various new packages today, so if you haven't
#' used them before run the following line to install them: 
#' `install.packages(c("mice", "editrules", "Hmisc", "PivotalR"))`

#' You'll also need the `DMwR` library, which unfortunatelt doesn't
#' exist anymore. There are (short) instructions on how to install
#' it.

#' Once packages have been installed (once) you can load them with
#' the `library()` function:
library(mice)
library(editrules)
library(Hmisc)
library(PivotalR)
library(DMwR)

#' -----------------------------------------------------------------
#' INCONSISTENCIES
#' -----------------------------------------------------------------
#' The first step of any analysis is *always* understanding your
#' dataset. This is an art, since it depends on context, but
#' here are some questions to get you started...
#'    - Are variable values of the right *type*? 
#'    - Do numerical values have a reasonable *range*?
#'    - Are there specific groups where you'd expect different 
#'      distributions?


#' Let's make some messy toy data.
students = c("John", "Paul", "Ringo", "George", "Ravi")
grade = c(85, 92, 93, 86, -5)
age = c(23, "24", 27, 900, 31) 
df = data.frame(students, grade, age) 

#' First thing we want to do is check data types. Is everything 
#' what you expect?
class(df$students)
class(df$grade)
class(df$age)

#' RANT: R saw that one element of *age* was a string. Since
#' vectors/columns can only have one type, it decided to make
#' the entire column a `character` type. Why doesn't it throw 
#' an error? Because R...

#' In any case, functions like `as.numeric()`, `as.character()`
#' etc. will help you convert different columns:
df$age
as.numeric(df$age)

#' This didn't convert the values in the data frame, we need to
#' assign it back:
df$age = as.numeric(df$age)


#' That was a simple example, but it comes up all the time! 
#' Datasets might include $ signs for prices, or weird formats 
#' for dates (check out the `lubridate` library for easy date
#' manipulation). You'll often have to convert types.


#' Next up, let's look for logical inconsistencies. What are
#' the ranges you'd expect for age/grade?
df$age > 150

#' Cool thing about R: `TRUE` counts as 1, and `FALSE` counts as 
#' zero. So I can count how many grades are "bad" by summing 
#' over the T/F vector.
sum(df$grade < 0 | df$grade > 100)


#' The `editrules` makes it easy to explore inconsistencies. 
#' We can define an *editset* of rules to check against our data. 
library(editrules)
E = editset(c("grade < 0", "age > 150"))
V = violatedEdits(E, df)

#' It tells us, for each row, which rules were violated...
V

#' So we can check, say, how many rows violated each rule...
V[,"num1"] | V[,"num2"] #| V[,"num3"]

sum(V[,"num1"] | V[,"num2"] | V[,"num3"])


#' -----------------------------------------------------------------
#' MISSING VALUES
#' -----------------------------------------------------------------
#' Missing values are also a part of life. Again, understanding what
#' they represent, and how it would impact your analysis is crucial.
#'    - Are they missing at random?
#'    - Or are they all from, say, a particular group?
#'    - Is the column high variance, so the mean might be
#'      a good approximation?
#'    - Or do I need KNN?


#' R encodes missing values by a special `NA` value. 
students = c("John", "Paul", "Ringo", "George", "Ravi")
grade = c(89, 92, NA, 86, NA)
age = c(23, 24, 27, NA, 31) 
df = data.frame(students, grade, age) 


#' NAs mess with various functions in different ways:
mean(df$grade)
mean(df$grade, na.rm = T)

#' The `is.na()` function is your best friend:
is.na(df)
!is.na(df$age)

#' Again, you can sum the T/F vector to see how many/what 
#' percentage of entries
#' are missing:
sum(is.na(df$grade))
mean(is.na(df$age))

#' We can use `is.na()` for subsetting, just like last recitation!
newdf = df[!is.na(df$age),]
newdf

#' Also useful: `complete.cases()` returns T/F for the rows which
#' contain an NA in any column.
complete.cases(df)

#' Or `na.omit()` which filters the dataframe to remove rows with NAs
na.omit(df)

#' -----------------------------------------------------------------
#' MISSING VALUE IMPUTATION
#' -----------------------------------------------------------------
#' It's usually a bad idea to remove missing values completely. Less
#' data usually means less model power. Instead we like to impute. 
#' Again (and I'm getting tired of saying this) how to best do this
#' also depends on your application. Let's look at some different
#' data...

#' The `data` function  loads 
data(abalone, package = "PivotalR")
View(abalone)

#' I'm going to remove some columns to make it slightly easier to 
#' look at. I'll also save a copy of the full data for later.
abalone = abalone[,-c(1,8,9)]
original = abalone

#' This dataset has no NA values, so I can't teach you anything!
#' Or I can break it and then teach you. Let's randomly introduce
#' some NAs.

#' The `sample()` function allows us to pick random numbers from
#' a sequence:
sample(1:100, 5)

#' We can overwrite some random values with NA:
set.seed(80)       # Used to get the same random numbers
abalone$length[sample(1:nrow(abalone), 42)] = NA
abalone$diameter[sample(1:nrow(abalone), 100)] = NA

#' Now are there NAs?
sum(is.na(abalone$length))

#' The `md.pattern()` function from `mice` is nice for checking
#' the overall presence of NAs:
library(mice)
md.pattern(abalone)
dev.off() # Clear plot

#' One way to deal with NAs is to replace them with the mean/median
#' of the column. The `impute()` function from `Hmisc` can help us
#' with this:
library(Hmisc)
impute(abalone$length, mean)
impute(abalone$diameter, median)


#' In real life, we don't know if this imputation is any good. 
#' Here, we know the original data so we can check! Let's learn 
#' how to create a function to calculate MAPE:
MAPE = function(actual, imputed) {
    percent_errors = abs(actual - imputed) / abs(actual)
    return(mean(percent_errors))
}

#' Let's use the function to compute MAPE of our imputation.
org   = original$length               # The uncorrupted data
imp   = impute(abalone$length, mean)  # My imputation 
# find the cells where we introduced NAs
miss  = is.na(abalone$length)         # T/F which elements were NA
# get the MAPE of the original values vs imputed values
MAPE(org[miss], imp[miss])   

#' A MAPE of 30% average error is pretty bad? Can anything do better?
#' The `DMwR` package allows us to do kNN imputation. We will impute
#' length based on height and diameter:
knnOut = knnImputation(abalone[,c("length", 
                                  "height", 
                                  "diameter", 
                                  "shucked")], 
                       k = 10) 

#' Let's try to compute MAPE again:
org   = original$length               # The uncorrupted data
imp   = knnOut$length                 # My imputation 
miss  = is.na(abalone$length)         # T/F which elements were NA
MAPE(org[miss], imp[miss])            # 7%, much better. 


#' -----------------------------------------------------------------
#' OUTLIERS
#' -----------------------------------------------------------------
#' What is an *outlier* depends on what you're trying to do. We 
#' looked at a few ways of looking for them: 
#'    * Univariate:   is a point outside the typical range in a 
#'                    specific variable?
#'    * Bivariate:    is it outside the typical range, after 
#'                    accounting for some other variable?
#'    * Multivariate: is it influential (high Cook's distance)?
#'                    i.e. does excluding it from a regression
#'                    model change predictions of other points
#'                    significantly?

#' We'll use the abalone dataset to work through some examples.
#' Reload it:
data(abalone, package = "PivotalR")

#' UNIVARIATE
#' We can look at a histogram with `hist()`
hist(abalone$length, breaks=10, xlab = "Length")           
hist(abalone$height, breaks=30, xlab = "Height") 


#' We can also look at `boxplot()` which does the IQR outlier
#' calculation for us:
boxplot(abalone$height, horizontal = TRUE, xlab = "Height")

#' BIVARIATE
#' If we want to account for a categorical variable, side-by-side
#' `boxplot()` are good. We use a *formula* (the ~ notation), with 
#' the continuous vector on the left and categorical groups on the 
#' right:
boxplot(abalone$shucked ~ abalone$sex, xlab = "Sex", ylab = "Shucked weight")

#' If we want to account for a continuous variable, we can use
#' a scatter plot:
plot(abalone$height, abalone$length, xlab="Height", ylab="Length", 
     xlim=c(0, 0.27))

#' MULTIVARIATE
#' We can calculate cook's distance by running a regression with 
#' any variable's we want (see Recitation 2) and using the
#' `cooks.distance()` function:
linreg = lm(shucked ~ length + height + diameter, data = abalone)
cd = cooks.distance(linreg) # The influence of each point in the data
plot(cd, ylab ="Cook's distance")

#' We can use the `which.max()` function from last time to find
#' the point with the most influence:
cd[which.max(cd)]
abalone[which.max(cd),]
