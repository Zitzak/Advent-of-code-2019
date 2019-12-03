class GetInputFiles:

	def __init__(self):
		self.test1 = "../tests/test.txt"
		self.test2 = "../tests/test1.txt"
		self.test3 = "../tests/test2.txt"
		self.test_cases_path = [self.test1, self.test2, self.test3]
		self.day03_input = "../input/day3_input.txt"

	def get_input_from_file(self, paths):
		path_list = []
		for elem in paths:
			f = open(elem, "r")
			input_file = f.readlines()
			path_list.append(input_file.copy())
		return path_list

	def create_list(self, input_file):

		list1 = list(input_file[0].split(','))
		list2 = list(input_file[1].split(','))
		list1[-1] = list1[-1].strip()
		return [list1, list2]
	
	def get_test_cases(self):

		return_list = []
		test_cases_read = self.get_input_from_file(self.test_cases_path)
		for elem in test_cases_read:
			return_list.append(self.create_list(elem))
		return return_list

	def get_input(self):
		
		path_read = self.get_input_from_file(self.day03_input)
		return self.create_list(path_read)