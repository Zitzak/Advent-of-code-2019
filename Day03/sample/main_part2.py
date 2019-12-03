from calculator import Calculator
from get_input_files import GetInputFiles
from unit_test import UnitTest

def get_input_from_file(paths):

	path_list = []
	for elem in paths:
		f = open(elem, "r")
		input_file = f.readlines()
		path_list.append(input_file.copy())
	return path_list

def create_list(input_file):

	list1 = list(input_file[0].split(','))
	list2 = list(input_file[1].split(','))
	list1[-1] = list1[-1].strip()
	return [list1, list2]

def unit_test(test_list):

	test_cases = []
	for elem in test_list:
		test_cases.append(create_list(elem))


	print(test_cases)
	# list1 = list(input_file[0].split(','))
	# list2 = list(input_file[1].split(','))
	# list1[-1] = list1[-1].strip()
	# calc = Calculator(list1, list2)
	# calc.run()
	# print(calc)

if __name__ == '__main__':

	unit_test = UnitTest()
	# unit_test.run_tests_part1()
	unit_test.run_tests_part2()
