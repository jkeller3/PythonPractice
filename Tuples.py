# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()


# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Both output the same because list_2 was simply pointing at list_1 the entire time

# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Tuples can not be modified the way lists can
# Better to use lists when wanting to alter data

