#---------------------------------------------------------------------------SINGLETON

class Singleton(type):
	def __init__(self, className, bases, attributes, **kwargs):
		#super().__init__(className, bases, attributes)
		self.only_instance = None

	def __call__(self, *args, **kwargs):
		if self.only_instance is None:
			self.only_instance = super().__call__(*args, **kwargs)
		return self.only_instance

#---------------------------------------------------------------------------
class WorkOrdersSetup():
	def __init__(self):
		import os
		if not os.path.exists("WorkOrders"):
			os.makedirs("WorkOrders")
		
#---------------------------------------------------------------------------
class PaymentsSetup():
	def __init__(self):
		import os
		if not os.path.exists("DelinquentNotices"):
			os.makedirs("DelinquentNotices")
#---------------------------------------------------------------------------			
class AdministrativeContactsSetup():
	def __init__(self):
		import Module_Contacts as contacts
		self.all_employees = contacts.AllEmployees()

		emp1 =  contacts.CompanyEmployee("Compliance","Yvette","Santiago","Georgia", '678-555-4325')
		emp2 =  contacts.CompanyEmployee("Compliance","Jaime", "Vallgor","Texas", '408-555-5239')
		emp3 =  contacts.CompanyEmployee("Regional","Becky","Lively","Georgia", '770-435-8891')
		emp4 =  contacts.CompanyEmployee("Regional","Misty","Godbey","Texas", '281-727-3344')
		emp5 =  contacts.CompanyEmployee("Regional","Juan","Vegas","Florida", '754-101-5561')
		emp6 =  contacts.CompanyEmployee("IT","Scott","McCurdy","Georgia", '678-903-1212')
		emp7 =  contacts.CompanyEmployee("IT","James","Little","Georgia", '678-231-8871')
		emp8 =  contacts.CompanyEmployee("Owner","Sandra","Harold","Georgia", '770-333-4561')
		emp9 =  contacts.CompanyEmployee("Owner","Robert","Harold","Georgia", '770-333-5562')

		self.all_employees.add(emp1)
		self.all_employees.add(emp2)
		self.all_employees.add(emp3)
		self.all_employees.add(emp4)
		self.all_employees.add(emp5)
		self.all_employees.add(emp6)
		self.all_employees.add(emp7)
		self.all_employees.add(emp8)
		self.all_employees.add(emp9)

#---------------------------------------------------------------------------

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
#---------------------------------------------------------------------------
class DatabaseManager(metaclass=Singleton):
	def __init__(self, mediator, dbFile, dbType="SQLITE3"):
		self.mediator = mediator
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