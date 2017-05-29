class BadData(Exception):#CUSTOM EXCEPTION CLASS USED FOR TESTS
	pass

#class Mediator():    
	#def __init__(self):
		#import Module_Payments as payments
		#import Module_WorkOrders as workOrder
		#self.objects = []
		#self.QuestionInputValidation = QuestionInputValidation(self)
		#self.PaymentManager = payments.PaymentManager(self)
		#self.PaymentOptions = payments.PaymentOptions(self)
		#self.DelinquentNotice = payments.DelinquentNotice(self)
		#self.WorkOrderOptions = workOrder.WorkOrderOptions(self)
		#self.WorkOrderManager = workOrder.WorkOrderManager(self)
	#def add_object(self, object):	self.objects.append(object)#NOT NEEDED, MAYBE LATER

#---------------------------------------------------------------------------------ABSTRACT FACTORY PIECE
		
class factoryType:
	def __init__(self, type):
		self.type = type

#---------------------------------------------------------------------------SINGLETON

class Singleton(type):
	def __init__(self, className, bases, attributes, **kwargs):
		#super().__init__(className, bases, attributes)
		self.only_instance = None

	def __call__(self, *args, **kwargs):
		if self.only_instance is None:
			self.only_instance = super().__call__(*args, **kwargs)
		return self.only_instance


class DatabaseManager(metaclass=Singleton):
	def __init__(self, dbFile, dbType="SQLITE3"):
		import sqlite3
		'''
		PRECONDITIONS: 
		MUST INSTANTIATE WITH DB FILE NAME AND DB TYPE
		DB TYPE IS USED FOR FUTURE FLEXIBILITY
		
		'''
		if dbType.upper() == "SQLITE3":
			self.connection = sqlite3.connect(dbFile)
			self.connection.commit()
			self.cursor = self.connection.cursor()
		elif dbType.upper() == "MYSQL":#SHOWING EASE OF FUTURE ADDITIONS 
			print("{0} Databases Are Not Implemented".format(dbType))
		else:
			print("{0} Databases Are Not Implemented".format(dbType))


	def query(self, statement):
		self.cursor.execute(statement)
		self.connection.commit()#AUTOMATICALLY COMMIT CHANGES
		return self.cursor

	def close(self):
		self.connection.close()


#---------------------------------------------------------------------------





#-----------------------------------------------------------------------------------------------------------------
class QuestionInputValidation(object):
	def __init__(self):
		pass
		#self.QuestionInputValidation = QuestionInputValidation()
	def validate_integer(self, variable):
		'''
		HANDLES INTEGER VALIDATION FOR UNIT NUMBERS
		'''
		try:
			final_variable = int(variable)
		except Exception as error:
			final_variable = 'bad'
			print('Error, {0}'.format(error))
		return final_variable
	def validate_date(self, variable):
		'''
		HANDLES DATE VALIDATION, TO ENSURE DATE IS IN PROPER FORMAT
		'''
		import datetime#NEEDED FOR DATE CHECK

		try:
			final_variable = variable
			datetime.datetime.strptime(final_variable, '%m/%d')
		except Exception as error:
			final_variable = 'bad'
			print('Error, {0}'.format(error))
		return final_variable

	def validate_monetary_float(self, variable):
		'''
		HANDLES MONEY VALIDATION TO ENSURE NUMBER CAN BE CONVERTED TO FLOAT
		'''
		try:
			final_variable = float(variable)
			#final_variable = "{0:.2f}".format(final_variable)
		except Exception as error:
			final_variable = 'bad'
			print('Error, {0}'.format(error))
		return final_variable
	def validate_string_length(self, variable):
		'''
		HANDLES STRING LENGTH VALIDATION TO ENSURE ENTERED WORK ORDER HAS A DESCRIPTION OF THE ISSUE
		'''
		if len(variable) > 2:
			final_variable = variable
		else:
			final_variable ='bad'
			print('Error, {0}'.format("You must enter more than 2 characters."))
		return final_variable

		#raise BadData	
#-----------------------------------------------------------------------------------------------------------------
class GenericOutput(object):#BASE/ABSTRACT OUTPUT CLASS
	def __init__(self):
		pass
	''' 
	#NOT NEEDED
	def select(self, type):
		if type.lower()=="payments":
			import Module_Payments as payments
			return payments.PaymentOutput()
		elif type.lower()=="work":
			import Module_WorkOrders as workOrders
			return workOrders.WorkOrderOutput()
			#pass
		else:
			print("Error in GenericOutput type, '{0}' is not recognized.".format(self.type))
	'''
	@staticmethod
	def make_payment_output():
		import Module_Payments as payments
		return payments.PaymentOutput()

	@staticmethod
	def make_work_order_output():
		import Module_WorkOrders as workOrders
		return workOrders.WorkOrderOutput()
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

class EmployeeNameIterator:
	def __init__(self, employees):
		import operator
		employees.sort(key = operator.attrgetter('last_name'))
		self.index_of_items = 0
		self.employees = employees

	def has_next(self):
		if self.index_of_items >= len(self.employees):
			return False
		else:
			return True

	def next(self):
		next_employee = self.employees[self.index_of_items]
		self.index_of_items += 1
		return next_employee

class EmployeePositionIterator:
	def __init__(self, employees):
		import operator
		employees.sort(key = operator.attrgetter('position'))
		self.employees = employees
		self.index_of_items = 0

	def has_next(self):
		if self.index_of_items >= len(self.employees):
			return False
		else:
			return True

	def next(self):
		next_employee = self.employees[self.index_of_items]
		self.index_of_items += 1
		return next_employee

class EmployeeStateIterator:
	def __init__(self, employees):
		import operator
		employees.sort(key = operator.attrgetter('state'))
		self.employees = employees
		self.index_of_items = 0

	def has_next(self):
		if self.index_of_items >= len(self.employees):
			return False
		else:
			return True

	def next(self):
		next_employee = self.employees[self.index_of_items]
		self.index_of_items += 1
		return next_employee

class AllEmployees:
	def __init__(self):
		self.employees = []

	def add(self, item_to_add):
		self.employees.append(item_to_add)

	def sort_by_last_names(self):
		return EmployeeNameIterator(self.employees)

	def sort_by_job_title(self):
		return EmployeePositionIterator(self.employees)

	def sort_by_state(self):
		return EmployeeStateIterator(self.employees)