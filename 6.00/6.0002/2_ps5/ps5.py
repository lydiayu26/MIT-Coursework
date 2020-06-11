# -*- coding: utf-8 -*-
# Problem Set 5: Modeling Temperature Change
# Name: Lydia Yu
# Collaborators (discussion): Wilson Spearman
# Time: 6 hrs

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import re

# cities in our weather data
CITIES = [
    'BOSTON',
    'SEATTLE',
    'SAN DIEGO',
    'PHOENIX',
    'LAS VEGAS',
    'CHARLOTTE',
    'DALLAS',
    'BALTIMORE', 
    'LOS ANGELES',
    'MIAMI',
    'NEW ORLEANS',
    'ALBUQUERQUE',
    'PORTLAND',
    'SAN FRANCISCO',
    'TAMPA',
    'NEW YORK',
    'DETROIT',
    'ST LOUIS',
    'CHICAGO'
]

TRAINING_INTERVAL = range(1961, 2011)
TESTING_INTERVAL = range(2011, 2017)

"""
Begin helper code
"""
class Dataset(object):
    """
    The collection of temperature records loaded from given csv file
    """
    def __init__(self, filename):
        """
        Initialize a Dataset instance, which stores the temperature records
        loaded from a given csv file specified by filename.

        Args:
            filename: name of the csv file (str)
        """
        self.rawdata = {}  #dictionary of [dictionary of cities] of [dictionary of years] of [dictonary of months] of [dictionary of days], each day has a temp

        f = open(filename, 'r')
        header = f.readline().strip().split(',')
        for line in f:
            items = line.strip().split(',')     

            date = re.match('(\d\d\d\d)(\d\d)(\d\d)', items[header.index('DATE')])
            year = int(date.group(1))
            month = int(date.group(2))
            day = int(date.group(3))

            city = items[header.index('CITY')]
            temperature = float(items[header.index('TEMP')])
            if city not in self.rawdata:
                self.rawdata[city] = {}
            if year not in self.rawdata[city]:
                self.rawdata[city][year] = {}
            if month not in self.rawdata[city][year]:
                self.rawdata[city][year][month] = {}
            self.rawdata[city][year][month][day] = temperature
            
        f.close()

    def get_yearly_temp(self, city, year):
        """
        Get the daily temperatures for the given year and city.

        Args:
            city: city name (str)
            year: the year to get the data for (int)

        Returns:
            a 1-d numpy array of daily temperatures for the specified year and
            city
        """
        temperatures = []
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year is not available"
        for month in range(1, 13):
            for day in range(1, 32):
                if day in self.rawdata[city][year][month]:
                    temperatures.append(self.rawdata[city][year][month][day])
        return np.array(temperatures)

    def get_daily_temp(self, city, month, day, year):
        """
        Get the daily temperature for the given city and time (year + date).

        Args:
            city: city name (str)
            month: the month to get the data for (int, where January = 1,
                December = 12)
            day: the day to get the data for (int, where 1st day of month = 1)
            year: the year to get the data for (int)

        Returns:
            a float of the daily temperature for the specified time (year +
            date) and city
        """
        assert city in self.rawdata, "provided city is not available"
        assert year in self.rawdata[city], "provided year {} is not available".format(year)
        assert month in self.rawdata[city][year], "provided month is not available"
        assert day in self.rawdata[city][year][month], "provided day is not available"
        return self.rawdata[city][year][month][day]

def se_over_slope(x, y, estimated, model):
    """
    For a linear regression model, calculate the ratio of the standard error of
    this fitted curve's slope to the slope. The larger the absolute value of
    this ratio is, the more likely we have the upward/downward trend in this
    fitted curve by chance.
    
    Args:
        x: a 1-d numpy array with length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d numpy array of values estimated by a linear
            regression model
        model: a numpy array storing the coefficients of a linear regression
            model

    Returns:
        a float for the ratio of standard error of slope to slope
    """
    assert len(y) == len(estimated)
    assert len(x) == len(estimated)
    EE = ((estimated - y)**2).sum()
    var_x = ((x - x.mean())**2).sum()
    SE = np.sqrt(EE/(len(x)-2)/var_x)
    return SE/model[0]

"""
End helper code
"""

def linear_regression(x, y):
    """
    Generate a linear regression models by fitting a to a set of points (x, y).

    Args:
        x: a list of length N, representing the x-coordinates of
            the N sample points
        y: a list of length N, representing the y-coordinates of
            the N sample points

    Returns:
        (m, b): A tuple containing the slope and y-intercept of the regression line,
                which are both floats.
    """
    #get avg of all the x and y vals
    xAvg = sum(x)/len(x)
    yAvg = sum(y)/len(y)
    
    #get the sums of all the products of differences between x,y vals and x,y avg
    #get sum of diff between x vals and xAvg, squared
    sumOfDiff = 0
    sumOfXDiff = 0
    for i in range(len(x)):
        sumOfDiff += (x[i] - xAvg) * (y[i] - yAvg)
        sumOfXDiff += (x[i] - xAvg)**2
              
    m = sumOfDiff/sumOfXDiff
    
    b = yAvg - (m * xAvg)
    
    return (m, b)

def evaluate_squared_error(x, y, m, b): 
    '''
    Calculate the squared error for all points in a given regression.

    Args:
        x: a list of length N, representing the x-coordinates of
            the N sample points
        y: a list of length N, representing the y-coordinates of
            the N sample points
        m: The slope of the regression line 
        b: The y-intercept of the regression line


    Returns:
        the total squared error of our regression 
    '''
    totalError = 0
    
    for i in range(len(x)):
        totalError += (y[i] - (m * x[i] + b))**2
        
    return totalError

def generate_models(x, y, degs):
    """
    Generate regression models by fitting a polynomial for each degree in degs
    to points (x, y).

    Args:
        x: a 1-d numpy array of length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array of length N, representing the y-coordinates of
            the N sample points
        degs: a list of integers that correspond to the degree of each polynomial 
            model that will be fit to the data

    Returns:
        a list of numpy arrays, where each array is a 1-d array of coefficients
        that minimizes the squared error of the fitting polynomial
    """
    arrays = []
    #adds each array of coefficients for each degree to list
    for deg in degs:
        arrays.append(np.polyfit(x, y, deg))
        
    return arrays

def evaluate_models_on_training(x, y, models):
    """
    For each regression model, compute the R-squared value for this model and the
    standard error over slope of a linear regression line (only if the model is
    linear), and plot the data along with the best fit curve.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        R-square of your model evaluated on the given data points,
        and SE/slope (if degree of this model is 1 -- see se_over_slope). 

    Args:
        x: a 1-d numpy array with length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        predictedY = np.polyval(model, x)   #gets predicted y values
        rSq = round(r2_score(y, predictedY), 3)
        title = "Regression degree: " + str(len(model)-1) + "; R-sq: " + str(rSq)
        if len(model) == 2:     #linear models will only have 2 coefficients
            se = round(se_over_slope(x, y, predictedY, model), 3)
            title += ("; SE/slope: " + str(se))
        plt.plot(x, y, color = "b", marker = '.', linestyle = '')
        plt.plot(x, predictedY, color = 'r', linestyle = '-')
        plt.title(title)
        plt.xlabel("Year")
        plt.ylabel("Degrees Celsius")
        plt.show()


def gen_cities_avg(temp, multi_cities, years):
    """
    Compute the average annual temperature over multiple cities.

    Args:
        temp: instance of Dataset
        multi_cities: the names of cities we want to average over (list of str)
        years: the range of years of the yearly averaged temperature (list of
            int)

    Returns:
        a numpy 1-d array of floats with length = len(years). Each element in
        this array corresponds to the average annual temperature over the given
        cities for a given year.
    """
    averageTemps = []
    for year in years:
        yearlyTemp = 0
        for city in multi_cities:
            #add the average yearly temp for that city to yearlytemps for all cities
            yearlyTemp += np.average(temp.get_yearly_temp(city, year))
        #adds average temps of all cities for that year to list
        averageTemps.append(yearlyTemp/float(len(multi_cities)))
        
    return np.asarray(averageTemps)   

def find_interval(x, y, length, has_positive_slope):
    """
    Args:
        x: a 1-d numpy array with length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        length: the length of the interval
        has_positive_slope: a boolean whose value specifies whether to look for
            an interval with the most extreme positive slope (True) or the most
            extreme negative slope (False)

    Returns:
        a tuple of the form (i, j) such that the application of linear (deg=1)
        regression to the data in x[i:j], y[i:j] produces the most extreme
        slope and j-i = length.

        In the case of a tie, it returns the most recent interval. For example,
        if the intervals (2,5) and (8,11) both have the same slope, (8,11) should
        be returned.

        If such an interval does not exist, returns None
    """
    slope = 0
    i = 0
    j = 0
    #go through every int from x to the length of the array - the length, inclusive (subtract length to avoid going out of range)
    for p in range(len(x)-length + 1):
        #consider new slope for regression of points within length of interval
        newSlope = linear_regression(list(x[p:p+length]), list(y[p:p+length]))[0]
        
        #if positive slope and new slope is more positive than old slope or if negative slope and new slope is negative than old slope, 
        #or if new slope is equal to old slope,
        #set i and j to endpoints of interval and slope as the new slope
        if (has_positive_slope and newSlope > slope + 10**(-8)) or (not has_positive_slope and newSlope < slope - 10**(-8))\
            or (abs(newSlope - slope) <= 10**-8):
            i = p
            j = p+length
            slope = newSlope
    
    #if unable to find an interval with the most extreme slope, return none
    if slope == 0:
        return None
    return (i, j)
            

def rmse(y, estimated):
    """
    Calculate the root mean square error term.

    Args:
        y: a 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        estimated: an 1-d numpy array of values estimated by the regression
            model

    Returns:
        a float for the root mean square error term
    """
    totalDiffSq = 0
    #finds diff sq for each actual y coordinate and predicted y coordinate
    for i in range(len(y)):
        totalDiffSq += (y[i] - estimated[i])**2
        
    error = (totalDiffSq/float(len(y)))**(1/2)
    return error


def evaluate_models_on_testing(x, y, models):
    """
    For each regression model, compute the RMSE for this model and plot the
    test data along with the model's estimation.

    For the plots, you should plot data points (x,y) as blue dots and your best
    fit curve (aka model) as a red solid line. You should also label the axes
    of this figure appropriately and have a title reporting the following
    information:
        degree of your regression model,
        RMSE of your model evaluated on the given data points. 

    Args:
        x: a 1-d numpy array with length N, representing the x-coordinates of
            the N sample points
        y: a 1-d numpy array with length N, representing the y-coordinates of
            the N sample points
        models: a list containing the regression models you want to apply to
            your data. Each model is a numpy array storing the coefficients of
            a polynomial.

    Returns:
        None
    """
    for model in models:
        predictedY = np.polyval(model, x)   #gets predicted y values
        rmseVal = rmse(y, predictedY)
        title = "Regression degree: " + str(len(model)-1) + "; RMSE: " + str(rmseVal)

        plt.plot(x, y, color = "b", marker = '.', linestyle = '')
        plt.plot(x, predictedY, color = 'r', linestyle = '-')
        plt.title(title)
        plt.xlabel("Year")
        plt.ylabel("Degrees Celsius")
        plt.show()



if __name__ == '__main__':
    
    pass

    # Problem 4A
    allData = Dataset("data.csv")
    xVals = list(range(1961,2017))
    yVals = []
    for year in xVals:
        yVals.append(allData.get_daily_temp("BOSTON", 2, 12, year))
    models = generate_models(xVals, yVals, [1])
    evaluate_models_on_training(np.asarray(xVals), np.asarray(yVals), models)
    

    # Problem 4B
    yVals = (gen_cities_avg(allData, ["BOSTON"], xVals))
    models = generate_models(xVals, yVals, [1])
    evaluate_models_on_training(np.asarray(xVals), yVals, models)

    # Problem 5B
    #positive slope
    yVals = gen_cities_avg(allData, ["LOS ANGELES"], xVals)
    interval = find_interval(xVals, yVals, 30, has_positive_slope = True)
    #generate the model only on the x and y values in the interval
    x = xVals[interval[0]:interval[1]]
    y = yVals[interval[0]:interval[1]]
    models = generate_models(x, y, [1])
    evaluate_models_on_training(np.asarray(x), y, models)
    
    #negative slope
    interval = find_interval(xVals, yVals, 30, has_positive_slope = False)
    #generate the model only on the x and y values in the interval
    x = xVals[interval[0]:interval[1]]
    y = yVals[interval[0]:interval[1]]
    models = generate_models(x, y, [1])
    evaluate_models_on_training(np.asarray(x), y, models)

    # Problem 6B
    #training data
    trainingData = Dataset("data.csv")
    xVals = list(TRAINING_INTERVAL)
    yVals = gen_cities_avg(trainingData, CITIES, xVals)
    models = generate_models(xVals, yVals, [2, 15])
    evaluate_models_on_training(xVals, yVals, models)
    
    #testing data
    testingData = Dataset("data.csv")
    xVals = list(TESTING_INTERVAL)
    yVals = gen_cities_avg(testingData, CITIES, xVals)
    evaluate_models_on_testing(xVals, yVals, models)

