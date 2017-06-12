import framework as framework
import Module_Utilities as utilities

class AbstractPaymentFactory():
	def make_payment_for_rent(self): 
		pass
	def make_payment_for_water(self): 
		pass

class PaymentFactory(AbstractPaymentFactory, metaclass=framework.Singleton):
	def select(self, type):
		if type.lower()=="rent":
			return RentPayments()
		elif type.lower()=='water':
			return WaterPayments()
		else:
			print('Error, wrong payment type entered.')
	def make_payment_for_rent(self): 
		pass
	def make_payment_for_water(self): 
		pass

class WaterPayments():
	def __init__(self):
		self.final_payment_list = []
		self.duplicate_entries = []
		self.type='water'

	def ask_unit_number(self):
		'''
		METHOD ASKS FOR UNIT NUMBER
		'''
		while True:
			self.unit_number = input("Please enter the appropriate unit number:  ")
			if self.QuestionInputValidation.validate_integer(self.unit_number) == "bad":
				continue
			self.unit_number = self.QuestionInputValidation.validate_integer(self.unit_number)

			self.dict_of_answers['unit_number'] = self.unit_number
			break
	def ask_due_date(self):
		'''
		METHOD ASKS DUE DATE
		'''
		while True:
			self.due_date = input("Please enter due date for {0} payment (mm/dd):  ".format(self.type))
			if self.QuestionInputValidation.validate_date(self.due_date) == "bad":
				continue
			self.due_date = self.QuestionInputValidation.validate_date(self.due_date)

			list_for_check = [self.unit_number, self.due_date.split('/')[0]]#ONLY CHECKS FOR MONTH, HENCE SPLIT[0]
			if list_for_check in self.duplicate_entries:
				print('Error, unit number and month already entered. Try again.')#--------------------------------------------------------------------------------------
				self.valid = 'N'
				break
			self.duplicate_entries.append(list_for_check)
				
			self.dict_of_answers['due_date'] = self.due_date
			break
	def ask_date_collected(self):
		'''
		METHOD ASKS DATE COLLECTED
		'''
		while True:
			if self.valid =="N":
				break
			self.date_collected = input("Please enter date {0} payment was collected (mm/dd):  ".format(self.type))
			if self.QuestionInputValidation.validate_date(self.date_collected) == "bad":
				continue
			self.date_collected = self.QuestionInputValidation.validate_date(self.date_collected)
			self.dict_of_answers['date_collected'] = self.date_collected
			break
	def ask_amount_due(self):
		'''
		METHOD ASKS AMOUNT DUE
		'''
		while True:
			if self.valid =="N":
				break	
			self.amount_due = input("Please enter amount due:  ")
			if self.QuestionInputValidation.validate_monetary_float(self.amount_due) == "bad":
				continue
			self.amount_due = self.QuestionInputValidation.validate_monetary_float(self.amount_due)
			self.dict_of_answers['amount_due'] = self.amount_due
			break
	def ask_amount_collected(self):
		'''
		METHOD ASKS AMOUNT COLLECTED
		'''
		while True:
			if self.valid =="N":
				break
			self.amount_collected = input("Please enter amount collected:  ")
			if self.QuestionInputValidation.validate_monetary_float(self.amount_collected) == "bad":
				continue
			self.amount_collected = self.QuestionInputValidation.validate_monetary_float(self.amount_collected)
			self.dict_of_answers['amount_collected'] = self.amount_collected
			break

	def ask_continue_question_for_payments(self):
		self.continue_asking_payment_data_questions = input("Continue entering payment data? (Y) Yes | Enter any other key to stop:  ")
		if self.continue_asking_payment_data_questions.lower() != "y" and self.continue_asking_payment_data_questions.lower() != "yes":
			self.valid ="Y"
			self.continue_asking_payment_data_questions = 'no'
		else:
			self.valid ="Y"
			self.continue_asking_payment_data_questions = 'yes'

	def ask_payment_data_questions(self):
		self.QuestionInputValidation = framework.QuestionInputValidation()
		'''
		METHOD WILL ASK ALL QUESTIONS FOR PAYMENT DATA ENTRY
		'''
		self.continue_asking_payment_data_questions = "yes"
		self.valid = "Y"
		while self.continue_asking_payment_data_questions.lower() == "y" or self.continue_asking_payment_data_questions.lower() == "yes":
			self.dict_of_answers = {'unit_number': '', 'due_date': '', 'date_collected': '', 'amount_due': '', 'amount_collected': ''}
			self.ask_unit_number()
			self.ask_due_date()			
			self.ask_date_collected()
			self.ask_amount_due()
			self.ask_amount_collected()

			if self.valid == 'Y':
				self.final_payment_list.append(self.dict_of_answers)

			self.ask_continue_question_for_payments()

class RentPayments():
	def __init__(self):
		self.final_payment_list = []
		self.duplicate_entries = []
		self.type='rent'

	def ask_unit_number(self):
		'''
		METHOD ASKS FOR UNIT NUMBER
		'''
		while True:
			self.unit_number = input("Please enter the appropriate unit number:  ")
			if self.QuestionInputValidation.validate_integer(self.unit_number) == "bad":
				continue
			self.unit_number = self.QuestionInputValidation.validate_integer(self.unit_number)

			self.dict_of_answers['unit_number'] = self.unit_number
			break
	def ask_due_date(self):
		'''
		METHOD ASKS DUE DATE
		'''
		while True:
			self.due_date = input("Please enter due date for {0} payment (mm/dd):  ".format(self.type))
			if self.QuestionInputValidation.validate_date(self.due_date) == "bad":
				continue
			self.due_date = self.QuestionInputValidation.validate_date(self.due_date)

			list_for_check = [self.unit_number, self.due_date.split('/')[0]]#ONLY CHECKS FOR MONTH, HENCE SPLIT[0]
			if list_for_check in self.duplicate_entries:
				print('Error, unit number and month already entered. Try again.')#--------------------------------------------------------------------------------------
				self.valid = 'N'
				break
			self.duplicate_entries.append(list_for_check)
				
			self.dict_of_answers['due_date'] = self.due_date
			break
	def ask_date_collected(self):
		'''
		METHOD ASKS DATE COLLECTED
		'''
		while True:
			if self.valid =="N":
				break
			self.date_collected = input("Please enter date {0} payment was collected (mm/dd):  ".format(self.type))
			if self.QuestionInputValidation.validate_date(self.date_collected) == "bad":
				continue
			self.date_collected = self.QuestionInputValidation.validate_date(self.date_collected)
			self.dict_of_answers['date_collected'] = self.date_collected
			break
	def ask_amount_due(self):
		'''
		METHOD ASKS AMOUNT DUE
		'''
		while True:
			if self.valid =="N":
				break	
			self.amount_due = input("Please enter amount due:  ")
			if self.QuestionInputValidation.validate_monetary_float(self.amount_due) == "bad":
				continue
			self.amount_due = self.QuestionInputValidation.validate_monetary_float(self.amount_due)
			self.dict_of_answers['amount_due'] = self.amount_due
			break
	def ask_amount_collected(self):
		'''
		METHOD ASKS AMOUNT COLLECTED
		'''
		while True:
			if self.valid =="N":
				break
			self.amount_collected = input("Please enter amount collected:  ")
			if self.QuestionInputValidation.validate_monetary_float(self.amount_collected) == "bad":
				continue
			self.amount_collected = self.QuestionInputValidation.validate_monetary_float(self.amount_collected)
			self.dict_of_answers['amount_collected'] = self.amount_collected
			break

	def ask_continue_question_for_payments(self):
		self.continue_asking_payment_data_questions = input("Continue entering payment data? (Y) Yes | Enter any other key to stop:  ")
		if self.continue_asking_payment_data_questions.lower() != "y" and self.continue_asking_payment_data_questions.lower() != "yes":
			self.valid ="Y"
			self.continue_asking_payment_data_questions = 'no'
		else:
			self.valid ="Y"
			self.continue_asking_payment_data_questions = 'yes'

	def ask_payment_data_questions(self):
		self.QuestionInputValidation = framework.QuestionInputValidation()
		'''
		METHOD WILL ASK ALL QUESTIONS FOR PAYMENT DATA ENTRY
		'''
		self.continue_asking_payment_data_questions = "yes"
		self.valid = "Y"
		while self.continue_asking_payment_data_questions.lower() == "y" or self.continue_asking_payment_data_questions.lower() == "yes":
			self.dict_of_answers = {'unit_number': '', 'due_date': '', 'date_collected': '', 'amount_due': '', 'amount_collected': ''}
			self.ask_unit_number()
			self.ask_due_date()			
			self.ask_date_collected()
			self.ask_amount_due()
			self.ask_amount_collected()

			if self.valid == 'Y':
				self.final_payment_list.append(self.dict_of_answers)

			self.ask_continue_question_for_payments()

class PaymentManager():
	def __init__(self):
		pass

	def make_payment(self):
		return PaymentFactory()


class PaymentOutput(utilities.GenericOutput):
	def __init__(self, state):
		self.state = state
	#def change_state(self, state):#I THINK THIS OPTION IS CLEANER
		#self.state = state
	def do_request(self,list, type):
		self.state.handle_request(list, type)
	print('')#FORMATTING
