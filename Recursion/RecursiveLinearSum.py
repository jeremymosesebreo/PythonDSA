def linear_sum(S, n):
    '''Return the sum of the first n elements of sequence S.'''
    if n == 0:
        return 0
    else:
        return S[n - 1] + linear_sum(S, n - 1)

S = [1, 2, 3]
print(linear_sum(S, len(S)))