# and, or, not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Admin Page')
elif not logged_in:
	print('Please log in')
elif user != 'Admin':
	print('Admin only')
else:
	print('Bad Credentials')

a = [1,2,3]
b = [1,2,3]

print(a==b)
print(a is b)
print(id(a))
print(id(b))

b = a 
print(a==b)
print(a is b)
print(id(a))
print(id(b))


# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

condition = False 

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')