from Module_Utilities import BadData #CUSTOM EXCEPTION CLASS USED FOR TESTS
from Module_Utilities import GenericOutput
import Module_Utilities as utilities


class AbstractWorkOrderFactory():
	def make_work_order_kitchen(self): 
		pass
	def make_work_order_bedroom(self): 
		pass

class WorkOrderFactory(AbstractWorkOrderFactory, metaclass=utilities.Singleton):
	def select(self, type):
		if type.lower()=="bedroom":
			return WorkOrderBedroom()
		elif type.lower()=='kitchen':
			return WorkOrderKitchen()
		else:
			print('Error, wrong payment type entered.')
	def make_work_order_kitchen(self): 
		pass
	def make_work_order_bedroom(self): 
		pass

class WorkOrderBedroom():
	def __init__(self):
		self.final_work_order_list = []
		#self.mediator = mediator

	def ask_work_order_questions(self):
		QuestionInputValidation = utilities.QuestionInputValidation()
		
		'''
		METHOD WILL ASK ALL QUESTIONS FOR WORK ORDER DATA ENTRY
		QUESTIONS WILL INCLUDE:
		UNIT NUMBER, DESCRIPTION OF ISSUE, POTENTIALLY ALSO STATUS (OPEN OR CLOSED)

		'''
		continue_asking_work_order_questions = "yes"
		valid = "Y"
		while continue_asking_work_order_questions.lower() == "y" or continue_asking_work_order_questions.lower() == "yes":
			dict_of_answers = {'unit_number': '', 'issue': '','type': 'Bedroom'}
			while True:
				self.unit_number = input("Please enter the appropriate unit number:  ")
				if QuestionInputValidation.validate_integer(self.unit_number) == "bad":#PASSED BY MEDIATOR
					continue
				self.unit_number = QuestionInputValidation.validate_integer(self.unit_number)#PASSED BY MEDIATOR

				dict_of_answers['unit_number'] = self.unit_number
				break
			while True:
				self.issue = input("Please enter a brief description of the issue:  ")
				if QuestionInputValidation.validate_string_length(self.issue) == "bad":#PASSED BY MEDIATOR
					continue
				self.issue = QuestionInputValidation.validate_string_length(self.issue)#PASSED BY MEDIATOR
				dict_of_answers['issue'] = self.issue
				break
			

			self.final_work_order_list.append(dict_of_answers)#THIS ALLOWS FOR MULTPLE ENTRIES
			#print(self.final_work_order_list)
			continue_asking_work_order_questions = input("Continue entering Work Orders? (Y) Yes | Enter any other key to stop:  ")
			if continue_asking_work_order_questions.lower() != "y" and continue_asking_work_order_questions.lower() != "yes":
				valid ="Y"
				break
			else:
				valid ="Y"
				continue

class WorkOrderKitchen():
	def __init__(self):
		self.final_work_order_list = []
		#self.mediator = mediator

	def ask_work_order_questions(self):
		QuestionInputValidation = utilities.QuestionInputValidation()
		
		'''
		METHOD WILL ASK ALL QUESTIONS FOR WORK ORDER DATA ENTRY
		QUESTIONS WILL INCLUDE:
		UNIT NUMBER, DESCRIPTION OF ISSUE, POTENTIALLY ALSO STATUS (OPEN OR CLOSED)

		'''
		continue_asking_work_order_questions = "yes"
		valid = "Y"
		while continue_asking_work_order_questions.lower() == "y" or continue_asking_work_order_questions.lower() == "yes":
			dict_of_answers = {'unit_number': '', 'issue': '','type': 'Kitchen'}
			while True:
				self.unit_number = input("Please enter the appropriate unit number:  ")
				if QuestionInputValidation.validate_integer(self.unit_number) == "bad":#PASSED BY MEDIATOR
					continue
				self.unit_number = QuestionInputValidation.validate_integer(self.unit_number)#PASSED BY MEDIATOR

				dict_of_answers['unit_number'] = self.unit_number
				break
			while True:
				self.issue = input("Please enter a brief description of the issue:  ")
				if QuestionInputValidation.validate_string_length(self.issue) == "bad":#PASSED BY MEDIATOR
					continue
				self.issue = QuestionInputValidation.validate_string_length(self.issue)#PASSED BY MEDIATOR
				dict_of_answers['issue'] = self.issue
				break
			

			self.final_work_order_list.append(dict_of_answers)#THIS ALLOWS FOR MULTPLE ENTRIES
			#print(self.final_work_order_list)
			continue_asking_work_order_questions = input("Continue entering Work Orders? (Y) Yes | Enter any other key to stop:  ")
			if continue_asking_work_order_questions.lower() != "y" and continue_asking_work_order_questions.lower() != "yes":
				valid ="Y"
				break
			else:
				valid ="Y"
				continue


class WorkOrderManager():
	def make_work_order(self):
		return WorkOrderFactory()

class AbstractRequiredWOClass():

	def store(self, entered_data):
		pass	

class RequiredWOClass():
	
	def store(self, entered_data):
		'''
		METHOD WILL STORE WORK ORDER ENTRIES
		'''
		for dictionary in entered_data:
			#print(dictionary)
			unit_number = dictionary['unit_number']
			type = dictionary['type']
			issue = dictionary['issue']

			query = 'INSERT INTO workOrders (workOrderID, entry_date, unitNumber, type, issue)VALUES (null,CURRENT_DATE,{0},"{1}","{2}")'.format(unit_number, type, issue)
			#print(query)#TESTING
		#self.dbHandler.query('"INSERT INTO workOrders (workOrderID, entry_date, unitNumber, type, issue)VALUES (?,?,?,?,?)",(1,2,3,4,5)')#ISSUE BECAUSE IT LOOKS LIKE MULTIPLE ARUGMENTS
		self.dbHandler.query(query)
		print('\n------Entry has been saved in DB.------\n')	

class WorkOrderOutput(RequiredWOClass, AbstractRequiredWOClass, GenericOutput):
	#KNOWN ISSUE: NEED TO PROVIDE A METHOD FOR DELETING WORK ORDERS FROM DB. WILL COMPLETE NEXT VERSION.
	def __init__(self):
		import os
		if not os.path.exists("WorkOrders"):#PLACED HERE SO THERE ARE NOT STUPID CRASHES
			os.makedirs("WorkOrders")
		self.dbHandler = utilities.DatabaseManager(os.path.join('WorkOrders', 'workOrders.db'), dbType="sqlite3")#SINGLETON 

	def determine(self):
		'''
		METHOD WILL DETERMINE ENTERED WORK ORDERS
		'''
		results = self.dbHandler.query("SELECT * FROM workOrders")
		selected = results.fetchall()
		return selected
	def display(self, tuple_to_display):
		'''
		METHOD WILL DISPLAY WORK ORDER ENTRIES
		'''
		if len(tuple_to_display) < 1:
			print("\nSorry, no work order entries yet.")
		else:
			for row in tuple_to_display:#0,1,2,3,4
				
				print("{0}: ({1}) Unit {2} has a {4} in the {3}. ".format(row[0], row[1], row[2], row[3], row[4]))

		