def fact(n):
    '''
    >>> fact(1)
      1
    >>> fact(3)
      6
      >>> fact(10)
      3628800
      >>> fact(0)
      Traceback (most recent call last):
      ...
      ValueError
      >>> fact(99999999)
      Traceback (most recent call last):
      ...
      RecursionError: maximum recursion depth exceeded in comparison
      >>> fact(-1)
      Traceback (most recent call last):
      ...
      ValueError
      '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)



fact(1)

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()