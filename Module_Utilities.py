import framework as framework
class BadData(Exception):#CUSTOM EXCEPTION CLASS USED FOR TESTS
	pass
#---------------------------------------------------------------------------------ABSTRACT FACTORY PIECE
class factoryType:
	def __init__(self, type):
		self.type = type
#---------------------------------------------------------------------------MEDIATOR 
class AbstractMediator():
	pass

class ConcreteMediator(AbstractMediator, metaclass=framework.Singleton):    
	def __init__(self):
		import Module_WorkOrders as workOrder
		import framework as framework
		import os
		self.WorkOrderDetermine = workOrder.WorkOrderDetermine(self)
		self.WorkOrderStorage = workOrder.WorkOrderStorage(self)

		self.dbHandler = framework.DatabaseManager(self, os.path.join('WorkOrders', 'workOrders.db'))
		#self.objects = []
	#def add_object(self, object):	self.objects.append(object)#NOT NEEDED, MAYBE LATER

#-----------------------------------------------------------------------------------------------------------------
class GenericOutput(object):#BASE/ABSTRACT OUTPUT CLASS
	def __init__(self):
		pass

	@staticmethod
	def make_payment_output(state):
		import Module_Payments as payments
		return payments.PaymentOutput(state)

	@staticmethod
	def make_work_order_output():
		import Module_WorkOrders as workOrders
		return workOrders.WorkOrderOutput()
#-----------------------------------------------------------------------------------------------------------------STATE
class AbstractState():
	def handle_request(self):
		pass

class StateForStarting(AbstractState):
	"""
	STATE OF PAYMENT OUTPUT OBJECT WHEN USER IS DETERMINING WHO IS LATE ON RENT
	"""
	def handle_request(self,list_of_dictionaries):
		print('Nothing done, object still in starting state.')

class StateForDisplay(AbstractState):
	"""
	STATE OF PAYMENT OUTPUT OBJECT WHEN USER IS DISPLAYING ITEMS
	"""

	def handle_request(self,list_of_dictionaries,type=None):
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
		
		for single_entry in self.list_of_overdue_residents:
			amount_still_needed = float(single_entry['amount_due']) - float(single_entry['amount_collected'])
			date_for_determination = datetime.datetime.strptime(single_entry['due_date'], "%m/%d")
			month_for_determination = date_for_determination.strftime('%B')
			today = datetime.datetime.now()
			year_for_determination = today.year
			
			if type == 'rent':
				string_to_add_to_list = 'Unit {0}: owes ${1:.2f} for {2} in {3} for rent.'.format(single_entry['unit_number'],amount_still_needed, month_for_determination, year_for_determination)
			elif type == 'water':
				string_to_add_to_list = 'Unit {0}: owes ${1:.2f} for {2} in {3} for water.'.format(single_entry['unit_number'],amount_still_needed, month_for_determination, year_for_determination)
			else:
				string_to_add_to_list = 'Unit {0}: owes ${1:.2f} for {2} in {3}.'.format(single_entry['unit_number'],amount_still_needed, month_for_determination, year_for_determination)
			self.list_to_display.append(string_to_add_to_list)

		
		if self.list_to_display == []:
			print("No Overdue Residents!\n")
		else:
			for bad_unit in self.list_to_display:
				print (bad_unit)
			print('')#FORMATTING			

class StateForDocumentGeneration(AbstractState):
	"""
	STATE OF PAYMENT OUTPUT OBJECT WHEN USER IS FINISHED
	"""
	def handle_request(self, list_of_dictionaries,type=None):
		import os
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
			if type == 'rent':
				string_to_add_to_list = 'Unit {0}: owes ${1:.2f} for {2} in {3} for rent.'.format(single_entry['unit_number'],amount_still_needed, month_for_determination, year_for_determination)
			elif type == 'water':
				string_to_add_to_list = 'Unit {0}: owes ${1:.2f} for {2} in {3} for water.'.format(single_entry['unit_number'],amount_still_needed, month_for_determination, year_for_determination)
			else:
				string_to_add_to_list = 'Unit {0}: owes ${1:.2f} for {2} in {3}.'.format(single_entry['unit_number'],amount_still_needed, month_for_determination, year_for_determination)
			self.list_to_display.append(string_to_add_to_list)

		#list_of_overdue_residents = []
		document_titles = []
		for item in self.list_to_display:
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
				with open(os.path.join('DelinquentNotices', document+'.txt'), 'a+') as file:
					file.write("Dear Resident,\n\n")
					file.write("Our records indicate that:\n{0}\n\n".format(self.list_to_display[counter]))
					file.write("Please drop by the leasing office and pay at your earliest convenience.\n\n")
					file.write("Sincerely,\n\n")
					file.write("Management")
					file.write("\n\n")
					file.write("-"*50)
					file.write("\n")
				counter+=1