#-----------------------------------------------------------------------------------------------------------------ITERATOR

class CompanyEmployee:
	def __init__(self, position, first_name, last_name, state, phone_number):
		self.position = position
		self.first_name = first_name
		self.last_name = last_name
		self.state = state
		self.phone_number = phone_number

	def __str__(self, type):
		if type.lower() == 'name':#FOR CLEAN OUTPUT
			return "{last}, {first} | {position} | {state} | {phone}".format(last=self.last_name, \
			 first=self.first_name, position=self.position, state=self.state, phone=self.phone_number)
		if type.lower() == 'title':#FOR CLEAN OUTPUT
			return "{position}| {last}, {first} | {state} | {phone}".format(last=self.last_name, \
				first=self.first_name, position=self.position, state=self.state, phone=self.phone_number)
		if type.lower() == 'state':#FOR CLEAN OUTPUT
			return "{state}| {position} | {last}, {first} | {phone}".format(last=self.last_name, \
				first=self.first_name, position=self.position, state=self.state, phone=self.phone_number)

class AbstractIterator():
	def set_first(self):#WILL BE TAKEN CARE OF IN INIT
		pass

	def get_element(self, index):#JUST IN THE EVENT THIS IS EVER NEEDED 
		pass

	def get_current(self):
		pass

	def has_another(self):
		pass

	def next(self):#MOST IMPORTANT
		pass

class EmployeeNameIterator(AbstractIterator):
	def __init__(self, employees):
		import operator
		employees.sort(key = operator.attrgetter('last_name'))
		self.index_of_items = 0
		self.employees = employees

	def set_first(self):#NOT NEEDED, SET TO FIRST DONE IN INIT, HERE FOR COMPLETENESS
		self.index_of_items = 0

	def get_element(self, index):#JUST IN THE EVENT THIS IS EVER NEEDED
		return self.employees[index]

	def get_current(self):
		return self.employees[self.index_of_items]

	def has_another(self):
		if self.index_of_items >= len(self.employees):
			return False
		else:
			return True

	def next(self):
		next_employee = self.employees[self.index_of_items]
		self.index_of_items += 1
		return next_employee

class EmployeePositionIterator(AbstractIterator):
	def __init__(self, employees):
		import operator
		employees.sort(key = operator.attrgetter('position'))
		self.employees = employees
		self.index_of_items = 0

	def set_first(self):#NOT NEEDED, SET TO FIRST DONE IN INIT, HERE FOR COMPLETENESS
		self.index_of_items = 0

	def get_element(self, index):#JUST IN THE EVENT THIS IS EVER NEEDED, I ADDED IT 
		return self.employees[index]

	def get_current(self):
		return self.employees[self.index_of_items]

	def has_another(self):
		if self.index_of_items >= len(self.employees):
			return False
		else:
			return True

	def next(self):
		next_employee = self.employees[self.index_of_items]
		self.index_of_items += 1
		return next_employee

class EmployeeStateIterator(AbstractIterator):
	def __init__(self, employees):
		import operator
		employees.sort(key = operator.attrgetter('state'))
		self.employees = employees
		self.index_of_items = 0

	def set_first(self):#NOT NEEDED, SET TO FIRST DONE IN INIT, HERE FOR COMPLETENESS
		self.index_of_items = 0

	def get_element(self, index):#JUST IN THE EVENT THIS IS EVER NEEDED, I ADDED IT 
		return self.employees[index]

	def get_current(self):
		return self.employees[self.index_of_items]

	def has_another(self):
		if self.index_of_items >= len(self.employees):
			return False
		else:
			return True

	def next(self):
		next_employee = self.employees[self.index_of_items]
		self.index_of_items += 1
		return next_employee
class AbstractAllEmployees():
	def add(self, item_to_add):
		pass

	def create_name_iterator(self):
		pass

	def create_job_iterator(self):
		pass

	def create_state_iterator(self):
		pass

class AllEmployees(AbstractAllEmployees):
	def __init__(self):
		self.employees = []

	def add(self, item_to_add):
		self.employees.append(item_to_add)

	def create_name_iterator(self):
		return EmployeeNameIterator(self.employees)

	def create_job_iterator(self):
		return EmployeePositionIterator(self.employees)

	def create_state_iterator(self):
		return EmployeeStateIterator(self.employees)