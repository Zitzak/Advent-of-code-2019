from state_machine import StateMachine

def get_input_list_ints():

	f = open("../tests/test2.txt", 'r')
	input_list = f.readline()
	input_list = list(input_list.split(","))
	input_list = [int(i) for i in input_list]
	f.close()
	return input_list

if __name__ == "__main__":

	input_list = get_input_list_ints()
	state_machine = StateMachine(input_list)
	state_machine.run()
	print(state_machine)