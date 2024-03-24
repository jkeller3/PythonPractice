# Classes and Instance

class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Joseph', 'Keller', 60000)
emp_2 = Employee('New', 'Guy', 5000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())