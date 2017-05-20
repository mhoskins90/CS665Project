#ABSTRACT-----------------------------------------------

class abstractFactory(object):
	def Statement(self):
		pass
	def Number(self):
		pass
class AbstractStatement(object):
	def print(self):
		pass
class AbstractNumber(object):
	def print(self):
		pass

#CONCRETE-----------------------------------------------
class randomFactory(abstractFactory):
	def Statement(self):
		return Statement()
	def Number(self):
		return Number()

class concreteFactoryType(): #IS THIS NEEDED FOR ABSTRACT FACTORY?
	def __init__(self,type):
		self.type = type

#CREATED CLASSES-----------------------------------------------
class Statement(AbstractStatement):
	def print(self):
		print("hello from Statement.print()")

class Number(AbstractNumber):
	def print(self):
		print(1234,"from Number.print()")


factory= concreteFactoryType(randomFactory())
statement_object = factory.type.Statement()
number_object = factory.type.Number()
statement_object.print()
number_object.print()

