from Module_Utilities import BadData #CUSTOM EXCEPTION CLASS USED FOR TESTS
from Module_Utilities import Output

class WorkOrderManager(object):
	def __init__(self, mediator):
		self.mediator = mediator

	def ask_work_order_questions(self):
		'''
		METHOD WILL ASK ALL QUESTIONS FOR WORK ORDER DATA ENTRY
		QUESTIONS WILL INCLUDE:
		UNIT NUMBER, DESCRIPTION OF ISSUE, POTENTIALLY ALSO STATUS (OPEN OR CLOSED)

		'''
		raise BadData

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