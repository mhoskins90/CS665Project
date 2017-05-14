import Module_Payments as payments #MODULE 1
import Module_WorkOrders as workOrders #MODULE 2
import Module_Utilities as utilities #MODULE 3


def initial_question():
	global section_to_access#GLOBAL DEC
	while True:
		section_to_access = input("Which section of the program do you want to access? (P) Payments, (WO) Work Orders, (Q) Quit:  ")
		section_to_access = section_to_access.lower()
		if section_to_access !="p" and section_to_access !="wo" and section_to_access !="q":
			print("Error, ({0}) is not a valid entry, try again.".format(section_to_access))
			continue
		else: 
			break


def main():
	
	outer_most_continue = "y"
	while outer_most_continue == "y":
		initial_question()
		if section_to_access == "q" or section_to_access == "quit":
			outer_most_continue ="n"#BREAK OUT OF LOOP

		if section_to_access == "p" or section_to_access == "payments":
			payment_handler = payments.ResidentPaymentDataHandler()
			payment_handler.ask_payment_data_questions()#ASK PAYMENT DATA QUESTIONS





if __name__ == "__main__":
	main()