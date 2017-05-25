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
#-----------------------------------------------------------------------------------------------------------------
class CompanyContacts():
	def display_name_number(self):
		pass


class ComplianceDirectors(CompanyContacts):
	#LEAF
	def __init__(self, name, phone):
		self.type = 'Compliance Director'
		self.name = name
		self.phone = phone

	def display_name_number(self):
		print('{0}: {1} - {2}'.format(self.type, self.name, self.phone))

class RegionalDirectors(CompanyContacts):
	#LEAF
	def __init__(self, location, name, phone):
		self.type = 'Regional Director'
		self.location = location
		self.name = name
		self.phone = phone

	def display_name_number(self):
		print('{0}-{1}: {2} - {3}'.format(self.type, self.location, self.name, self.phone))


class CorporateDirectors(CompanyContacts):
	#NON LEAF
	def __init__(self):
		self.children = []

	def display_name_number(self):
		for child_object in self.children:
			child_object.display_name_number()

	def add(self, object_child):
		if object_child not in self.children:#I COULD HAVE USED SET BUT THERE WERE ODD ORDERING ISSUES WHEN CHILDREN WERE ADDED
			self.children.append(object_child)


class IT(CorporateDirectors):
	#LEAF
	def __init__(self, name, phone):
		#super().__init__()
		self.OuterType = 'Corporate Director'
		self.InnerType = "Internet Technology"
		self.name = name
		self.phone = phone

	def display_name_number(self):
		print('{0}-{1}: {2} - {3}'.format(self.OuterType, self.InnerType, self.name, self.phone))

class Owner(CorporateDirectors):
	#LEAF
	def __init__(self, name, phone):
		#super().__init__()
		self.type = 'Owner'
		self.name = name
		self.phone = phone

	def display_name_number(self):
		print('{0}: {1} - {2} {3}'.format(self.type, self.name, self.phone, "(Only Call If Nessesary)"))