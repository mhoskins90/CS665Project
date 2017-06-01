import Module_Payments as payments 
import Module_WorkOrders as workOrders
import Module_Utilities as utilities

valid_payments_selection = ['p','pay','payments','payment']
valid_work_order_selection = ['w','wo','work','order','workorder','workorders']
valid_contacts_selection = ['c','contact','contacts']
valid_quit_selection = ['q', 'quit','stop','exit','exit()', 'end']
combined_valid_entries = valid_payments_selection + valid_work_order_selection +valid_contacts_selection + valid_quit_selection

def initial_question():
	global section_to_access
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
	mediator = utilities.ConcreteMediator()
	while outer_most_continue == "y":
		initial_question()
		if section_to_access in valid_quit_selection:
			outer_most_continue ="n"#BREAK OUT OF LOOP
#-------------------------------------------------------------------------------------------
		if section_to_access in valid_payments_selection:
			starting_state = utilities.StateForStarting()#STATE
			state_for_display = utilities.StateForDisplay()#STATE
			ending_state = utilities.StateForDocumentGeneration()#STATE

			PaymentOutput = utilities.GenericOutput().make_payment_output(starting_state)#FACTORY
			while True:
				payment_selection = input("Do you want to enter (Rent) Rent Payment or (Water) Water Payment? :  ")
				if payment_selection.lower() == 'rent' or payment_selection.lower() == 'r':
					payment_manager= utilities.factoryType(payments.PaymentManager())#ABSTRACT FACTORY
					payment_factory = payment_manager.type.make_payment()
					rent_payment = payment_factory.select('rent')
					rent_payment.ask_payment_data_questions()#ASK PAYMENT DATA QUESTIONS FOR RENTAL ENTRY
					print('')#FORMATTING
					#SET STATE TO DETERMINE WHICH RESIDENTS STILL OWE MONEY FOR A MONTH AND DISPLAY THEM
					PaymentOutput = utilities.GenericOutput().make_payment_output(state_for_display)#STATE CHANGE
					PaymentOutput.do_request(rent_payment.final_payment_list, type='rent')
					#SET STATE TO ENDING STATE AND GENERATE LATE PAYMENT DOCUMENTS
					PaymentOutput = utilities.GenericOutput().make_payment_output(ending_state)#STATE CHANGE
					PaymentOutput.do_request(rent_payment.final_payment_list, type='rent')

					break
				elif payment_selection.lower() == 'water' or payment_selection.lower() == 'w':
					payment_manager= utilities.factoryType(payments.PaymentManager())#ABSTRACT FACTORY
					payment_factory = payment_manager.type.make_payment()
					water_payment = payment_factory.select('water')
					water_payment.ask_payment_data_questions()#ASK PAYMENT DATA QUESTIONS FOR RENTAL ENTRY
					print('')#FORMATTING
					#SET STATE TO DETERMINE WHICH RESIDENTS STILL OWE MONEY FOR A MONTH AND DISPLAY THEM
					PaymentOutput = utilities.GenericOutput().make_payment_output(state_for_display)#STATE CHANGE
					PaymentOutput.do_request(water_payment.final_payment_list, type="water")
					#SET STATE TO ENDING STATE AND GENERATE LATE PAYMENT DOCUMENTS
					PaymentOutput = utilities.GenericOutput().make_payment_output(ending_state)#STATE CHANGE
					PaymentOutput.do_request(water_payment.final_payment_list, type="water")
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
				work_order_selection = input("Select what you want to do: (B) Bedroom Work Orders, (K) Kitchen Work Orders, (C) Check Work Orders, (D) Delete Work Orders :  ")
				if work_order_selection.lower() == 'bedroom' or work_order_selection.lower() == 'b':
					work_order_manager= utilities.factoryType(workOrders.WorkOrderManager())#ABSTRACT FACTORY
					work_order_factory = work_order_manager.type.make_work_order()
					bedroom_work_order = work_order_factory.select('bedroom')
					bedroom_work_order.ask_work_order_questions()#ASK PAYMENT DATA QUESTIONS FOR RENTAL ENTRY
					print('')#FORMATTING
					
					mediator.WorkOrderStorage.store(bedroom_work_order.final_work_order_list)#MEDIATOR ------------------------------------------
					break
				elif work_order_selection.lower() == 'kitchen' or work_order_selection.lower() == 'k':
					work_order_manager= utilities.factoryType(workOrders.WorkOrderManager())#ABSTRACT FACTORY
					work_order_factory = work_order_manager.type.make_work_order()
					kitchen_work_order = work_order_factory.select('kitchen')
					kitchen_work_order.ask_work_order_questions()#ASK PAYMENT DATA QUESTIONS FOR RENTAL ENTRY
					print('')#FORMATTING

					mediator.WorkOrderStorage.store(kitchen_work_order.final_work_order_list)#STORE USING MEDIATOR
					break
				elif work_order_selection.lower() == 'check' or work_order_selection.lower() == 'c':
					selected_items = mediator.WorkOrderDetermine.determine()#DETERMINE ENTRIES VIA MEDIATOR
					mediator.WorkOrderDetermine.display(selected_items)#DISPLAY	VIA MEDIATOR				
					break
				elif work_order_selection.lower() == 'delete' or work_order_selection.lower() == 'd':
					while True:
						selected_items = mediator.WorkOrderDetermine.determine()#DETERMINE ENTRIES VIA MEDIATOR
						mediator.WorkOrderDetermine.display(selected_items)#MEDIATOR ------------------------------------------
						if len(selected_items)>0:

							delete_entry = input('Enter the number of the entry you want to delete:  ')

							result = mediator.WorkOrderStorage.delete(delete_entry)
							print(result)
							if result == 'Row Deleted':
								break
						else:
							break
					break
				else:
					print("Error, invalid entry. Try again.")
					continue			

			print('')#FORMATTING
#-------------------------------------------------------------------------------------------
		if section_to_access in valid_contacts_selection:
			all_employees = utilities.AllEmployees()

			emp1 =  utilities.CompanyEmployee("Compliance","Yvette","Santiago","Georgia", '678-555-4325')
			emp2 =  utilities.CompanyEmployee("Compliance","Jaime", "Vallgor","Texas", '408-555-5239')
			emp3 =  utilities.CompanyEmployee("Regional","Becky","Lively","Georgia", '770-435-8891')
			emp4 =  utilities.CompanyEmployee("Regional","Misty","Godbey","Texas", '281-727-3344')
			emp5 =  utilities.CompanyEmployee("Regional","Juan","Vegas","Florida", '754-101-5561')
			emp6 =  utilities.CompanyEmployee("IT","Scott","McCurdy","Georgia", '678-903-1212')
			emp7 =  utilities.CompanyEmployee("IT","James","Little","Georgia", '678-231-8871')
			emp8 =  utilities.CompanyEmployee("Owner","Sandra","Harold","Georgia", '770-333-4561')
			emp9 =  utilities.CompanyEmployee("Owner","Robert","Harold","Georgia", '770-333-5562')

			all_employees.add(emp1)
			all_employees.add(emp2)
			all_employees.add(emp3)
			all_employees.add(emp4)
			all_employees.add(emp5)
			all_employees.add(emp6)
			all_employees.add(emp7)
			all_employees.add(emp8)
			all_employees.add(emp9)

			while True:
				accepted_type_input = ['n','name','s','state','j','job']
				type_input = input("\nChoose whether to sort by (N) Name, (S) State, (J) Job:  ")
				type_input = type_input.lower()
					
				if type_input in accepted_type_input:				
					if type_input == 'n' or type_input =='name':
						iterator_list_via_last_names = all_employees.create_name_iterator()
						#print(iterator_list_via_last_names.get_element(1).__str__("name"))#THIS IS HOW YOU GET SPECIFIC ELEMENTS
						while iterator_list_via_last_names.has_another():
							person = iterator_list_via_last_names.next()#NEXT RETURNS NEXT PERSON
							print(person.__str__("name"))
						break
					if type_input == 's' or type_input =='state':
						iterator_list_via_state = all_employees.create_state_iterator()
						while iterator_list_via_state.has_another():
							person = iterator_list_via_state.next()
							print(person.__str__("state"))
						break
					if type_input == 'j' or type_input =='job':
						iterator_list_via_job_title = all_employees.create_job_iterator()
						while iterator_list_via_job_title.has_another():
							person = iterator_list_via_job_title.next()
							print(person.__str__("title"))
						break
				else:
					print('\nError, input not accepted. Try again.')
					continue

			print('')#FORMATTING

if __name__ == "__main__":
	main()