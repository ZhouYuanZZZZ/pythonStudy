# Here is a small example using a dictionary:
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 412777

print(tel)
print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print('--------------------1----------------------------')
print('\n')

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict1)
print('--------------------2----------------------------')
print('\n')

# When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
for k, v in dict1.items():
    print(k+':'+str(v))
print('--------------------3----------------------------')
print('\n')

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})

print(a == b == c == d == e)
print('--------------------4----------------------------')
print('\n')

dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

# iteration
n = 0
for val in values:
    n += val
print(n)


# keys and values are iterated over in the same order
list(keys)

list(values)


# view objects are dynamic and reflect dict changes
del dishes['eggs']
del dishes['sausage']
list(keys)


# set operations
keys & {'eggs', 'bacon', 'salad'}

keys ^ {'sausage', 'juice'}

print('--------------------5----------------------------')
print('\n')