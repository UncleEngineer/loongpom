class Loongpom:

	def __init__(self):
		self.name = 'Prawit'
		self.lastname = 'Wongsuwan'
		self.nickname = 'Lung Pom'

	def WhoIAm(self):
		print('My name is {}'.format(self.name))
		print('My lastname is {}'.format(self.lastname))
		print('ชื่อไทย: ประวิตร วงษ์สุวรรณ')

	@property
	def thainame(self):
		return 'ประวิตร วงษ์สุวรรณ'

if __name__ == '__main__':
	myloong = Loongpom()
	print(myloong.name)
	print(myloong.lastname)
	myloong.WhoIAm()
	print(myloong.thainame)