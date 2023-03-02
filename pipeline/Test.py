# print("I am IRON MAN Testing the Misciles, in the pool of Stephan hawklings riding a rocket")
#!/usr/bin/python3

#Test case for 
import unittest

from Program1 import calcSum

class TestSum(unittest.TestCase):
  def test_list_init(self):
    ''' Test case to add 2 numbers '''
    data = [23,32]
    result = calcSum(data)
    self.assertEqual(result,55)
    
if __name__ == '__main__':
  unittest.main()
