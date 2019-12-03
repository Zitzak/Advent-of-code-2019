from get_input_files import GetInputFiles
from calculator import Calculator

class UnitTest:

	def __init__(self):
		input_files = GetInputFiles()
		self.test_sollutions_part1 = [6, 159, 135]
		self.test_sollutions_part2 = [30, 610, 410]
		self.test_cases = input_files.get_test_cases()
		self.calc = Calculator([0,0], [0,0])

	def run_tests_part1(self):

		for elem in range(len(self.test_cases)):
			self.calc.update_init(self.test_cases[elem][0], self.test_cases[elem][1])
			self.calc.run_part1()
			if self.calc.lowest_manhattan_distance == self.test_sollutions_part1[elem]:
				print("Test %i correct\n" % (elem + 1))
			else:
				print("Test %i failed\n" % (elem + 1))

	def run_tests_part2(self):

		for elem in range(len(self.test_cases)):
			self.calc.update_init(self.test_cases[elem][0], self.test_cases[elem][1])
			self.calc.run_part2()
			if self.calc.crossing_points_in_steps_list[0] == self.test_sollutions_part2[elem]:
				print("Test %i correct\n" % (elem + 1))
			else:
				print("Test %i failed\n" % (elem + 1))
