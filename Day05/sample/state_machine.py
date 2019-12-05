class StateMachine:

	def __init__(self, input_list):

		self.tape = input_list
		self.index = 0
		self.plus_state = 1
		self.multi_state = 2
		self.input_state = 3
		self.output_state = 4
		self.jump_if_true_state = 5
		self.jump_if_false_state = 6
		self.less_the_state = 7
		self.equals_state = 8
		self.final_state = 99
		self.current_state = 0
		self.user_input = 0
		self.parameters_intstructions = ""
		self.get_next_state()

	def __str__(self):

		return '{self.tape}'.format(self=self)

	def update_tape(self, tape):

		self.index = 0
		self.tape = tape
		self.get_next_state()

	def get_next_state(self):

		upcode = str(self.tape[self.index])
		self.current_state = upcode[-2:]
		if self.current_state[0] == "0":
			self.current_state = self.current_state[1]
		self.current_state = int(self.current_state)
		# print("state - ", self.current_state)
	
	def get_num_from_tape_plus_index(self, temp_index):

		if temp_index == '1':
			index = self.index
		else:
			index = self.tape[self.index]
		return self.tape[index]

	def calculate(self, int1, int2):

		if self.current_state == self.plus_state:
			return int1 + int2
		else:
			return int1 * int2
	
	def put_sum_in_tape(self, sum):
		# print("4", self.tape[self.index])

		self.tape[self.tape[self.index]] = sum

	def get_parameters_instructions(self):

		temp_string = ""

		parameters_intstructions = str(self.tape[self.index])
		if len(parameters_intstructions) != 1:
			temp_string = parameters_intstructions[:-2]
		else:
			temp_string = "00"
		self.parameters_intstructions = temp_string

	def index_plus_1(self):

		self.index += 1
	
	def multi_or_plus_state_processing(self):

		int1 = self.get_num_from_tape_plus_index(self.parameters_intstructions[-1])
		self.index_plus_1()
		int2 = self.get_num_from_tape_plus_index(self.parameters_intstructions[-2:-1])
		self.index_plus_1()
		sum = self.calculate(int1, int2)
		self.put_sum_in_tape(sum)
		self.index_plus_1()
		# self.get_next_state()

	def input_state_processing(self):

		# print("test1", self.index)
		self.put_sum_in_tape(self.user_input)
		self.index_plus_1()
		self.get_next_state()

	def output_state_processing(self):
		
		# print("test2", self.index)
		print(self.get_num_from_tape_plus_index(0))
		self.index_plus_1()
		self.get_next_state()

	def jump_if_true_state_processing(self):

		# print("test3", self.index)
		if self.get_num_from_tape_plus_index(self.parameters_intstructions[-1]) != 0:
			self.index_plus_1()
			self.index = self.get_num_from_tape_plus_index(self.parameters_intstructions[-2:-1])
	
	def jump_if_false_state_processing(self):

		# print("test4", self.index)
		if self.get_num_from_tape_plus_index(self.parameters_intstructions[-1]) == 0:
			self.index_plus_1()
			self.index = self.get_num_from_tape_plus_index(self.parameters_intstructions[-2:-1])

	def less_the_state_processing(self):
		# print("test5", self.index)
		int1 = self.get_num_from_tape_plus_index(self.parameters_intstructions[-1])
		self.index_plus_1()
		int2 = self.get_num_from_tape_plus_index(self.parameters_intstructions[-2:-1])
		self.index_plus_1()
		if int1 < int2:
			self.put_sum_in_tape(1)
		else:
			self.put_sum_in_tape(0)
		self.index_plus_1()

	def equals_state_processing(self):

		# print("test6", self.index)
		# print(self.tape)
		int1 = self.get_num_from_tape_plus_index(self.parameters_intstructions[-1])
		self.index_plus_1()
		int2 = self.get_num_from_tape_plus_index(self.parameters_intstructions[-2:-1])
		self.index_plus_1()
		if int1 == int2:
			self.put_sum_in_tape(1)
		else:
			self.put_sum_in_tape(0)
		self.index_plus_1()





	def do_operation(self):

		if self.current_state == self.multi_state or self.current_state == self.plus_state:
			# print("test")
			self.multi_or_plus_state_processing()
		elif self.current_state == self.input_state:
			self.input_state_processing()
		elif self.current_state == self.output_state:
			self.output_state_processing()
		elif self.current_state == self.jump_if_true_state:
			self.jump_if_true_state_processing()
		elif self.current_state == self.jump_if_false_state:
			self.jump_if_false_state_processing()
		elif self.current_state == self.less_the_state:
			self.less_the_state_processing()
		else:
			self.equals_state_processing()

	def run(self):
		print("Fill in the user ID:")
		self.user_input = int(input())
		# print(self.user_input)

		while self.current_state is not self.final_state:
			# print("1", self.index)
			# print(self.tape)
			self.get_parameters_instructions()
			# print("2", self.index)
			self.index_plus_1()
			# print("3", self.index)
			self.do_operation()
			self.get_next_state()

