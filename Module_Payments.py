from Module_Utilities import BadData #CUSTOM EXCEPTION CLASS USED FOR TESTS
import Module_Utilities as utilities
from Module_Utilities import Output

class PaymentManager(object):
	def __init__(self, mediator):
		self.final_payment_list = []
		self.mediator = mediator#MEDIATOR OBJECT
		self.duplicate_entries = []


	def ask_payment_data_questions(self):
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
				if self.mediator.QuestionInputValidation.integer_validation(self.unit_number) == "bad":#PASSED BY MEDIATOR
					continue
				self.unit_number = self.mediator.QuestionInputValidation.integer_validation(self.unit_number)#PASSED BY MEDIATOR
				#if self.unit_number in self.duplicate_entries:
				#	print('Error, unit number already entered. Try again.')
				#	continue

				#self.duplicate_entries.append(self.unit_number)

				dict_of_answers['unit_number'] = self.unit_number
				break
			while True:
				self.due_date = input("Please enter due date for rent (mm/dd):  ")
				if self.mediator.QuestionInputValidation.date_validation(self.due_date) == "bad":#PASSED BY MEDIATOR
					continue
				self.due_date = self.mediator.QuestionInputValidation.date_validation(self.due_date)#PASSED BY MEDIATOR

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
				if self.mediator.QuestionInputValidation.date_validation(self.date_collected) == "bad":#PASSED BY MEDIATOR
					continue
				self.date_collected = self.mediator.QuestionInputValidation.date_validation(self.date_collected)#PASSED BY MEDIATOR
				dict_of_answers['date_collected'] = self.date_collected
				break
			while True:
				if valid =="N":
					break	
				self.amount_due = input("Please enter amount due:  ")
				if self.mediator.QuestionInputValidation.monetary_float_validation(self.amount_due) == "bad":#PASSED BY MEDIATOR
					continue
				self.amount_due = self.mediator.QuestionInputValidation.monetary_float_validation(self.amount_due)#PASSED BY MEDIATOR
				dict_of_answers['amount_due'] = self.amount_due
				break
			while True:
				if valid =="N":
					break
				self.amount_collected = input("Please enter amount collected:  ")
				if self.mediator.QuestionInputValidation.monetary_float_validation(self.amount_collected) == "bad":#PASSED BY MEDIATOR
					continue
				self.amount_collected = self.mediator.QuestionInputValidation.monetary_float_validation(self.amount_collected)#PASSED BY MEDIATOR
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

		#raise BadData

class PaymentOptions(Output):
	def __init__(self, mediator):
		self.mediator = mediator

	def determine(self, list_of_dictionaries):
		'''
		METHOD WILL CALCULATE ENTRIES THAT STILL OWE MONEY
		'''		
		import datetime

		self.list_of_overdue_residents, self.list_of_residents_that_owe_nothing, self.list_of_residents_that_paid_extra, self.list_to_display = [],[],[],[]
		for dictionary in list_of_dictionaries:
			if dictionary['amount_collected'] < dictionary['amount_due']:#IF AMOUNT COLLECTED IS LESS THAN AMOUNT DUE
				self.list_of_overdue_residents.append(dictionary)#ONLY ONE IMPORTANT NOW
			elif dictionary['amount_collected'] == dictionary['amount_due']:#IF AMOUNT COLLECTED IS EQUAL TO AMOUNT DUE
				self.list_of_residents_that_owe_nothing.append(dictionary)
			else:#RESIDENT OVERPAID, WHICH IS NOT OVERLY COMMON
				self.list_of_residents_that_paid_extra.append(dictionary)

		#combined_dictionary = { k:[d[k] for d in self.list_of_overdue_residents] for k in self.list_of_overdue_residents[0] }#NOT NEEDED NOW, MAYBE LATER
		#print(combined_dictionary)#TESTING
		for single_entry in self.list_of_overdue_residents:
			amount_still_needed = float(single_entry['amount_due']) - float(single_entry['amount_collected'])
			date_for_determination = datetime.datetime.strptime(single_entry['due_date'], "%m/%d")
			month_for_determination = date_for_determination.strftime('%B')
			today = datetime.datetime.now()
			year_for_determination = today.year
			
			string_to_add_to_list = 'Unit {0}: owes ${1:.2f} for {2} in {3}.'.format(single_entry['unit_number'],amount_still_needed, month_for_determination, year_for_determination)
			self.list_to_display.append(string_to_add_to_list)

		return self.list_to_display

	def display(self, list_of_overdue_residents):
		'''
		METHOD WILL DISPLAY ENTRIES THAT STILL OWE MONEY
		'''
		if list_of_overdue_residents == []:
			print("No Overdue Residents!\n")
		else:
			for bad_unit in list_of_overdue_residents:
				print (bad_unit)
			print('')#FORMATTING

class DelinquentNotice(object):
	'''
	TECHNICALLY THIS COULD BE A COMMON UTILITY, BUT AT THIS TIME ONLY PAYMENT DOCUMENTS ARE GENERATED SO IT IS
	MODULIZED HERE. WORK ORDER DATA WOULD NOT NEED TO BE MADE INTO A DOCUMENT SO THIS WILL REMAIN HERE UNTIL 
	A NEW TASK THAT REQURES DOCUMENT GENERATION IS CREATED IN FUTURE RELEASES.

	METHOD WILL GENERATE TEXT FILE FOR EACH UNIT THAT STILL OWES MONEY
	'''
	def __init__(self, mediator):
		self.mediator = mediator

	def generate_late_rent_document(self, list_of_overdue_residents):
		document_titles = []
		for item in list_of_overdue_residents:
			unit_for_doc_title = item.split(':')[0]
			month_for_doc_title = item.split('for')[1].split(' ')[1]
			year_for_doc_title = item.split('in')[1].split(' ')[1].replace(".","")
			#print(year_for_doc_title)#TESTING
			title_to_append = unit_for_doc_title.replace(" ", "")+'-'+month_for_doc_title+'-'+year_for_doc_title
			document_titles.append(title_to_append)

		
		if document_titles:
			#print(document_titles)#TESTING
			counter = 0
			for document in document_titles:
				with open('DelinquentNotices/'+document+".txt", 'w') as file:
					file.write("Dear Resident,\n\n")
					file.write("Our records indicate that:\n{0}\n\n".format(list_of_overdue_residents[counter]))
					file.write("Please drop by the leasing office and pay at your earliest convenience.\n\n")
					file.write("Sincerely,\n\n")
					file.write("Management")
				counter+=1

		#print(list_of_overdue_residents)TESTING

		#raise BadData
