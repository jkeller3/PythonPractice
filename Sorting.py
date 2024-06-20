
li = [9,1,8,2,7,3,6,4,5]
# is a list of numbers

s_li = sorted(li, reverse=True)
# creates new list with the variables sorted
# sort defaults to ascending
# reverse=True changes to descending

print('Sorted Variable:\t', s_li)

# li.sort(reverse=True)
# this sorts the list without involving a new variable

print('Original Variable:\t', li)


tup = (9,1,8,2,7,3,6,4,5)

s_tup = sorted(tup)
print('Tuple:\t', s_tup)


di = {'name': 'Corey', 'job': 'programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dictionary:\t', s_di)
# sorts dictionary by keys in alphabetical order


li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key=abs)
print (s_li)


class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __repr__(self):
		return '({},{},${})'.format(self.name, self.age, self.salary)

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
	return emp.age
# this is used as a key to tell the sort to sort by age.

# normally can not sort Classes without a key
s_employees = sorted(employees, key=e_sort)

print(s_employees)