import unittest

#GLOBALS
#=======
FIRST_IDX = 0

class TestBinarySearch(unittest.TestCase):
	def test_binary_search(self):
		self.assertEqual(-1,binary_search([1,2,3],0))
		self.assertEqual(0,binary_search([1,2,3],1))
		self.assertEqual(2,binary_search([1,2,3],3))
		self.assertEqual(2,binary_search([1,2,2,2,3],2))
		
	
	def test_binary_search_min_idx(self):
		self.assertEqual(-1,binary_serach_min_idx([1,2,3],0))
		self.assertEqual(1,binary_serach_min_idx([1,2,2,2,3],2))
		self.assertEqual(3,binary_serach_min_idx([3,2,17,34,34,56],34))
		self.assertEqual(5,binary_serach_min_idx([3,2,17,34,34,56],56))

	def test_binary_search_max_idx(self):
		self.assertEqual(-1,binary_serach_max_idx([1,2,3],0))
		self.assertEqual(3,binary_serach_max_idx([1,2,2,2,3],2))
		self.assertEqual(4,binary_serach_max_idx([3,2,17,34,34,56],34))
		self.assertEqual(5,binary_serach_max_idx([3,2,17,34,34,56],56))



		
def binary_search_rec(sorted_list, element,real_start_idx,real_end_idx):
	if len(sorted_list) == 0:
		return -1
	
	middle_idx = (len(sorted_list)-1)/2
	real_middle_idx = (real_start_idx+real_end_idx)/2
	current_element = sorted_list[middle_idx]
	if current_element == element:
		return real_middle_idx
	elif current_element > element:
		return binary_search_rec(sorted_list[:middle_idx],element,real_start_idx,real_middle_idx-1)
	elif current_element < element:
		return binary_search_rec(sorted_list[middle_idx+1:],element,real_middle_idx+1,real_end_idx)
	
	
def binary_search(sorted_list, element)	:
		return binary_search_rec(sorted_list,element,0,len(sorted_list)-1)
		
def binary_serach_min_idx_rec(sorted_list, element,real_start_idx,real_end_idx):
	if len(sorted_list) == 0:
		return -1
	#print "current list:", sorted_list
	middle_idx = (len(sorted_list)-1)/2
	#print "middle_idx is:",middle_idx
	real_middle_idx = (real_start_idx+real_end_idx)/2
	#print "real_middle_idx:", real_middle_idx
	current_element = sorted_list[middle_idx]
	#print "current_element:", current_element
	if current_element == element:
		if  middle_idx== 0 or sorted_list[middle_idx-1] != element:
			return real_middle_idx
		#search minimum index
		else:
			return binary_serach_min_idx_rec(sorted_list[:middle_idx],element,real_start_idx,real_middle_idx-1)
	
	#check left side
	elif current_element > element: 
		return binary_serach_min_idx_rec(sorted_list[:middle_idx],element,real_start_idx,real_middle_idx-1)
	#check right side
	elif current_element < element:
		#print "current is lower"
		return binary_serach_min_idx_rec(sorted_list[middle_idx+1:],element,real_middle_idx+1,real_end_idx)
		

	
	
	return
	
def binary_serach_min_idx(sorted_list, element):
	return binary_serach_min_idx_rec(sorted_list, element,0,len(sorted_list)-1)
	
def binary_serach_max_idx_rec(sorted_list, element,real_start_idx,real_end_idx):
	if len(sorted_list) == 0:
		return -1
	#print "current list:", sorted_list
	middle_idx = (len(sorted_list)-1)/2
	#print "middle_idx is:",middle_idx
	real_middle_idx = (real_start_idx+real_end_idx)/2
	#print "real_middle_idx:", real_middle_idx
	current_element = sorted_list[middle_idx]
	#print "current_element:", current_element
	if current_element == element:
		if  middle_idx== 0 or sorted_list[middle_idx+1] != element:
			return real_middle_idx
		#search maximum index
		else:
			return binary_serach_max_idx_rec(sorted_list[middle_idx+1:],element,real_middle_idx+1,real_end_idx)
	
	#check left side
	elif current_element > element: 
		return binary_serach_max_idx_rec(sorted_list[:middle_idx],element,real_start_idx,real_middle_idx-1)
	#check right side
	elif current_element < element:
		#print "current is lower"
		return binary_serach_max_idx_rec(sorted_list[middle_idx+1:],element,real_middle_idx+1,real_end_idx)
		
def  binary_serach_max_idx(sorted_list, element):
	return binary_serach_max_idx_rec(sorted_list, element,0,len(sorted_list)-1)

def get_freq(sorted_list, element):
	if element not in sorted_list:
		return 0
	
	#element is in list, do binary search to find some index of it		

  
  
if __name__ == "__main__":
	unittest.main()
