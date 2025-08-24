class Employee:
	_companyName = 'Capco Technologies Pvt Ltd.'
	def __init__(self, id, name, doj):
		self.id, self.name, self.doj = id, name, doj 
	
	@classmethod
	def getCompanyName(cls):
		return cls._companyName
		
	@staticmethod
	def someMethod():
		print(f'SomeMethod() called')

	def __str__(self):
		return f'Id: {self.id} Name: {self.name}  Doj:{self.doj}'
	
if __name__ == '__main__':
	obj = Employee(1011, 'Sachin', '12-8-2021')
	print(obj)
	print(f'Company: {Employee.getCompanyName()}')
	Employee.someMethod()
	print('*' * 50)
	print(obj.__str__)
	print(obj.getCompanyName)
	print(obj.someMethod)
