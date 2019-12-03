from calculator import Calculator

def get_input_from_file(path):

	f = open(path, "r")
	input_file = f.readlines()
	return input_file

def test_cases(input_file):


	list1 = list(input_file[0].split(','))
	list2 = list(input_file[1].split(','))
	list1[-1] = list1[-1].strip()
	calc = Calculator(list1, list2)
	calc.run()
	print(calc)

if __name__ == '__main__':

	test = "../tests/test.txt"
	test1 = "../tests/test1.txt"
	test2 = "../tests/test2.txt"
	input_day = "../input/day3_input.txt"
	input_file = get_input_from_file(input_day)
	test_cases(input_file)
	# print(list1[-2])
	# list2 =  input_file[1]÷
	# print(list1, lis÷t2)
	# list_mass = open("../input/day1_input.txt", 'r')
	# fuel_calculator = CalcFuel(list_mass)
	# fuel_calculator.run_part1()
	# list_mass.close()
	# print(fuel_calculator)