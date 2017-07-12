import unittest



#GLOBALS
#=======
FIRST_IDX = 0

class TestBinarySearch(unittest.TestCase):
	def test_chop(self):
		self.assertEqual(-1, chop(3, []))
		self.assertEqual(-1, chop(3, [1]))
		self.assertEqual(0,  chop(1, [1, 3, 5]))
		self.assertEqual(1,  chop(3, [1, 3, 5]))
		self.assertEqual(2,  chop(5, [1, 3, 5]))
		self.assertEqual(-1, chop(0, [1, 3, 5]))
		self.assertEqual(-1, chop(2, [1, 3, 5]))
		self.assertEqual(-1, chop(4, [1, 3, 5]))
		self.assertEqual(-1, chop(6, [1, 3, 5]))
		
		self.assertEqual(0,  chop(1, [1, 3, 5, 7]))
		self.assertEqual(1,  chop(3, [1, 3, 5, 7]))
		self.assertEqual(2,  chop(5, [1, 3, 5, 7]))
		self.assertEqual(3,  chop(7, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
		self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

def chop(number, int_list):
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
			

  
  
if __name__ == "__main__":
	unittest.main()
