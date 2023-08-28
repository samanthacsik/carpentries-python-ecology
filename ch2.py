# A Python Script File 
# Following exercises in Ch 2.

# assign some variables 
text = "Data Carpentries" # string
number = 42 # numeric/integer
pi_value = 3.1415 # float

# print text
print(text)

# operators
2 + 2
6 * 7
2 ** 16
13 % 5
3 > 4
True and True
True or False # I don't understand this
True and False # I don't understand this

# lists (ordered sequence of elements. Each element can be accessed by an index)
numbers = [1, 2, 3]
numbers[0]

# for loops
for num in numbers:
    print(num)

# append elements to a list
numbers.append(4)

# find what methods are available for 
help(numbers)

# tuples (A tuple is similar to a list in that it’s an ordered sequence of elements. However, tuples can not be changed once created (they are “immutable”))
a_tuple = (1, 2, 3)
another_tuple = ('blue', 'red', 'green')

a_list = [1, 2, 3]

# dictionary (work like lists but you index them with keys)
translation = {'one': 'first', 'two': 'second'}
translation['one']

rev = {'first': 'one', 'second': 'two'}
rev['second']

# add an item to an existing dictionary
rev['third'] = 'three'
rev

# using for loops with dictionaries
for key, value in rev.items():
    print(key, '->', value)

# changing dictionaries (practice)

# 1. printe value of the `rev` dictionary to the screen
print(rev)

# 2. reassign the value that corresponds to the key `second` so that it no longer reads "two" but unstead `2`
rev['second'] = 2

# 3. print the value of `rev` to the screen again to see if the value has changed
print(rev)

# functions
def add_function(a, b): 
    result = a + b
    return result

z = add_function(20, 22)
print(z)