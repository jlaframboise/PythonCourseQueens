'''
This program draws a picture using the Turtle Graphics module in Python.

Author: Jacob Laframboise
Date: Sept. 24th, 2018
Student Number: --------
'''

import turtle

'''
Draws a square beginning at the upper left corner of the square denoted by startPos.  
startPos is a tuple containing 2 values (x, y) indicating the start position.
The size of the square is denoted by the parameter size (in pixels).
Colour is a string containing a hexidecimal number representing the color.
A hexidecimal number looks something like #FF0000.  So, to represent red, the string
"#FF0000" would be passed as the colour.
Use https://www.webfx.com/web-design/color-picker/ to find colour representations.
'''
def drawSquare(theTurtle, startPos, size, colour):

    #move the turtle to startPos position
    theTurtle.penup()
    theTurtle.setposition(startPos)
    theTurtle.pendown()

    #set the direction of the turtle
    theTurtle.setheading(90)

    #set pen colour
    theTurtle.pencolor(colour)

    #draw the squre
    for i in range(4):
        theTurtle.forward(size)
        theTurtle.right(90)


'''
Draws a rectangle beginning at the upper left corner of the rectangle denoted by startPos.  
startPos is a tuple containing 2 values (x, y) indicating the start position.
The width of the rect is the width parameter in pixels, height is height.
Colour is a string containing a hexidecimal number representing the color.
'''
def drawRect(theTurtle, startPos, width, height, colour):

    #move the turtle to startPos position
    theTurtle.penup()
    theTurtle.setposition(startPos)
    theTurtle.pendown()

    #set the direction of the turtle
    theTurtle.setheading(90)

    #set pen colour
    theTurtle.pencolor(colour)

    # start fill
    theTurtle.begin_fill()
    theTurtle.fillcolor(colour)
    
    # draw the rectangle
    for i in range(4):
        if i%2==1: # altenate width and height lengths
            theTurtle.forward(width)
        else:
            theTurtle.forward(height)
        theTurtle.right(90)
    # stop filling
    theTurtle.end_fill()


'''
Draws a 5 point star starting at startx, starty which is the top-most point of the star.
startPos is a tuple containing 2 values (x, y) indicating the start position.
Size is the length of the line from one point to the next. 
Colour is a string containing a hexidecimal number representing the color.  
Use https://www.webfx.com/web-design/color-picker/ to find colours.
'''
def drawStar(theTurtle, startPos,  size, colour):

    # move the turtle to (startx, starty) position
    theTurtle.penup()
    theTurtle.setposition(startPos)
    theTurtle.pendown()

    #set the direction of the turtle
    theTurtle.setheading(90)

    # set pen colour
    theTurtle.pencolor(colour)

    #draw the star
    for i in range(5):
        theTurtle.forward(size)
        theTurtle.right(144)

'''A function to draw an equilateral triangle on the screen. It takes the turtle which will draw it,
the start position startPos, which is a tuple containing the x,y coords of the bottom left corner.
It takes the side length as a measure of size in pixels, and a hex value for the colour of the triangle.
The triangle drawn is a filled triangle. '''
def drawTriangle(theTurtle, startPos, sideLength, colour):
    
    #move the turtle to startPos position
    theTurtle.penup()
    theTurtle.setposition(startPos)
    theTurtle.pendown()

    #set the direction of the turtle
    theTurtle.setheading(0)

    #set pen and fill colours
    theTurtle.pencolor(colour)
    theTurtle.begin_fill()
    theTurtle.fillcolor(colour)

    #Draw the triangle
    for x in range(3):
        theTurtle.forward(sideLength)
        theTurtle.right(360/3)
        
    theTurtle.end_fill()
        
'''A function to draw a tree of predefined qualities on a screen with a variable width and height.
Takes the turtle object, the width of the screen, and the height of the screen. '''
def drawTree(myTurtle, screenWidth, screenHeight):
    
    # draw the tree trunk
    drawRect(myTurtle, (screenWidth/2 - 30, screenHeight-200), 60, 200, '#663300')
    
    # change colour and draw the trees
    myTurtle.begin_fill()
    myTurtle.fillcolor('#009933')
    
    for x in range(4): # loop draws four tree sections
        triSize = 60*(4-x) #make the tree sections progressively smaller
        triBase = 150
        # draw the triangles at a fixed width to the base of the tree, height scales with counter var
        drawTriangle(myTurtle, (screenWidth/2-triSize/2, screenHeight-250/3*x - triBase), triSize, '#009933')
        
    # Adjust fill colour and draw the star
    myTurtle.begin_fill()
    myTurtle.fillcolor('#33cccc')
    drawStar(myTurtle, (screenWidth/2, screenHeight-250-triBase-triSize+20), 30, '#33cccc')
    
    myTurtle.end_fill()

'''A function containing a loop that draws a simple wall out of squares to border the background of
my drawing. parameters are the turtle object, the screen width in pixels, and the screen height in pixels. '''
def drawWall(myTurtle, screenWidth, screenHeight):
    
    # a loop to draw many squares, with the horizontal position related to the counter
    for x in range(20):
        drawSquare(myTurtle, (screenWidth/20*x, screenHeight/2-10), 20, '#993300')


'''
The main function starts the program execution.  The drawing area size is set. 
The coordinate system is set so that (0, 0) is in the top left corner of the drawing window.
x increases going to the right, y increases as you move down the screen.  The bottom right corner is 
position (width, height).
A turtle is created (called bob) and is used for drawing.
The background is drawn, the wall is added
The tree is drawn.
The program pauses before exit. 
'''
def main():

    #initializes the screen size and the coordinate system.
    width = 600
    height = 600
    turtle.setup(width, height)
    wn = turtle.Screen()
    wn.setworldcoordinates(0, width, height, 0)

    #creates the turtle with which you will draw.  This turtle should be passed to all functions.
    bob = turtle.Turtle()
    bob.speed = 0

    #draw the background
    drawRect(bob, (0,height/2), width, height/2, '#99cc00')
    drawRect(bob, (0,0), width, height/2, '#00ccff')

    # draw the wall on the background
    drawWall(bob, width, height)

    #draw the tree
    drawTree(bob, width, height)

    #the following stops the window from closing so that you can admire the drawing
    wn.exitonclick()



main()
