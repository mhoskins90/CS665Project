import Module_Payments as payments #MODULE 1
import Module_WorkOrders as workOrders #MODULE 2
import Module_Utilities as utilities #MODULE 3


def initial_question():
	global section_to_access#GLOBAL DEC
	while True:
		section_to_access = input("Which section of the program do you want to access? (P) Payments, (WO) Work Orders, (Q) Quit:  ")
		section_to_access = section_to_access.lower().replace(" ", "")#FOR WORK ORDERS I HAD TO USE REPLACE AS WELL
		if section_to_access !="p" and section_to_access !="payments" and section_to_access !="wo" and \
		section_to_access !="workorders" and section_to_access !="workorder" and section_to_access != "q" and section_to_access != "quit":
			print("Error, ({0}) is not a valid entry, try again.".format(section_to_access))
			continue
		else: 
			break

def main():
	outer_most_continue = "y"
	#mediator = utilities.Mediator()#MEDIATOR OBJECT - I UPGRADED THIS TO USE ABSTRACT FACTORY, NOT NEEDED BUT I WANTED TO TEST IT OUT.
	abstract_mediator = utilities.MediatorWrapper(utilities.MediatorConcreteFactory())
	mediator = abstract_mediator.factory.makeMediator()#ABSTRACT FACTORY MEDIATOR OBJECT

	while outer_most_continue == "y":
		initial_question()
		if section_to_access == "q" or section_to_access == "quit":
			outer_most_continue ="n"#BREAK OUT OF LOOP
#-------------------------------------------------------------------------------------------
		if section_to_access == "p" or section_to_access == "payments":

			#test=['Unit 1: owes $35.00 for May in 2017.', 'Unit 2: owes $35.00 for May in 2017.']
			#mediator.DelinquentNotice.generate_late_rent_document(test)#PASSED VIA MEDIATOR

			mediator.PaymentManager.ask_payment_data_questions()#ASK PAYMENT DATA QUESTIONS VIA MEDIATOR, NOT NEEDED BUT WHY NOT...
			print('')#FORMATTING
			
			#DETERMINE WHICH RESIDENTS STILL OWE MONEY FOR A MONTH
			overdue_residents = mediator.PaymentOptions.determine(mediator.PaymentManager.final_payment_list)#PASSED VIA MEDIATOR

			#DISPLAY OVERDUE RESIDENTS
			mediator.PaymentOptions.display(overdue_residents)#PASSED VIA MEDIATOR

			#PRINT NOTICES FOR OVERDUE RESIDENTS
			mediator.DelinquentNotice.generate_late_rent_document(overdue_residents)#PASSED VIA MEDIATOR
#-------------------------------------------------------------------------------------------
		if section_to_access == "wo" or section_to_access == "workorder" or section_to_access == "workorders":
			print("\nSorry, Work Orders are not implemented yet. Try (P) Payments.\n")


if __name__ == "__main__":
	main()