from CalcFuel import CalcFuel

if __name__ == '__main__':

	list_mass = open("../input/day1_input.txt", 'r')
	fuel_calculator = CalcFuel(list_mass)
	fuel_calculator.run_part1()
	print(fuel_calculator)