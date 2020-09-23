import unittest
from HW2_2018141 import minFunc
from HW2_2018141 import expression
from HW2_2018141 import same
from HW2_2018141 import dectobin
from HW2_2018141 import dectobinthree
from HW2_2018141 import dectobintwo
class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(4,'(0,1,2,3,4,5)d-'),'w`x`+w`y`')
		self.assertEqual(minFunc(4,'(0,1,2,3,4,5)d(6,7,8,9,10,11,12,13,14)'),'w`')
		self.assertEqual(minFunc(3,'(0,1,2,3)d(5,6)'),'w`')
		self.assertEqual(minFunc(3,'(0,5,6)d(1,2)'),'w`x`+x`y+xy`')
		self.assertEqual(minFunc(2,'(0,2)d-'),'x`')
		self.assertEqual(minFunc(2,'(0)d(1)'),'w`')
                
if __name__=='__main__':
	unittest.main()
