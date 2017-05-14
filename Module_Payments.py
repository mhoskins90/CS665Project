from Module_Utilities import BadData #CUSTOM EXCEPTION CLASS USED FOR TESTS

class ResidentPaymentDataHandler(object):

	def ask_payment_data_questions(self):
		'''
		METHOD WILL ASK ALL QUESTIONS FOR PAYMENT DATA ENTRY
		QUESTIONS WILL INCLUDE:
		UNIT NUMBER, DUE DATE, DATE PAYMENT WAS ACCEPTED, AMOUNT DUE, AND AMOUNT COLLECTED
		'''

		continue_asking_payment_data_questions = "yes"
		while continue_asking_payment_data_questions.lower() == "y" or continue_asking_payment_data_questions.lower() == "yes":
			self.unit_number = input("Please enter the appropriate unit number:  ")
			self.due_date = input("Please enter due date for rent:  ")
			self.date_collected = input("Please enter date rent was collected:  ")
			self.amount_due = input("Please enter amount due:  ")
			self.amount_collected = input("Please enter amount collected:  ")
			continue_asking_payment_data_questions = input("Continue entering payment data? (Y) Yes | Enter any other key to stop:  ")
			if continue_asking_payment_data_questions.lower() != "y" and continue_asking_payment_data_questions.lower() != "yes":
				break
			else:
				continue

		#raise BadData

class DelinquentNoticeDocumentGenerator(object):
	'''
	TECHNICALLY THIS COULD BE A COMMON UTILITY, BUT AT THIS TIME ONLY PAYMENT DOCUMENTS ARE GENERATED SO IT IS
	MODULIZED HERE. WORK ORDER DATA WOULD NOT NEED TO BE MADE INTO A DOCUMENT SO THIS WILL REMAIN HERE UNTIL 
	A NEW TASK THAT REQURES DOCUMENT GENERATION IS CREATED IN FUTURE RELEASES.
	'''
	def generate_late_rent_document(self):
		'''
		METHOD WILL GENERATE TEXT FILE FOR EACH UNIT THAT STILL OWES MONEY
		'''
		raise BadData
