import unittest

#GLOBALS
#=======
FIRST_IDX = 0

class TestBinarySearch(unittest.TestCase):
	def test_chop_itr(self):
		self.assertEqual(-1, chop_itr(3, []))
		self.assertEqual(-1, chop_itr(3, [1]))
		self.assertEqual(0,  chop_itr(1, [1, 3, 5]))
		self.assertEqual(1,  chop_itr(3, [1, 3, 5]))
		self.assertEqual(2,  chop_itr(5, [1, 3, 5]))
		self.assertEqual(-1, chop_itr(0, [1, 3, 5]))
		self.assertEqual(-1, chop_itr(2, [1, 3, 5]))
		self.assertEqual(-1, chop_itr(4, [1, 3, 5]))
		self.assertEqual(-1, chop_itr(6, [1, 3, 5]))
		self.assertEqual(0,  chop_itr(1, [1, 3, 5, 7]))
		self.assertEqual(1,  chop_itr(3, [1, 3, 5, 7]))
		self.assertEqual(2,  chop_itr(5, [1, 3, 5, 7]))
		self.assertEqual(3,  chop_itr(7, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_itr(0, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_itr(2, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_itr(4, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_itr(6, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_itr(8, [1, 3, 5, 7]))
		
	def test_chop_recursive(self):
		self.assertEqual(-1, chop_recursive(3, []))
		self.assertEqual(-1, chop_recursive(3, [1]))
		self.assertEqual(0,  chop_recursive(1, [1, 3, 5]))
		self.assertEqual(1,  chop_recursive(3, [1, 3, 5]))
		self.assertEqual(2,  chop_recursive(5, [1, 3, 5]))
		self.assertEqual(-1, chop_recursive(0, [1, 3, 5]))
		self.assertEqual(-1, chop_recursive(2, [1, 3, 5]))
		self.assertEqual(-1, chop_recursive(4, [1, 3, 5]))
		self.assertEqual(-1, chop_recursive(6, [1, 3, 5]))
		self.assertEqual(0,  chop_recursive(1, [1, 3, 5, 7]))
		self.assertEqual(1,  chop_recursive(3, [1, 3, 5, 7]))
		self.assertEqual(2,  chop_recursive(5, [1, 3, 5, 7]))
		self.assertEqual(3,  chop_recursive(7, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_recursive(0, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_recursive(2, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_recursive(4, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_recursive(6, [1, 3, 5, 7]))
		self.assertEqual(-1, chop_recursive(8, [1, 3, 5, 7]))

def chop_itr(number, int_list):
	list_size = len(int_list)
	start_idx = FIRST_IDX
	end_idx = list_size-1
	current_idx = end_idx/2
	itr_counter = list_size
	while itr_counter>0:
		current_value = int_list[current_idx]
		if current_value == number:
			return current_idx
		elif current_value > number:
			end_idx = current_idx - 1
		elif current_value < number:
			start_idx = current_idx+1

		current_idx = (end_idx + start_idx)/2
		itr_counter /=2
		
	return -1
			
def chop_recursive(number,int_list):
	return helper(number,int_list,0,len(int_list)-1)

def helper(number,int_list,start,end):
	if len(int_list) == 0:
                return -1
        else:
                list_size = len(int_list)
                start_idx = FIRST_IDX
                end_idx = list_size-1
                current_idx = end_idx/2
		real_idx = (start+end)/2
                current_value = int_list[current_idx]
                if current_value == number:
                        return real_idx 
                elif current_value > number:
                        return helper(number,int_list[:current_idx],start,real_idx-1)
                elif current_value < number:
                        return helper(number,int_list[current_idx+1:],real_idx+1,end)
		
	
  
  
if __name__ == "__main__":
	unittest.main()

