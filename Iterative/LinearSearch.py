def linear_search(data, target):
    '''Return True if target is found in data, False otherwise.'''
    for item in data:
        if item == target:
            return True
    return False
'''the linear search algorithm does not 
require a sorted list, unlike the binary search algorithm'''