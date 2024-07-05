def binary_search_iterative(data, target):
    '''Return True if target is found in data, False otherwise.'''
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:#if we found a match
            return True
        elif target < data[mid]:#only considers values left of mid
            high = mid - 1
        else:
            low = mid + 1#only considers values right of mid
    return False #loop ends without successful match