from Module_Utilities import BadData #CUSTOM EXCEPTION CLASS USED FOR TESTS
import Module_Utilities as utilities

class AbstractPaymentFactory():
	def make_payment_for_rent(self): 
		pass
	def make_payment_for_water(self): 
		pass

class PaymentFactory(AbstractPaymentFactory, metaclass=utilities.Singleton):
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
		#self.mediator = mediator#MEDIATOR OBJECT
		self.duplicate_entries = []
		self.type='water'

	def ask_payment_data_questions(self):
		QuestionInputValidation = utilities.QuestionInputValidation()
		#self.final_payment_list = []
		'''
		METHOD WILL ASK ALL QUESTIONS FOR PAYMENT DATA ENTRY
		QUESTIONS WILL INCLUDE:
		UNIT NUMBER, DUE DATE, DATE PAYMENT WAS ACCEPTED, AMOUNT DUE, AND AMOUNT COLLECTED
		'''
		continue_asking_payment_data_questions = "yes"
		valid = "Y"
		while continue_asking_payment_data_questions.lower() == "y" or continue_asking_payment_data_questions.lower() == "yes":
			dict_of_answers = {'unit_number': '', 'due_date': '', 'date_collected': '', 'amount_due': '', 'amount_collected': ''}
			while True:
				self.unit_number = input("Please enter the appropriate unit number:  ")
				if QuestionInputValidation.validate_integer(self.unit_number) == "bad":#PASSED BY MEDIATOR
					continue
				self.unit_number = QuestionInputValidation.validate_integer(self.unit_number)#PASSED BY MEDIATOR


				dict_of_answers['unit_number'] = self.unit_number
				break
			while True:
				self.due_date = input("Please enter due date for rent (mm/dd):  ")
				if QuestionInputValidation.validate_date(self.due_date) == "bad":#PASSED BY MEDIATOR
					continue
				self.due_date = QuestionInputValidation.validate_date(self.due_date)#PASSED BY MEDIATOR

				list_for_check = [self.unit_number, self.due_date.split('/')[0]]#ONLY CHECKS FOR MONTH, HENCE SPLIT[0]
				if list_for_check in self.duplicate_entries:
					print('Error, unit number and month already entered. Try again.')#--------------------------------------------------------------------------------------
					valid = 'N'
					break

				self.duplicate_entries.append(list_for_check)
				#print(self.duplicate_entries)#TESTING
				dict_of_answers['due_date'] = self.due_date
				break				
			while True:
				if valid =="N":
					break
				self.date_collected = input("Please enter date rent was collected (mm/dd):  ")
				if QuestionInputValidation.validate_date(self.date_collected) == "bad":#PASSED BY MEDIATOR
					continue
				self.date_collected = QuestionInputValidation.validate_date(self.date_collected)#PASSED BY MEDIATOR
				dict_of_answers['date_collected'] = self.date_collected
				break
			while True:
				if valid =="N":
					break	
				self.amount_due = input("Please enter amount due:  ")
				if QuestionInputValidation.validate_monetary_float(self.amount_due) == "bad":#PASSED BY MEDIATOR
					continue
				self.amount_due = QuestionInputValidation.validate_monetary_float(self.amount_due)#PASSED BY MEDIATOR
				dict_of_answers['amount_due'] = self.amount_due
				break
			while True:
				if valid =="N":
					break
				self.amount_collected = input("Please enter amount collected:  ")
				if QuestionInputValidation.validate_monetary_float(self.amount_collected) == "bad":#PASSED BY MEDIATOR
					continue
				self.amount_collected = QuestionInputValidation.validate_monetary_float(self.amount_collected)#PASSED BY MEDIATOR
				dict_of_answers['amount_collected'] = self.amount_collected
				break

			self.final_payment_list.append(dict_of_answers)#THIS ALLOWS FOR MULTPLE ENTRIES

			continue_asking_payment_data_questions = input("Continue entering payment data? (Y) Yes | Enter any other key to stop:  ")
			if continue_asking_payment_data_questions.lower() != "y" and continue_asking_payment_data_questions.lower() != "yes":
				valid ="Y"
				break
			else:
				valid ="Y"
				continue

class RentPayments():
	def __init__(self):
		self.final_payment_list = []
		#self.mediator = mediator#MEDIATOR OBJECT
		self.duplicate_entries = []
		self.type='rent'


	def ask_payment_data_questions(self):
		QuestionInputValidation = utilities.QuestionInputValidation()
		#self.final_payment_list = []
		'''
		METHOD WILL ASK ALL QUESTIONS FOR PAYMENT DATA ENTRY
		QUESTIONS WILL INCLUDE:
		UNIT NUMBER, DUE DATE, DATE PAYMENT WAS ACCEPTED, AMOUNT DUE, AND AMOUNT COLLECTED
		'''
		continue_asking_payment_data_questions = "yes"
		valid = "Y"
		while continue_asking_payment_data_questions.lower() == "y" or continue_asking_payment_data_questions.lower() == "yes":
			dict_of_answers = {'unit_number': '', 'due_date': '', 'date_collected': '', 'amount_due': '', 'amount_collected': ''}
			while True:
				self.unit_number = input("Please enter the appropriate unit number:  ")
				if QuestionInputValidation.validate_integer(self.unit_number) == "bad":
					continue
				self.unit_number = QuestionInputValidation.validate_integer(self.unit_number)


				dict_of_answers['unit_number'] = self.unit_number
				break
			while True:
				self.due_date = input("Please enter due date for rent (mm/dd):  ")
				if QuestionInputValidation.validate_date(self.due_date) == "bad":
					continue
				self.due_date = QuestionInputValidation.validate_date(self.due_date)

				list_for_check = [self.unit_number, self.due_date.split('/')[0]]#ONLY CHECKS FOR MONTH, HENCE SPLIT[0]
				if list_for_check in self.duplicate_entries:
					print('Error, unit number and month already entered. Try again.')#--------------------------------------------------------------------------------------
					valid = 'N'
					break

				self.duplicate_entries.append(list_for_check)
				#print(self.duplicate_entries)#TESTING
				dict_of_answers['due_date'] = self.due_date
				break				
			while True:
				if valid =="N":
					break
				self.date_collected = input("Please enter date rent was collected (mm/dd):  ")
				if QuestionInputValidation.validate_date(self.date_collected) == "bad":
					continue
				self.date_collected = QuestionInputValidation.validate_date(self.date_collected)
				dict_of_answers['date_collected'] = self.date_collected
				break
			while True:
				if valid =="N":
					break	
				self.amount_due = input("Please enter amount due:  ")
				if QuestionInputValidation.validate_monetary_float(self.amount_due) == "bad":
					continue
				self.amount_due = QuestionInputValidation.validate_monetary_float(self.amount_due)
				dict_of_answers['amount_due'] = self.amount_due
				break
			while True:
				if valid =="N":
					break
				self.amount_collected = input("Please enter amount collected:  ")
				if QuestionInputValidation.validate_monetary_float(self.amount_collected) == "bad":
					continue
				self.amount_collected = QuestionInputValidation.validate_monetary_float(self.amount_collected)
				dict_of_answers['amount_collected'] = self.amount_collected
				break

			self.final_payment_list.append(dict_of_answers)#THIS ALLOWS FOR MULTPLE ENTRIES

			continue_asking_payment_data_questions = input("Continue entering payment data? (Y) Yes | Enter any other key to stop:  ")
			if continue_asking_payment_data_questions.lower() != "y" and continue_asking_payment_data_questions.lower() != "yes":
				valid ="Y"
				break
			else:
				valid ="Y"
				continue

class PaymentManager():
	def __init__(self):
		#self.type = type
		pass

	def make_payment(self):
		return PaymentFactory()


class PaymentOutput(utilities.GenericOutput):
	def __init__(self, state):
		self.state = state
	#def change_state(self, state):#I THINK THIS OPTION IS CLEANER, BUT IT IS NOT USED 
		#self.state = state
	def do_request(self,list, type):
		self.state.handle_request(list, type)
	print('')#FORMATTING
