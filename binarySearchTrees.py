# siblings, leafs are bottom nodes, nodes, root is top node
# children, parents

# binary tree:
# every node has at most 2 children
# each node is [left, data, right]
# left and right can be none

# cannot have duplicate values in the tree

# everything left of a root node is lesser,
# and everything right of a root node is greater
# where a root node can be a subtree

# Complexity: assuming balance
#   -adding to tree = log(n)
#     -search for value = log(n)

# bin search tree more efficient than binary search list ebcause adding an element is log(n)
# unbalanced tree when you try to convert a list [1,2,3,4,5,6,7] to a tree and they all add to the right side
# balanced if there is an equal number (+-1) depth on each side


def search(tree, value):
    if tree == None:
        return False
    if tree['data']==value:
        return True
    if value<tree['data']:
        return search(tree['left'], value)
    elif tree['data']<value:
        return search(tree['right'], value)

def printTree(tree):
    if tree==None:
        return
    printTree(tree['left'])
    print(tree['data'])
    printTree(tree['right'])

tree1 = {'left':{'left':None, 'data':1, 'right':None}, 'data':2, 'right':{'left':None,'data':6, 'right':None}}
printTree(tree1)
print(search(tree1, 6))