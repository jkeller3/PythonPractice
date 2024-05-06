# LEGB
# Local, Enclosing, Global, Built-in

import builtins

# print(dir(builtins))

def my_min():
	pass

m = min([5, 1, 4, 2, 3])
print(m)

x = 'global x'


def test(z):
	# y = 'local y'
	x = 'local x'
	# print(y)
	print(z)

test('local z')
# print(y) fails due to not being in scope
# print(z)

def outer():
	x = 'outer x'

	def inner():
		# nonlocal x
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()
print(x)