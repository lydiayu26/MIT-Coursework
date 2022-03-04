#' -----------------------------------------------------------------
#' `15.774/780 Fall 2021`
#' `Recitation 1 - ABCs of R`
#' 
#' By the end of this recitation, you should know:
#'     - How to use R as a calculator
#'     - The difference between some variable types
#'     - How to set your working directory
#'     - How to load a dataset
#'     - How to interact with a data frame
#'     - The basics of vectorized operations
#' -----------------------------------------------------------------

#' Before proceeding, please make sure that you have downloaded the 
#' dataset `retail_sales.csv` to your computer. 



#' -----------------------------------------------------------------
#' INTRODUCTION TO RStudio

# Everything following a pound sign is a comment. Running a comment 
# accomplishes nothing. 

#' Adding a tick ' after the pound sign allows *prettier* `formatting`
#  Without a tick ' no *prettier* `formatting`
#' Use ticked comments to make your code/comments more readable. 

#' To allow us to go back to code we've written, we will be saving it 
#' in *scripts*. What you're reading now is a script!
#' 
#' You can open scripts by clicking `File` -> `Open File`. Navigate to 
#' where you saved the files, select the script you want to open (*.R file)
#' and click `Open`.
#' 
#' Alternatively, use the bottom right window in RStudio (Files pane)
#' to navigate your file system and open .R files.
#' 
#' 1. *Scripts* will occupy the top left window, where you can edit them.
#' 2. Code won't execute unless you run them in the *console* in the 
#'    bottom left window. 
#' 3. The top right window (Environment pane) shows info on objects you 
#'    have created by running stuff in the console. 
#'      - We'll see more of that in a sec. 
#'      - Switch to History pane to see all the commands you've run.
#' 4. The bottom right window is used primarily for navigation (Files pane) and 
#'    displaying plots (Plots pane). 
#'      - Again we'll see more of this in a sec. 
#'    

#' -----------------------------------------------------------------
#' BASIC CALCULATIONS IN R

#' You can always run commands by typing them in the *console*.
#' 
#' To run commands from a *script*, you can do any of the following: 
#'    1) Copy paste into console
#'    2) Highlight the command in the script and:
#'        a) Ctrl + R or Ctrl + Enter (Windows)
#'        b) Command + R or Command + Enter (Mac)
#'    3) If nothing is highlighted, (2) will execute the command 
#'       where your cursor is.
library(DMwR)

#' Try running these lines:
13*3
4^7 
#' The [1] is just R's way of labeling the output.

#' Scroll through previous commands using up and down arrows in the console.
  
#' ALL THE MATH!
543670/1.456767
13.0 / 6.5

#' FUNCTIONS AND VARIABLES
  
#' A function can take in several arguments or inputs, 
#' and returns an output value. Example:
sqrt(2)
abs(-65)

#' Get help on any function:
?sqrt

#' Save the output to a variable. 
SquareRoot2 = sqrt(2)

#' See the value by typing its name
SquareRoot2

#' Basic variable naming rules: 
#'    * Don't use spaces (periods or capital letters instead)
#'    * Don't start names with a number
#'    * Variable names are case sensitive

#' You can also use <- instead of = for assignment. There is NO difference, 
#' though apparently people have strong opinions (?!?!?).
HoursYear <- 365*24 

#' We have the usual comparison operators: `==`, `>`, `>=`, `<`, `<=`
#' which return `TRUE` or `FALSE` (these are reverse keywords)
3 == 3.0
4 > 2

#' Note that you can use `T` and `F` for shorthand TRUE/FALSE
T == TRUE
F == FALSE

#' And finally logical operators:
T & F # TRUE AND FALSE = FALSE
T | F # TRUE OR FALSE = TRUE
!T
#' `CAUTION:` NOTE how we used single `&`/`|` unlike some other languages
#' `&&`/`||` also exist in R but YOU SHOULD NOT USE THEM, they work weirdly. 
#' If you're curious about the difference, come see me after class. 

#' -----------------------------------------------------------------
#' VECTORS
#' A *vector* is a series of values, stored as the same object.
#' 
#' Create a vector using the `c()` function:
c(2,3,5,8,13)

#' You can use variables you've created:
c(2,3,5,8,13, HoursYear)

#' Vector of Students names: 
Students1 = c("John", "Paul")
Students1

#' `c()` actually stands for concatenate, you can combine any vectors into one:
Students2 = c("Ringo", "George")
Students = c(Students1, Students2, "Ravi")

#' The length of a vector:
length(Students)

#' All elements of a vector need to have the *same type*. You can see
#' the type with the `class()` function. 
class(Students) 

#' Students' grades:
Grades = c(85, 92, 98, 86, 80)

#' Numeric does *not* distinguish between integers and floats.
class(Grades)

#' Access elements using square brackets
Students[1]
Grades[3]

#' `seq()` function: 
?seq #what does it do?
Sequence = seq(-13,13,3) #see it in action!
Sequence

#' -----------------------------------------------------------------
#' VECTORIZATION
#' 
#' One of R's most useful features is `vectorization`, but it is also
#' most confusing for those used to other languages.
#' 
#' In R, (most) operators and functions work *element-wise*. 

v1 = c(2,3,4,5)
v2 = c(4,9,16,25)

sqrt(v2) # Returns a vector of element-wise square roots
sqrt(v2) == v1
v1 + v2 # element wise addition
v1 * v2 


#' Logical operations are also vectorized element-wise:
c(T, F) & c(T, T)

#' Here's the hardest part to get used to: in R *SCALARS ARE LENGTH-1 VECTORS*
a = 2
length(a)

#' In a vectorized operation, length-1 vectors will be implicitly "recycled"
#' up to the length of the other vectors:
a * v1
Grades / 100

#' Vectorization is useful also for subsetting vectors (and tables)
#' Create a vector of true/falses for each element
Grades
Grades > 90 # F T T F T

#' Indexing a vector by a T/F of the same length keeps only the TRUE elements:
Students[c(F, T, T, F, F)]

# So we can use conditional statements in the brackets!:
Students[Grades > 90]

#' We can also select multiple elements by using vectors of indices:
Students[c(1, 4, 5)]


#' -----------------------------------------------------------------
#' DATA FRAMES
#' 
#' R has been designed to be intuitive and easy to use with tabular data, 
#' stored in objects called `data frames` (think Excel spreadsheet). 

#' Create data frames with the `data.frame()` function:
Data = data.frame(Students, Grades)
Data

#' You can access elements using `[,]` and their indices:
Data[3,2]

#' Refer to columns by their name as well:
Data[3,'Grades']

#' Pick all columns by ommitting the column name index:
Data[3,] # Don't forget the comma!

#' Extract multiple rows with vectors of indices:
Data[1:3,'Grades']
Data[c(3,1,5),]
Data[seq(1,5,by=2),]

#' At a high level, data frames are a list of *fixed-length vectors*.
#' The $ operator extracts a column as a vector:
Data$Students
Data$Grades[1:3]

#' We can do any indexing we did before!
Data$Students[Data$Grades > 90]
Data[Data$Grades > 90, ]

#' Add a new variable (Age) by assigning to the vector:
Data$Age = c(40, 77, 79, 58, 92)
Data

#' New observations for Bill and Ted
Students = c("Bill","Ted")
Grades = c(82, 96)
Age = c(18, 18) 
NewData = data.frame(Students, Grades, Age)

#' Combine our new data with the old data by using `rbind()` (row-bind):
AllData = rbind(Data, NewData)
?cbind # I wonder what this is?


#' -----------------------------------------------------------------
#' WORKING DIRECTORIES AND READING CSV
#'
#' When you need to import data from an external file, you need to be aware
#' of your *working directory*. This is the folder where R will load data from
#' by default.
 
#' You can see your current working directory with `getwd()`
getwd()

#' There are many ways to change your working directory.
#'    1) Navigate to the directory you want in the Files pane (bottom right), 
#'       then click on `More` -> `Set as Working Directory`
#'    2) At the top bar, click `Session` -> `Set Working Directory` -> `Choose Directory`
#'    3) Set the WD to the current script's location with
#'       `Session` -> `Set Working Directory` -> `To Source File Location`
#'    4) With the `setwd()` command in the console


#' To read a data set from a csv, use the `read.csv(filename)` function. 
#' CAUTION: This won't work if your working directory does not include the 
#' file you're trying to load...
sales = read.csv("retail_sales.csv")

View(sales)

#' The `str()` function gives you information about the structure of the data...
str(sales)

#' Sales of a product in markets:
#' `Sales`: Number of units sold in ZIP code
#' `Income`: Median income in the ZIP code
#' `Population`: Popoulation of the ZIP code
#' `Market`: Whether it's considered Urban/Suburban/Rural

#' Statistical summary of the columns:
summary(sales)

#' Recall that the `$` extracts a data frame column as a vector
sales$Sales

# Statistics about this variable
mean(sales$Sales)
max(sales$Sales)
min(sales$Sales)
sd(sales$Sales)
summary(sales$Sales)

#' Identify the index of tract corresponding to max and min
which.min(sales$Sales)
sales[which.min(sales$Sales),]

which.max(sales$Sales)
sales[which.max(sales$Sales),]

#' Lte's try some more *subsetting*. We might wish to create new data frames by
#' filtering out some rows (e.g. outliers). We can 
filtsales = sales[sales$Market == "Urban" & sales$Sales > mean(sales$Sales),]
filtsales

#' That looks kind of ugly... We can also use the `subset()` function, which
#' allows us to skip the ugly `$` notation -- we straight up use the column 
#' names!
filtsales2 = subset(sales, Market == "Urban" & Sales > mean(Sales))
filtsales2

#' You can check that the data frames are the same!
dim(filtsales)
dim(filtsales2)

#' -----------------------------------------------------------------
#' PLOTS

#' The `plot(x, y)` creates a new scatter plot. The arguments `x` and `y` 
#' are the x- and y-coords of the points. 
plot(sales$Income, sales$Sales)

#' Arguments change the appearance of the plot:
plot(sales$Income, 
     sales$Sales, 
     xlab = "Income",
     ylab = "Sales", 
     main = "An Example Scatter Plot", 
     pch = 16)

#' `points()` will add more points to the current plot. For example, we 
#' can add blue points for Urban markets:
points(sales$Income[sales$Market == "Urban"],
       sales$Sales[sales$Market == "Urban"], 
       col = "blue", 
       pch = 19)

#' You can save a plot in RStudio's *Plots* pane (bottom right) by clicking
#' on `Export`. You can save as an image, PDF or copy into your clipboard.

#' Histogram
hist(sales$Sales, breaks = 30)

#' Tabulate values with `table()`
table(sales$Market, dnn = "Market") #' `dnn` (optional) sets the title

#' Tabulate multiple columns by adding a second column:
table(sales$Market, sales$Sales > 445, dnn = c("Market", "Sales > 455?"))

#' Use the output of `table()` to create bar plots:
barplot(table(sales$Market), 
        xlab = "Market",
        ylab ="Number of ZIP codes")

