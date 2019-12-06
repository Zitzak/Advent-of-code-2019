from state_machine import StateMachine

def get_input_list_ints():

	f = open("../tests/test1.txt", 'r')
	# f = open("../input/day6_input.txt", 'r')
	input_list = f.readlines()
	input_list = list(map(str.strip, input_list))
	f.close()
	return input_list




def recursive(current_planet, orbit_list, num):

	# if current_planet is None or orbit_list is None:
	# 	return
	# num = 1
	# num += 1
		# num +=1
	next_orbit = next((s for s in orbit_list if current_planet in s), False)
	if next_orbit is False:
		print("na false - ", num)
		return False

	print("Voor volgend rec - %i - %s" % (num, next_orbit))

	while next_orbit is not False:
		print("before - ", orbit_list)
		orbit_list.remove(next_orbit)
		print("after - ", orbit_list)
		temp = next_orbit.rsplit(')')
		temp = str(temp[1])
		print("next iter - ",temp)
		print(num)
		num += recursive(temp, orbit_list, (num + 1))
		# if temp is False:
		# 	num -=1
		# else:
		# 	num =  num + temp 


		next_orbit = next((s for s in orbit_list if current_planet in s), False)
	# print(temp)



		

	
	return num


if __name__ == "__main__":

	input_list = get_input_list_ints()
	print(recursive("COM", input_list, 0))

	# print (1 + 3 + False)



	# print(input_list)
	# state_machine = StateMachine(input_list)
	# state_machine.run()