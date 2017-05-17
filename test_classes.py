import Module_Payments as payments #MODULE 1
import Module_WorkOrders as workOrders #MODULE 2
import Module_Utilities as utilities #MODULE 3

import pytest#YOU MUST INSTALL PYTEST ON SYSTEM FOR THIS TO WORK
#pip install pytest

mediator = utilities.Mediator()#MEDIATOR OBJECT

###########--------------UTILITIES TESTS-----------------###########
#-------------------------------------------------------------------

#TESTS VALIDATION
integer_for_test = 1234
float_for_test = 50.99
date_for_test = '05/05'#THIS IS THE FORMAT NEEDED
string_for_test = 'This is a test'

def test_integer_validation():
	if mediator.QuestionInputValidation.integer_validation(integer_for_test) == 'bad':
		assert False#USED TO CATCH PYTEST
	else:
		assert True

def test_date_validation():
	if mediator.QuestionInputValidation.date_validation(date_for_test) == 'bad':
		assert False
	else:
		assert True

def test_monetary_float_validation():
	if mediator.QuestionInputValidation.monetary_float_validation(float_for_test) == 'bad':
		assert False
	else:
		assert True

def test_string_length_validation():
	if mediator.QuestionInputValidation.string_length_validation(string_for_test) == 'bad':
		assert False
	else:
		assert True

#-------------------------------------------------------------------



###########--------------PAYMENTS TESTS-----------------###########


'''
def test_ask_payment_data_questions(): #YOU CAN'T TEST INPUT QUESTIONS
	try:#
		mediator.PaymentManager.ask_payment_data_questions()
	except Exception:
		assert False
	else:
		assert True
'''
#------------------------------------------------------------------

def test_determine_p():
	try:
		mediator.PaymentOptions.determine([{'unit_number':17, 'due_date':'05/05', 'date_collected':'05/05', 'amount_due':1100, 'amount_collected':900}])
	except Exception:
		assert False
	else:
		assert True

list_for_test = ['Test: for Test in Test.']

def test_display_p():
	try:
		mediator.PaymentOptions.display(list_for_test)
	except Exception:
		assert False
	else:
		assert True



def test_generate_late_rent_document():
	try:
		mediator.DelinquentNotice.generate_late_rent_document(list_for_test)
	except Exception:
		assert False
	else:
		assert True


###########--------------WORK ORDER MODULE TESTS-----------------###########

#TESTS
'''
def test_ask_work_order_questions(): #YOU CAN'T TEST INPUT QUESTIONS
	try:
		mediator.WorkOrderManager.ask_work_order_questions()
	except Exception:
		assert False
	else:
		assert True
'''
#-----------------------------------------------------------THESE FAIL BECAUSE THEY HAVE NOT BEEN IMPLEMENTED YET.
def test_determine():
	try:
		mediator.WorkOrderOptions.determine()
	except Exception:
		assert False
	else:
		assert True

def test_display():
	try:
		mediator.WorkOrderOptions.display()
	except Exception:
		assert False
	else:
		assert True

def test_store():
	try:
		mediator.WorkOrderOptions.store()
	except Exception:
		assert False
	else:
		assert True