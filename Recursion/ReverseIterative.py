def reverse_iterative(S):
    '''Reverse elements in sequence S.'''
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start, stop = start + 1, stop - 1

S = [1, 2, 3, 4, 5]
reverse_iterative(S)
print(S)