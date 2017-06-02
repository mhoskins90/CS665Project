import Module_Payments as payments #MODULE 1
import Module_WorkOrders as workOrders #MODULE 2
import Module_Utilities as utilities #MODULE 3

import pytest#YOU MUST INSTALL PYTEST ON SYSTEM FOR THIS TO WORK
#pip install pytest

QuestionInputValidation = utilities.QuestionInputValidation()

###########--------------UTILITIES TESTS-----------------###########
#-------------------------------------------------------------------
def test_singleton_database():
	DatabaseManager1 = utilities.DatabaseManager()#SINGLETON
	DatabaseManager2 = utilities.DatabaseManager()#SINGLETON
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
#-------------------------------------------------------------------ITERATOR
all_employees = utilities.AllEmployees()

def test_name_iterator():
	try:
		emp1 =  utilities.CompanyEmployee("Compliance","Yvette","Santiago","Georgia", '678-555-4325')
		all_employees.add(emp1)
		iterator_list_via_last_names = all_employees.create_name_iterator()
		while iterator_list_via_last_names.has_another():
			person = iterator_list_via_last_names.next()#NEXT RETURNS NEXT PERSON
	except:
		assert False
	else:
		assert True

def test_job_iterator():
	try:
		emp1 =  utilities.CompanyEmployee("Compliance","Yvette","Santiago","Georgia", '678-555-4325')
		all_employees.add(emp1)
		iterator_list_via_job_title = all_employees.create_job_iterator()
		while iterator_list_via_job_title.has_another():
			person = iterator_list_via_job_title.next()
	except:
		assert False
	else:
		assert True
def test_state_iterator():
	try:
		emp1 =  utilities.CompanyEmployee("Compliance","Yvette","Santiago","Georgia", '678-555-4325')
		all_employees.add(emp1)
		iterator_list_via_state = all_employees.create_state_iterator()
		while iterator_list_via_state.has_another():
			person = iterator_list_via_state.next()
	except:
		assert False
	else:
		assert True
#-------------------------------------------------------------------STATE

final_payment_list = [{'unit_number':17, 'due_date':'05/05', 'date_collected':'05/05', 'amount_due':1100, 'amount_collected':900}]

def test_state_display():
	starting_state = utilities.StateForStarting()#STATE
	PaymentOutput = utilities.GenericOutput().make_payment_output(starting_state)#STATE CHANGE
	try:
		PaymentOutput.do_request(final_payment_list, type='rent')
	except:
		assert False
	else:
		assert True

def test_state_display():
	state_for_display = utilities.StateForDisplay()#STATE
	PaymentOutput = utilities.GenericOutput().make_payment_output(state_for_display)#STATE CHANGE
	try:
		PaymentOutput.do_request(final_payment_list, type='rent')
	except:
		assert False
	else:
		assert True

def test_state_ending():
	ending_state = utilities.StateForDocumentGeneration()#STATE
	PaymentOutput = utilities.GenericOutput().make_payment_output(ending_state)#STATE CHANGE
	try:
		PaymentOutput.do_request(final_payment_list, type='rent')
	except:
		assert False
	else:
		assert True
#-------------------------------------------------------------------MEDIATOR
mediator = utilities.ConcreteMediator()#MEDIATOR

def test_mediator_display():
	try:
		mediator.WorkOrderDetermine.display(mediator.WorkOrderDetermine.determine())
	except:
		assert False
	else:
		assert True

def test_mediator_storage():
	try:
		mediator.WorkOrderStorage.store([{'unit_number': 0, 'issue': 'test', 'type': 'test'}])#MEDIATOR
	except:
		assert False
	else:
		assert True
