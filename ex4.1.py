# Jacob Laframboise
# --------
# Oct. 12th, 2018
# A program to convert temperature scales, with a bug fixed

'''
Python Course Exercise 4
'''

'''
Program 1
'''

'''
Degrees Celsius to degrees Fahrenheit converter.
The parameter is an int or float representing some number of degrees Celsius.
The return value (a float) is the degrees Fahrenheit conversion of that number.
'''
def celsius_to_fahrenheit(degrees_celsius):
	return degrees_celsius * 9 / 5 + 32

'''
Degrees Fahrenheit to degrees Celsius converter.
The parameter is an int or float representing some number of degrees Fahrenheit.
The return value (a float) is the degrees Celsius conversion of that number.
'''
def fahrenheit_to_celsius(degrees_fahrenheit):
	return (degrees_fahrenheit - 32) / 9 * 5 # I added brackets to fix order of operation error

'''Print a Celsius-to-Fahrenheit table.'''
for i in range(0, 101):
	print (str(i) + '° Celsius is ' + str(celsius_to_fahrenheit(i)) + '° Fahrenheit')

'''Print a Fahrenheit-to-Celsius table.'''
for i in range(32, 213):
	print (str(i) + '° Fahrenheit is ' + str(fahrenheit_to_celsius(i)) + '° Celsius')
