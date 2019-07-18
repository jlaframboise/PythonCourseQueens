# Jacob Laframboise
# --------
# Oct. 17th, 2018
# A program to draw and graph functions on a canvas using tkinter



from tkinter import *
from math import *

CANV_WIDTH = 750
CANV_HEIGHT = 250


def draw_axes(scale, tick_length):
    """Draws a horizontal line across the middle of the canvas, and a vertical
    line down the centre of the canvas using tkinter's default line thickness
    and colour.
    Also draws tick marks for axis scales on each axis.
    """

    # Draw the x axis
    width = w.winfo_width()
    w.create_line(get_x(-width // 2), get_y(0), get_x(width // 2), get_y(0))
    # Draw the y axis
    height = w.winfo_height()
    w.create_line(get_x(0), get_y(-height // 2), get_x(0), get_y(height // 2))

    #draw ticks on y axis
    for tick in range(int(round(height/scale, 0))):
        w.create_line(get_x(0), get_y(scale*tick), get_x(-tick_length), get_y(scale*tick))
        w.create_line(get_x(0), get_y(-scale*tick), get_x(-tick_length), get_y(-scale*tick))
    # draw ticks on x axis
    for tick in range(int(round(width / scale, 0))):
        w.create_line(get_x(scale*tick), get_y(0), get_x(scale*tick), get_y(-tick_length))
        w.create_line(get_x(-scale*tick), get_y(0), get_x(-scale*tick), get_y(-tick_length))



def get_x(x_val):
    """Maps a Cartesian-style x coordinate (where x is 0 at the window's
    horizontal centre) onto the tkinter canvas (where x is 0 is at the left
    edge). x_val is the Cartesian x coordinate. The units of measurerment
    are pixels.
    """
    '''Takes coords relative to the center, and returns coords realtive to the 
    upper left corner as per tk default.'''
    tkCoord = x_val + w.winfo_width()/2
    return  tkCoord


def get_y(y_val):
    """Maps a Cartesian-style y coordinate (where y is 0 at the window's
    vertical centre, and in which y grows in value upwards) onto the tkinter
    canvas (where y is 0 is at the top edge, and y grows in value downwards).
    y_val is the Cartesian y coordinate. The returned value is the
    corresponding tkinter canvas x coordinate. The units of measurerment are
    pixels.
    """
    tkCoord = -y_val + w.winfo_height()/2
    return tkCoord


def plot_point(x, y, p_size, colour='black'):
    """Draws a single pixel "dot" at Cartesian coordinates (x,y).
    The optional colour parameter determines the colour of the dot.
    """
    w.create_oval(get_x(x), get_y(y), get_x(x+p_size),
                  get_y(y+p_size), fill=colour, width=0)



def plot_fn(fn, start_x, end_x, scale=20, colour='black'):
    """Plots a function, y = fn(x), onto the canvas.

    Parameters:

    * fn is a function that takes a single number parameter and returns a
      number.

    * start_x is the left-most x value to be passed to fn.

    * end_x is the right-most x value to be passed to fn.

    * scale (optional) is used as a multiplier in both the x and y directions
      to "zoom in" on the plot. It is also used to increase the number of x
      coordinates "fed" to the fn function, to fill in all the horizontal gaps
      that would otherwise appear between the plotted points. scale is
      particularly useful for showing detail that would be otherwise be lost.

    * colour (optional) determines the colour of the plotted function.

    Note: nothing bad happens if start_x, end_x, or any y value computed from
    fn(x) is off the canvas. Those points simply will not be displayed.
    (Note to the student programmer: This happens automatically. You don't
    have to program it.)
    """
    try:
        # for every pixel on the screen:
        for xCoord in range(-w.winfo_width()//2, w.winfo_width()//2+1):
            # get the value which should be inputted to the function
            xVal = xCoord/scale
            # get the value of the function at that point
            yVal = fn(xVal)
            # find how high on the screen the value correlates to
            yCoord = yVal*scale

            # only plot if it is within the boundaries set
            if xVal>=start_x and xVal<=end_x:
                plot_point(xCoord/1, yCoord/1, 2, colour)
    except:
        print('Sorry, something went wrong with this function!')


def square(x):
    """Returns the square of x"""
    return x * x


def func_1(x):
    """A quadratic polynomial function (for testing)."""
    return -3 * square(x) + 2 * x + 1


def func_2(x):
    """An absolute value sin function"""
    return abs(sin(x))+1


def func_3(x):
    """An absolute value cosine function, when used with func_2,
    it stacks on top neatly. """
    return abs(cos(x))+2  # replace this line


master = Tk()
master.title('Plot THIS!')
w = Canvas(master,
           width=CANV_WIDTH,
           height=CANV_HEIGHT)
w.pack(expand=YES, fill=BOTH)
w.update()  # makes w.winfo_width() and w.winfo_height() meaningful


def main():
    '''A main function to operate all of the defined functions in this program.
    Will draw out a number of functions on a grid that is also drawn. '''
    # initialize some variables for repeated values
    scale = 40
    tickLength = 4
    # draw the grid
    draw_axes(scale, tickLength)
    # pot all the functions
    plot_fn(sin, -20, 20, scale, 'green')  # sin() is defined in the math module
    plot_fn(cos, -20, 20, scale, 'blue')  # cos() is defined in the math module
    plot_fn(square, -20, 20, scale, 'red')
    plot_fn(func_1, -20, 20, scale, 'purple')
    plot_fn(func_2,-20,20,40,'brown')
    plot_fn(func_3,-20,20,40,'cyan')

# run the main then boot the gui run loop
main()

mainloop()
