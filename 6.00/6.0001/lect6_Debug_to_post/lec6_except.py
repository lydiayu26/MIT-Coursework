######################################
# EXAMPLE: Raising your own exceptions
######################################
def get_ratios(L1, L2):
    """ Assumes: L1 and L2 are lists of equal length of numbers
        Returns: a list containing L1[i]/L2[i] """
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print("success")
        finally:
            print("executed no matter what!")
    return ratios
    
#print(get_ratios([1, 4], [2, 4]))
#print(get_ratios([1, 4], [2, 0]))


#######################################
## EXAMPLE: Exceptions and lists
#######################################
def get_stats(class_list):
	new_stats = []
	for person in class_list:
		new_stats.append([person[0], person[1], avg(person[1])])
	return new_stats 

test_grades = [[['peter', 'parker'], [10.0, 5.0, 85.0]], 
           [['bruce', 'wayne'], [10.0, 8.0, 74.0]],
           [['captain', 'america'], [8.0,10.0,96.0]],
           [['thor'], []]]

# avg function: version without an exception
#def avg(grades):
#    return (sum(grades))/len(grades)
    
# avg function: version with an exception
#def avg(grades):
#    try:
#        return sum(grades)/len(grades)
#    except ZeroDivisionError:
#        print('warning: no grades data')
#    # alternative choice
##        return 0.0


# avg function: version with assert
#def avg(grades):
#    assert len(grades) != 0, 'warning: no grades data'
#    return sum(grades)/len(grades)


print(get_stats(test_grades))
