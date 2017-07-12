#GLOBALS
#=======
FIRST_IDX = 0

def chop(number, int_list):
	list_size = length(int_list)
	start_idx = FIRST_IDX
	end_idx = list_size-1
	current_idx = end_idx/2
	itr_counter = list_size
	while itr_counter>0:
		current_value = int_list[current_idx]
			if current_value == number:
				return current_idx
			else if current_value > number:
				end_idx = current_idx - 1
			else if current_value < number:
				start_idx = current_idx+1

			current_idx = (end_idx + start_idx)/2
			itr_counter /=2
			
	if __name__=="__main__":
	
