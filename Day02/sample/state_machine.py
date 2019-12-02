class StateMachine:

	def __init__(self, input_list):

		self.tape = input_list
		self.index = 0
		self.plus_state = 1
		self.multi_state = 2
		self.final_state = 99
		self.current_state = 0
		self.get_next_state()

	def __str__(self):

		return '{self.tape}'.format(self=self)

	def update_tape(self, tape):

		self.index = 0
		self.tape = tape
		self.get_next_state()

	def get_next_state(self):

		self.current_state = self.tape[self.index]
	
	def get_num_from_tape_plus_index(self):

		return self.tape[self.tape[self.index]]

	def calculate(self, int1, int2):

		if self.current_state == self.plus_state:
			return int1 + int2
		else:
			return int1 * int2
	
	def put_sum_in_tape(self, sum):

		self.tape[self.tape[self.index]] = sum


	def between_states(self):

		self.index += 1
		int1 = self.get_num_from_tape_plus_index()
		self.index += 1
		int2 = self.get_num_from_tape_plus_index()
		self.index += 1
		sum = self.calculate(int1, int2)
		self.put_sum_in_tape(sum)
		self.index += 1
		self.get_next_state()

	def run(self):
		while self.current_state is not self.final_state:
			self.between_states()