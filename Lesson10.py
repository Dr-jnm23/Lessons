# adding to list

# create list
A = [5, 12, 72, 55, 89]

#try and re-assign, this will fail
#A = A + 1

# correct method
A = A + [1]

# add string
A = A + ['BCD']

# add string as list this does all three letters
A = A + list('BCD')

# add elements

# append - causes nullify if you try and assign
A = A.append(10)

# if null, type is 'non-type'

# correct method is insert

# first index
A.insert(0, 222)

# first index, insert list
A.insert(0, [1, 2, 3])

# cannot do this with string

#  remove
A.remove(0)

#tuple
# tuples use parentheses and are immutable

#immutable
our_tuple = (1, 2, 3, 'A', 'B', 'C')

#mutable
our_list = [1, 2, 3, 'A', 'B', 'C']

# dictionaries

students = {'Alice':25, 'Bob':27, 'Claire':17, 'Dan':21 , 'Emma':22}

# can get age (key) by typing the name
students['Emma']

# update age
students['Alice'] = 26

# try and delete, fail
del students[Fred]

# get keys, note this is not a list
students.keys()

# convert to a list
#a = list(students.keys())
a[0]

# get all values (ages)
students.values()

# get all items
students.items()

# dictionaries don't have an order