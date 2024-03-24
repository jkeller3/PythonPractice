# Classes and Instances

class Employee:
	
	num_of_employees = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		Employee.num_of_employees += 1
		self.userID = self.num_of_employees

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		pass

emp_1 = Employee('Joseph', 'Keller', 60000)
emp_2 = Employee('New', 'Guy', 50000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.userID)
print(emp_2.userID)
# emp_1.apply_raise()
# emp_2.apply_raise()
# print(emp_1.pay)
# print(emp_2.pay)

print(emp_1.__dict__)
print(Employee.__dict__)