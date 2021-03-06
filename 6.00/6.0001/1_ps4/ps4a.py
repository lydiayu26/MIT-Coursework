 # Problem Set 4A
# Name: Lydia Yu
# Collaborators:
# Time Spent: 2:00
# Late Days Used: 0

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the tests named data_representation should pass.
tree1 = [[4,10],5]
tree2 = [[15,4],[[1,2],10]]
tree3 = [[12],[14,6,2],[19]]


# Part A1: Multiplication on tree leaves

def mul_tree(tree):
    """
    Recursively computes the product of all tree leaves.
    Returns an integer representing the product.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
    Outputs
       total: An int equal to the product of all leaves of the tree.

    """
    #if the tree is just an int, return the value of that int
    #if the tree is an empty array, return 1 which multiplies the total by 1
    if type(tree) == int:
        return tree
    if tree == []:
        return 1
    #total is the product of the first element of the array and the mul_tree function of the rest of the array
    total = mul_tree(tree[0]) * mul_tree(tree[1:])
    
    return total


# Part A2: Arbitrary operations on tree leaves

def sumem(a,b):
    """
    Example operator function.
    Takes in two integers, returns their sum.
    """
    return a + b

def prod(a,b):
    """
    Example operator function.
    Takes in two integers, returns their product.
    """
    return a * b

def op_tree(tree, op, base_case):
    """
    Recursively runs a given operation on tree leaves.
    Return type depends on the specific operation.

    Inputs
       tree: A list (potentially containing sublists) that
       represents a tree structure.
       op: A function that takes in two inputs and returns the
       result of a specific operation on them.
       base_case: What the operation should return as a result
       in the base case (i.e. when the tree is empty).
    """
    if type(tree) == int:
        return tree
    if tree == []:
        return base_case
    
    #runs op on the first element of tree and the rest of the tree    
    total = op(op_tree(tree[0], op, base_case), op_tree(tree[1:], op, base_case))
    return total

# Part A3: Searching a tree

def search_even(a, b):
    """
    Operator function that searches for even values within its inputs.

    Inputs
        a, b: integers or booleans
    Outputs
        True if either input is equal to True or even, and False otherwise
    """
    if type(a) == int and type(b) == int:
        if a%2 == 0 or b%2 == 0:
            return True
    elif type(a) == bool and type(b) == bool:
        if a == True or b == True:
            return True
    elif (type(a) == bool and type(b) == int):
        if(b%2 == 0) or (a == True):
            return True
    elif (type(a) == int and type(b) == bool):
        if(a%2 == 0) or (b == True):
            return True
    return False
    
        
if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # Do not erase the pass statement below.
    pass
