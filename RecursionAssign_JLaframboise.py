# Jacob Laframboise
# Short Assign 6
# Python Course
# Student #: --------
# A set of three functions that use recursion to accomplish small tasks


def square_and_sum(a_list):
    """Squares all the elements of a_list (assumed to contain numbers) and
    returns the sum of those squared elements (or 0 if a_list is empty).
    For example:
        list = [4, 2, 0]
        square_and_sum(list)
    returns 20 and changes list to [16, 4, 0]
    """

    # make a new variable to store the modified list
    # because it cant be reset to a simpler version each
    # new level of recursion.
    global newList
    newList = []

    # If the list is empty
    if len(a_list) == 0:
        return 0
    # recursion:
    elif len(a_list) > 0:
        # get the squared term
        term = a_list[0] ** 2

        # here is the recursive step
        sum = term + square_and_sum(a_list[1:])
        # add to the newList
        newList = newList + [term]
        # set the input list to the newList but reverse bc recursion reverses
        a_list[:] = newList[::-1]
        # return the sum of the squares
        return sum


def compare_lists(list_1, list_2, i=0):
    """Returns False if list_1 and list_2 have different lengths, True if
    list_1 and list_2 are identical, and otherwise returns the index of the
    first mismatched elements between the lists. For example,
        compare_lists([],[1]) returns False (different lengths)
        compare_lists([],[]) returns True (identical lists)
        compare_lists([1],[1]) returns True (identical lists)
        compare_lists([8,2],[8,2]) returns True (identical lists)
        compare_lists([8,2],[8,1]) returns 1 (index of 1st mismatch)
        compare_lists
    """

    # if the lists are different lengths
    if len(list_1) != len(list_2):
        return False
    # base case
    if len(list_1) == 0:
        return True

    if len(list_1) > 0:
        # if the first elements are equal
        if list_1[0] == list_2[0]:
            # run on the lists without the first element, increase i by 1
            # to hold the place.
            return compare_lists(list_1[1:], list_2[1:], i + 1)
        else:
            # if they differ, return the index, i
            return i


def machine_epsilon(try_this=1.0):
    """Returns an approximation of machine epsilon, i.e., the smallest value
    greater than 1.0 that is distinguishable from 1.0 on this system.
    """

    # base case
    if 1.0 + try_this == 1.0:
        return 1.0 + try_this * 2
    # reduce the value
    else:
        return machine_epsilon(try_this / 2)
