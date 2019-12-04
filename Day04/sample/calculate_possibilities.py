class CalculatePossibilities:

	def __init__(self):

		self.begin = 372304
		self.end = 847060
		self.count = 0
	
	def search_dubbel_digit(self, num):

		for i in range(6):
			x = num.count(num[i])
			if x >= 2:
				return True
		return False

	def search_dubbel_no_trippel_digit(self, num):

		for i in range(6):
			x = num.count(num[i])
			if x == 2:
				return True
		return False

	def check_increase_valid(self, num):

		for i in range(5):
			if int(num[i]) > int(num[i + 1]):
				return False
		return True

	def run_part1(self):

		for num in range(self.begin, self.end):
			if self.check_increase_valid(str(num)):
				if self.search_dubbel_digit(str(num)):
					self.count += 1
		print(self.count)

	def run_part2(self):

		for num in range(self.begin, self.end):
			if self.check_increase_valid(str(num)):
				if self.search_dubbel_no_trippel_digit(str(num)):
					self.count += 1
		print(self.count)