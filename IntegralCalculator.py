
import numpy as np
import matplotlib.pyplot as plt





def string2func(string):
    ''' evaluates the string and returns a function of x
    find all words and check if all are allowed: '''
        
    replacements = {
    'sin' : 'np.sin',
    'cos' : 'np.cos',
    'exp': 'np.exp',
    'sqrt': 'np.sqrt',
    '^': '**',
    'log': 'np.log',
    'e' : '2.718281828459045',
    'pi' : '355/133',
    'tan': 'np.tan',
    'math.' : ''
    
    
}

    
        
    #Goes through the inputted formula and replaces the string text with numpy functions 

    for old, new in replacements.items():
        string = string.replace(old, new)

    return string

def increment(boundaries, trapezoids):
    ''''Takes in the boundaries for integration and the number of trapezoids wanted and calculates
    the increment base (or increment) of each trapezoid'''
    increments = (float(boundaries[-1]) - float(boundaries[0])) / trapezoids
    return increments
    
    
def x_vals(boundaries, increments, trapezoids):
    ''''takes in the number of increments and boundaries and calculates all the left x-values for the 
    trapezoids '''
    
    x_vals = []

    
    for i in range(0, trapezoids + 1):
    
        x_val = int(boundaries[0]) + i * increments
        
        x_vals.append(x_val)
        #i += 1
    return x_vals

def left_vals(x_vals, formula):
    ''''Using the x_vals from the x_vals fucntion, it'll calculate the value of the function at that
    which we wil use later to calculate the total area under the curve'''
    y_vals = []
    
    for x in x_vals:
        y = eval(formula)
        y_vals.append(y)
        
    return y_vals
    
def area(left_vals, increment):
    ''''Takes in the left_vals and increments and calculates the total area under the curve'''
    
    areas = []
    #The function will calculate the area under each trapezoid and apend them to a list. At the very it'll return the sum
    #of all the areas
    for i in range(len(left_vals) - 1): 
        area = (left_vals[i] * increment) + ((left_vals[i + 1] - left_vals[i]) * increment/ 2)
        areas.append(area)
        
    return sum(areas)

def plot(formula, boundaries, areas, x_val, left_val):
    ''''takes in everything that we've done so far and plots the formula, the estimated line, 
    and the area underneath the estimated line'''
    func = string2func(formula)
    a = float(boundaries[0])
    b = float(boundaries[1])
    x = np.linspace(a, b, 250)
    
    
    func = eval(func)
    plt.plot(x, func, 'r-.')
    plt.xlim(a, b)
    plt.plot(x_val, left_val, 'bs')
    plt.fill_between(x_val, left_val, color='red',
                 alpha=0.5)
    plt.ylabel('y-axis')
    plt.xlabel('x-axis')
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.text(x_val[0], max(left_val), 'The Area is: {}'.format(areas), fontsize = 10, bbox = props)

    plt.title('Plot of {} and estimated area'.format(formula))
    plt.grid()
 



def main(): 
    ''''This is just the main function where everything takes place '''
    #Main three arguments 
    formula = input('Input an equation: ')

    boundaries = tuple((input('Enter the limits for integration with a space in between them(NOTE: make sure the function is continuos in that interval): ').split()))

    trapezoids = int(input('How many trapezoids do you want? '))
    
    #all the math and other function acalls
    increments = increment(boundaries, trapezoids)
    
    wformula = string2func(formula)
    print(wformula)
    x_val = x_vals(boundaries, increments, trapezoids)
   
    
    left_val = left_vals(x_val, wformula)
    
    areas = area(left_val, increments)
    
    #final return values 
    print('TThe resulting summation of the trapezoid areas is', areas)
    plot(formula, boundaries, areas, x_val, left_val)
    


