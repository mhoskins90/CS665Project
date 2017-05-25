import Module_Payments as payments #MODULE 1
import Module_WorkOrders as workOrders #MODULE 2
import Module_Utilities as utilities #MODULE 3

import pytest#YOU MUST INSTALL PYTEST ON SYSTEM FOR THIS TO WORK
#pip install pytest

QuestionInputValidation = utilities.QuestionInputValidation()
PaymentOutput = payments.PaymentOutput()
DelinquentNotice = payments.DelinquentNotice()
WorkOrderOutput = workOrders.WorkOrderOutput()
DatabaseManager1 = utilities.DatabaseManager()#SINGLETON
DatabaseManager2 = utilities.DatabaseManager()#SINGLETON

###########--------------UTILITIES TESTS-----------------###########
#-------------------------------------------------------------------
def test_singleton_database():
	assert id(DatabaseManager1) == id(DatabaseManager2)


#TESTS VALIDATION
integer_for_test = 1234
float_for_test = 50.99
date_for_test = '05/05'#THIS IS THE FORMAT NEEDED
string_for_test = 'This is a test'

def test_integer_validation():
	if QuestionInputValidation.validate_integer(integer_for_test) == 'bad':
		assert False#USED TO CATCH PYTEST
	else:
		assert True

def test_date_validation():
	if QuestionInputValidation.validate_date(date_for_test) == 'bad':
		assert False
	else:
		assert True

def test_monetary_float_validation():
	if QuestionInputValidation.validate_monetary_float(float_for_test) == 'bad':
		assert False
	else:
		assert True

def test_string_length_validation():
	if QuestionInputValidation.validate_string_length(string_for_test) == 'bad':
		assert False
	else:
		assert True

#-------------------------------------------------------------------

PaymentFactory1 = payments.PaymentFactory()#SINGLETON
PaymentFactory2 = payments.PaymentFactory()#SINGLETON

###########--------------PAYMENTS TESTS-----------------###########
def test_singleton_payment_factory():
	assert id(PaymentFactory1) == id(PaymentFactory2)

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
		PaymentOutput.determine([{'unit_number':17, 'due_date':'05/05', 'date_collected':'05/05', 'amount_due':1100, 'amount_collected':900}])
	except Exception:
		assert False
	else:
		assert True

list_for_test = ['Test: for Test in Test.']

def test_display_p():
	try:
		PaymentOutput.display(list_for_test)
	except Exception:
		assert False
	else:
		assert True



def test_generate_late_payment_document():
	try:
		DelinquentNotice.generate_late_payment_document(list_for_test)
	except Exception:
		assert False
	else:
		assert True


###########--------------WORK ORDER MODULE TESTS-----------------###########
WorkOrderFactory1 = workOrders.WorkOrderFactory()#SINGLETON
WorkOrderFactory2 = workOrders.WorkOrderFactory()#SINGLETON
#TESTS
def test_singleton_work_order_factory():
	assert id(WorkOrderFactory1) == id(WorkOrderFactory2)
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
tuple_to_display = ()
dict_of_answers = [{'unit_number': 'test', 'issue': 'test','type': 'test'}]
def test_determine():
	try:
		WorkOrderOutput.determine()
	except Exception:
		assert False
	else:
		assert True

def test_display():
	try:
		WorkOrderOutput.display(tuple_to_display)
	except Exception:
		assert False
	else:
		assert True

def test_store():
	try:
		WorkOrderOutput.store([{'unit_number': 0, 'issue': 'test', 'type': 'test'}])
	except Exception:
		assert False
	else:
		assert True