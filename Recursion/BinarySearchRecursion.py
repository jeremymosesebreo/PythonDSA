def binary_search(data, target, low, high):
    '''Return True if the target is found in indicated portion of a Python list.'''
    '''The search only considers the portion from data[low] to data[high] inclusive.'''
    if low > high:
        return False #interval is empty
    else:
        mid = (low + high) // 2
        if target == data[mid]: #the (base case) condition if we found the match
            return True
        elif target < data[mid]:
            #recur on the portion left of the middle
            return binary_search(data, target, low, mid - 1)
        else:
            #recur on the portion right of the middle element
            return binary_search(data, target, mid + 1, high)

