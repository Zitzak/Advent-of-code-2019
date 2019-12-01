class CalcFuel:

	def __init__(self, mass_list):
		self.fuel = 0
		self.mass_list = mass_list

	def __str__(self):

		return '{self.fuel}'.format(self=self)

	def run_part1(self):

		for mass in self.mass_list:
			self.fuel += (int((int(mass) / 3)) - 2)

	def calc_fuel_for_fuel_from_mass(self, mass):

		temp = 0
		fuel = 0
		while mass is not 0 and mass > 0:
			fuel += temp
			temp = int(mass / 3) - 2
			mass = temp
		return fuel
	
	def run_part2(self):

		for mass in self.mass_list:
			self.fuel += self.calc_fuel_for_fuel_from_mass(int(mass))

