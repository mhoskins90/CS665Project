class BadData(Exception):#CUSTOM EXCEPTION CLASS USED FOR TESTS
	pass

class Mediator():    
	def __init__(self):
		import Module_Payments as payments
		import Module_WorkOrders as workOrder
		self.objects = []
		self.QuestionInputValidation = QuestionInputValidation(self)
		self.PaymentManager = payments.PaymentManager(self)
		self.PaymentOptions = payments.PaymentOptions(self)
		self.DelinquentNotice = payments.DelinquentNotice(self)
		self.WorkOrderOptions = workOrder.WorkOrderOptions(self)
		self.WorkOrderManager = workOrder.WorkOrderManager(self)
	#def add_object(self, object):	self.objects.append(object)#NOT NEEDED, MAYBE LATER

#-----------------------------------------------------------------------------------------------------------------
class QuestionInputValidation(object):
	def __init__(self, mediator):
		self.mediator = mediator
		#self.QuestionInputValidation = QuestionInputValidation()
	def integer_validation(self, variable):
		'''
		HANDLES INTEGER VALIDATION FOR UNIT NUMBERS
		'''
		try:
			final_variable = int(variable)
		except Exception as error:
			final_variable = 'bad'
			print('Error, {0}'.format(error))
		return final_variable
	def date_validation(self, variable):
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

	def monetary_float_validation(self, variable):
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
	def string_length_validation(self, variable):
		'''
		HANDLES STRING LENGTH VALIDATION TO ENSURE ENTERED WORK ORDER HAS A DESCRIPTION OF THE ISSUE
		'''
		if len(variable) > 2:
			final_variable = variable
		else:
			final_variable ='bad'

		#raise BadData	
#-----------------------------------------------------------------------------------------------------------------
class Output(object):#BASE/ABSTRACT OUTPUT CLASS
	def __init__(self, mediator):
		self.mediator = mediator

	def display(self):
		pass
	def store(self):
		pass