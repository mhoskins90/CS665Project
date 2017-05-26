import Module_Payments as payments #MODULE 1
import Module_WorkOrders as workOrders #MODULE 2
import Module_Utilities as utilities #MODULE 3

valid_payments_selection = ['p','pay','payments','payment']
valid_work_order_selection = ['w','wo','work','order','workorder','workorders']
valid_contacts_selection = ['c','contact','contacts']
valid_quit_selection = ['q', 'quit','stop','exit','exit()', 'end']
combined_valid_entries = valid_payments_selection + valid_work_order_selection +valid_contacts_selection + valid_quit_selection

def initial_question():
	global section_to_access#GLOBAL DEC
	while True:
		section_to_access = input("Which section of the program do you want to access? (P) Payments, (WO) Work Orders, (C) Contacts (Q) Quit:  ")
		section_to_access = section_to_access.lower().replace(" ", "")#FOR WORK ORDERS I HAD TO USE REPLACE AS WELL
		if section_to_access not in combined_valid_entries:
			print("Error, ({0}) is not a valid entry, try again.".format(section_to_access))
			continue
		else: 
			break

def main():
	outer_most_continue = "y"
	#paymentOutput = utilities.GenericOutput().make_payment_output()#TESTING STATIC METHOD
	#print(type(paymentOutput))

	while outer_most_continue == "y":
		initial_question()
		if section_to_access in valid_quit_selection:
			outer_most_continue ="n"#BREAK OUT OF LOOP
#-------------------------------------------------------------------------------------------
		if section_to_access in valid_payments_selection:

			PaymentOutput = utilities.GenericOutput().make_payment_output()#FACTORY
			DelinquentNotice = payments.DelinquentNotice()
			while True:
				payment_selection = input("Do you want to enter (Rent) Rent Payment or (Water) Water Payment? :  ")
				if payment_selection.lower() == 'rent' or payment_selection.lower() == 'r':
					payment_manager= utilities.factoryType(payments.PaymentManager())#ABSTRACT FACTORY
					payment_factory = payment_manager.type.make_payment()
					rent_payment = payment_factory.select('rent')
					rent_payment.ask_payment_data_questions()#ASK PAYMENT DATA QUESTIONS FOR RENTAL ENTRY
					print('')#FORMATTING
					#DETERMINE WHICH RESIDENTS STILL OWE MONEY FOR A MONTH
					overdue_residents = PaymentOutput.determine(rent_payment.final_payment_list)
					#DISPLAY OVERDUE RESIDENTS
					PaymentOutput.display(overdue_residents)
					#PRINT NOTICES FOR OVERDUE RESIDENTS
					DelinquentNotice.generate_late_payment_document(overdue_residents)#PASSED VIA MEDIATOR
					break
				elif payment_selection.lower() == 'water' or payment_selection.lower() == 'w':
					payment_manager= utilities.factoryType(payments.PaymentManager())#ABSTRACT FACTORY
					payment_factory = payment_manager.type.make_payment()
					water_payment = payment_factory.select('water')
					water_payment.ask_payment_data_questions()#ASK PAYMENT DATA QUESTIONS FOR RENTAL ENTRY
					print('')#FORMATTING
					#DETERMINE WHICH RESIDENTS STILL OWE MONEY FOR A MONTH
					overdue_residents = PaymentOutput.determine(water_payment.final_payment_list)
					#DISPLAY OVERDUE RESIDENTS
					PaymentOutput.display(overdue_residents)
					#PRINT NOTICES FOR OVERDUE RESIDENTS
					DelinquentNotice.generate_late_payment_document(overdue_residents)#PASSED VIA MEDIATOR
					break
				else:
					print("Error, not a valid entry. Try again.")
					continue
#-------------------------------------------------------------------------------------------
		if section_to_access in valid_work_order_selection:
			WorkOrderOutput = utilities.GenericOutput().make_work_order_output()#FACTORY
			dbHandler = utilities.DatabaseManager("workOrders.db", dbType="sqlite3")#SINGLETON
			dbHandler.query('''CREATE TABLE IF NOT EXISTS 
			workOrders(workOrderID INTEGER PRIMARY KEY, entry_date TEXT default CURRENT_DATETIME, unitNumber INTEGER, type TEXT, issue TEXT)''')#NEED TO ENSURE THIS TABLE IS THERE
			while True:
				work_order_selection = input("Select what you want to do: (B) Bedroom Work Orders, (K) Kitchen Work Orders, (C) Check Work Orders :  ")
				if work_order_selection.lower() == 'bedroom' or work_order_selection.lower() == 'b':
					work_order_manager= utilities.factoryType(workOrders.WorkOrderManager())#ABSTRACT FACTORY
					work_order_factory = work_order_manager.type.make_work_order()
					bedroom_work_order = work_order_factory.select('bedroom')
					bedroom_work_order.ask_work_order_questions()#ASK PAYMENT DATA QUESTIONS FOR RENTAL ENTRY
					print('')#FORMATTING
					
					WorkOrderOutput.store(bedroom_work_order.final_work_order_list)
					break
				elif work_order_selection.lower() == 'kitchen' or work_order_selection.lower() == 'k':
					work_order_manager= utilities.factoryType(workOrders.WorkOrderManager())#ABSTRACT FACTORY
					work_order_factory = work_order_manager.type.make_work_order()
					kitchen_work_order = work_order_factory.select('kitchen')
					kitchen_work_order.ask_work_order_questions()#ASK PAYMENT DATA QUESTIONS FOR RENTAL ENTRY
					print('')#FORMATTING

					WorkOrderOutput.store(kitchen_work_order.final_work_order_list)
					break
				elif work_order_selection.lower() == 'check' or work_order_selection.lower() == 'c':
					selected_items = WorkOrderOutput.determine()#DETERMINE ENTRIES
					WorkOrderOutput.display(selected_items)#DISPLAY					
					break
				else:
					print("Error, invalid entry. Try again.")
					continue			

			print('')#FORMATTING
		if section_to_access in valid_contacts_selection:
			composite_object = utilities.CorporateDirectors()

			YvetteSantiago = utilities.ComplianceDirectors('Yvette Santiago', '678-555-4325')
			composite_object.add(YvetteSantiago)#ADD TO COMPOSITE
			JaimeVallgor = utilities.ComplianceDirectors('Jaime Vallgor', '678-555-5239')
			composite_object.add(JaimeVallgor)#ADD TO COMPOSITE

			BeckyLively = utilities.RegionalDirectors('Georgia','Becky Lively', '770-435-8891')
			composite_object.add(BeckyLively)#ADD TO COMPOSITE
			MistyGodbey = utilities.RegionalDirectors('Texas','Misty Godbey', '281-727-3344')
			composite_object.add(MistyGodbey)#ADD TO COMPOSITE
			JuanVegas = utilities.RegionalDirectors('Florida','Juan Vegas', '754-101-5561')
			composite_object.add(JuanVegas)#ADD TO COMPOSITE
			
			ScottMcCurdy = utilities.IT('Scott McCurdy', '678-903-1212')
			composite_object.add(ScottMcCurdy)
			JamesLittle = utilities.IT('James Little', '678-231-8871')
			composite_object.add(JamesLittle)

			SandraHarold= utilities.Owner('Sandra Harold', '770-333-4561')
			composite_object.add(SandraHarold)
			RobertHarold= utilities.Owner('Robert Harold', '770-333-5562')
			composite_object.add(RobertHarold)
			
			print('\n#################### ADMINISTRATIVE COMPANY CONTACTS ####################')
			composite_object.display_name_number()#DISPLAY TREE

			print('')#FORMATTING

if __name__ == "__main__":
	main()