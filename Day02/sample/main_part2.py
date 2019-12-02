from state_machine import StateMachine
import sys

def get_input_list_ints():

	f = open("../input/day2_input.txt", 'r')
	input_list = f.readline()
	input_list = list(input_list.split(","))
	input_list = [int(i) for i in input_list]
	return input_list


def update_list(noun, verb, input_list):

	input_list[1] = noun
	input_list[2] = verb
	return input_list

if __name__ == "__main__":

	noun = 0
	verb = 0
	input_list = get_input_list_ints()
	state_machine = StateMachine(input_list)

	while noun is not 99:
		verb = 0
		while verb is not 99:
			temp_input_list = update_list(noun, verb, input_list.copy())
			state_machine.update_tape(temp_input_list)
			state_machine.run()
			if state_machine.tape[0] == 19690720:
				print(state_machine.tape[1], state_machine.tape[2])
				sys.exit()
			verb +=1
		noun +=1
			
