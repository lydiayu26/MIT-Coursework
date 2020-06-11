pi = 3.14159
radius = 2.2
# area of circle equation <- this is a comment
area = pi*(radius**2)
print(area)
#
## change values of radius <- another comment
## use comments to help others understand what you are doing in code
radius = radius + 1
print(area)     # area doesn't change
#
## recalculate area using new values
area = pi*(radius**2)
print(area)
#
#################################################
x = 1
x_str = str(x)
print("my fav num is", x, ".", "x =", x)
print("my fav num is " + x_str + ". " + "x = " + x_str)
#
#################################################
text = input("Type anything... ")
print(5*text)
#
num = int(input("Type anything... "))
print(5*num)
#
#################################################
#Try Newton Raphson for cube root
print('Find the cube root of x')
x = 9
g = 3
print('Current estimate cubed =', g**3)
nextGuess = g - ((g**3 - x)/(3*g**2))
print('Next guess to try =', nextGuess)
#
#################################################
##Correct indentation
x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: "))
if x == y:
    print(x,"and",y)
    print("These are equal!")

##Incorrect indentation
x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: "))
if x == y:
    print(x,"and",y)
print("These are equal!")

##############################
##### COMMENTING LINES #######
##############################
## to comment MANY lines at a time, highlight all of them then CTRL+1
## do CTRL+1 again to uncomment them
## try it on the next few lines below!
#
##area = pi*(radius**2)
##print(area)
##radius = radius + 1
##area = pi*(radius**2)
##print(area)
#
##############################
##### AUTOCOMPLETE #######
##############################
## Spyder can autocomplete names for you
## start typing a variable name defined in your program and hit tab 
## before you finish typing -- try it below
#
## define a variable
#a_very_long_variable_name_dont_name_them_this_long_pls = 0
#
## below, start typing a_ve then hit tab... cool, right!
## use autocomplete to change the value of that variable to 1
#
## use autocomplete to write a line that prints the value of that long variable
## notice that Spyder also automatically adds the closed parentheses for you!
