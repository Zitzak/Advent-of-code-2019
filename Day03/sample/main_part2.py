from calculator import Calculator
from get_input_files import GetInputFiles
from unit_test import UnitTest

if __name__ == '__main__':

	# unit_test = UnitTest()
	# unit_test.run_tests_part2()


	input_file = GetInputFiles()
	input_list = input_file.get_input()
	calc = Calculator(input_list[0], input_list[1])
	calc.run_part2()
