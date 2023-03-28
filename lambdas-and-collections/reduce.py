# Code to calculate sum of elements in a list

from functools import reduce

list_input = list(range(1, 5))
the_sum = reduce(lambda acc, i: acc + i, list_input)
# accumulator initial value is not declared.
# Hence, taking the first value in the list
print(the_sum)
