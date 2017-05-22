from Module_Utilities import BadData #CUSTOM EXCEPTION CLASS USED FOR TESTS
from Module_Utilities import Output
import Module_Utilities as utilities

class WorkOrderManager(utilities.AbstractWorkOrderManager):
	def __init__(self):
		self.final_work_order_list = []
		#self.mediator = mediator

	def ask_work_order_questions(self, mediator):
		self.mediator = mediator
		'''
		METHOD WILL ASK ALL QUESTIONS FOR WORK ORDER DATA ENTRY
		QUESTIONS WILL INCLUDE:
		UNIT NUMBER, DESCRIPTION OF ISSUE, POTENTIALLY ALSO STATUS (OPEN OR CLOSED)

		'''
		continue_asking_work_order_questions = "yes"
		valid = "Y"
		while continue_asking_work_order_questions.lower() == "y" or continue_asking_work_order_questions.lower() == "yes":
			dict_of_answers = {'unit_number': '', 'issue': '','resolved': 'N'}
			while True:
				self.unit_number = input("Please enter the appropriate unit number:  ")
				if self.mediator.QuestionInputValidation.integer_validation(self.unit_number) == "bad":#PASSED BY MEDIATOR
					continue
				self.unit_number = self.mediator.QuestionInputValidation.integer_validation(self.unit_number)#PASSED BY MEDIATOR

				dict_of_answers['unit_number'] = self.unit_number
				break
			while True:
				self.issue = input("Please enter a brief description of the issue:  ")
				if self.mediator.QuestionInputValidation.string_length_validation(self.issue) == "bad":#PASSED BY MEDIATOR
					continue
				self.issue = self.mediator.QuestionInputValidation.string_length_validation(self.issue)#PASSED BY MEDIATOR
				dict_of_answers['issue'] = self.issue
				break
			

			self.final_work_order_list.append(dict_of_answers)#THIS ALLOWS FOR MULTPLE ENTRIES
			print(self.final_work_order_list)
			continue_asking_work_order_questions = input("Continue entering Work Orders? (Y) Yes | Enter any other key to stop:  ")
			if continue_asking_work_order_questions.lower() != "y" and continue_asking_work_order_questions.lower() != "yes":
				valid ="Y"
				break
			else:
				valid ="Y"
				continue
		#raise BadData

class WorkOrderOptions(Output):
	def __init__(self, mediator):
		self.mediator = mediator

	def determine(self):
		'''
		METHOD WILL DETERMINE ENTERED WORK ORDERS
		'''
		raise BadData
	def display(self):
		'''
		METHOD WILL DISPLAY WORK ORDER ENTRIES
		'''
		raise BadData
	def store(self):
		'''
		METHOD WILL STORE WORK ORDER ENTRIES
		'''
		raise BadData