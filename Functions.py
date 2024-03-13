
# def hello_func():
# 	return 'Hello Function!'

def hello_func(greeting, name = 'You'):
	return '{}, {}.'.format(greeting, name)

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

name = 'Joey'

for i in range(0,4):
	print(hello_func('Hi',name))

print(hello_func('HEY').upper())

student_info()

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)


