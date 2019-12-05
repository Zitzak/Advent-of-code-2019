from state_machine import StateMachine

def get_input_list_ints():

	f = open("../tests/test4.txt", 'r')
	# f = open("../input/day5_input.txt", 'r')
	input_list = f.readline()
	input_list = list(input_list.split(","))
	input_list = [int(i) for i in input_list]
	f.close()
	return input_list

if __name__ == "__main__":

	# test = "10"
	# print(test[-1])
	# print(test[-2:-1])
	# print(test[-3:-2])
	input_list = get_input_list_ints()
	# print(input_list)
	state_machine = StateMachine(input_list)
	state_machine.run()
	# print(state_machine)