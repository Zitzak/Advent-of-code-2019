class Calculator:
	
	def __init__ (self, list1, list2):
		self.list1 = list1
		self.list2 = list2
		self.cartesian_points_list1 = [[0, 0]]
		self.cartesian_points_list2 = [[0, 0]]
		self.crossing_points_list = []
		self.crossing_points_in_steps = 0
		self.lowest_manhattan_distance = 0
	
	def update_init(self, list1, list2):

		self.list1 = list1
		self.list2 = list2
		self.cartesian_points_list1 = [[0, 0]]
		self.cartesian_points_list2 = [[0, 0]]
		self.crossing_points_list = []
		self.crossing_points_in_steps_list = []
		self.lowest_manhattan_distance = 0


	def points_to_right(self, steps, cartesian_list):

		last_elem_list = cartesian_list[-1].copy()
		num = last_elem_list[1]
		for i in range(steps):
			num +=1
			cartesian_list.append([last_elem_list[0],num])

	def points_to_left(self, steps, cartesian_list):

		last_elem_list = cartesian_list[-1].copy()
		num = last_elem_list[1]
		for i in range(steps):
			num -=1
			cartesian_list.append([last_elem_list[0],num])

	def points_to_up(self, steps, cartesian_list):

		last_elem_list = cartesian_list[-1].copy()
		num = last_elem_list[0]
		for i in range(steps):
			num +=1
			cartesian_list.append([num, last_elem_list[1]])

	def points_to_down(self, steps, cartesian_list):

		last_elem_list = cartesian_list[-1].copy()
		num = last_elem_list[0]
		for i in range(steps):
			num -=1
			cartesian_list.append([num, last_elem_list[1]])

	def convert_list_to_cartesian_points(self, instructions, cartesian_list):

		for elem in instructions:
			if elem[0] == 'R':
				self.points_to_right(int(elem[1:]), cartesian_list)
			elif elem[0] == 'L':
				self.points_to_left(int(elem[1:]), cartesian_list)
			elif elem[0] == 'U':
				self.points_to_up(int(elem[1:]), cartesian_list)
			else:
				self.points_to_down(int(elem[1:]), cartesian_list)

	def find_crossing_points(self):

		del self.cartesian_points_list1[0]
		del self.cartesian_points_list2[0]
		res_set = set(map(tuple, self.cartesian_points_list1)) & set(map(tuple, self.cartesian_points_list2)) 
		self.crossing_points_list = list(map(list, res_set))

	def find_crossing_point_in_steps(self):

		temp_list = []
		for elem in self.crossing_points_list:
			sum1 = 0
			sum2 = 0
			for elem1 in self.cartesian_points_list2:
				sum1 += 1
				if elem == elem1:
					break
			for elem2 in self.cartesian_points_list1:
				sum2 += 1
				if elem == elem2:
					break
			temp_list.append(sum1 + sum2)
		self.crossing_points_in_steps = min(temp_list)

	def convert_negative_to_positve(self):

		def func(elem):
			for n, i in enumerate(elem):
				if i < 0:
					elem[n] = i * -1
		for elem in self.crossing_points_list:
			func(elem)

	
	def calc_lowest_manhattan_distance(self):

		for elem in self.crossing_points_list:
			temp = elem[0] + elem[1]
			if temp < self.lowest_manhattan_distance or self.lowest_manhattan_distance is 0:
				self.lowest_manhattan_distance = temp


	def run_part1(self):

		self.convert_list_to_cartesian_points(self.list1, self.cartesian_points_list1)
		self.convert_list_to_cartesian_points(self.list2, self.cartesian_points_list2)
		# print(self.cartesian_points_list1, "\n", self.cartesian_points_list2)
		self.find_crossing_points()
		self.convert_negative_to_positve()
		self.calc_lowest_manhattan_distance()
		# print(self.crossing_points_list)

	def run_part2(self):

		self.convert_list_to_cartesian_points(self.list1, self.cartesian_points_list1)
		self.convert_list_to_cartesian_points(self.list2, self.cartesian_points_list2)
		# print(self.cartesian_points_list1, "\n", self.cartesian_points_list2)
		self.find_crossing_points()
		# print(self.crossing_points_list)
		self.find_crossing_point_in_steps()
		print(self.crossing_points_in_steps)
