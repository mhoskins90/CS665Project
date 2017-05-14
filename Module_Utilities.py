class BadData(Exception):#CUSTOM EXCEPTION CLASS USED FOR TESTS
	pass
#-----------------------------------------------------------------------------------------------------------------
class QuestionInputValidation(object):

	def unit_number_int_validation(self):
		'''
		HANDLES INTEGER VALIDATION FOR UNIT NUMBERS
		'''
		#pass #CHECK FOR ACCURACY
		raise BadData
	def date_validation(self):
		'''
		HANDLES DATE VALIDATION, TO ENSURE DATE IS IN PROPER FORMAT
		'''
		raise BadData
	def monetary_float_validation(self):
		'''
		HANDLES MONEY VALIDATION TO ENSURE NUMBER CAN BE CONVERTED TO FLOAT
		'''
		raise BadData
	def work_order_description_validation(self):
		'''
		HANDLES STRING LENGTH VALIDATION TO ENSURE ENTERED WORK ORDER HAS A DESCRIPTION OF THE ISSUE
		'''
		raise BadData	
#-----------------------------------------------------------------------------------------------------------------
class WorkOrderAndPaymentsCalculations(object):
	def calculate_and_display_delinquent_payments(self):
		'''
		METHOD WILL CALCULATE ENTRIES THAT STILL OWE MONEY AND RETURN THEM TO CONSOLE
		'''
		raise BadData
	def calculate_and_display_work_order_entries(self):
		'''
		METHOD WILL CALCULATE TOTAL WORK ENTRIES FOR ENTERED UNITS AND RETURN THE NUMBER AS WELL AS ISSUE TO CONSOLE
		'''
		raise BadData
