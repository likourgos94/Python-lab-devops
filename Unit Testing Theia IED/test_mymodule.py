class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.


class TestAdd(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(add(2 , 4), 6) # test when 2 and 4 is given the output is 6.
        self.assertEqual(add(0,0), 0) # test when 0 and 0 is given as input the output is 0.
        self.assertEqual(add("hello", "world"), "helloworld") # test when strings "hello" and "world" is given the output is "helloworld"
        self.assertEqual(add(2.3,3.6), 5.9) #test when 2.3 and 3.6 is given as input the output is 5.9.
        self.assertEqual(add(2.3000,4.3000), 6.6) #test when 2.3000 and 4.3000 is given as input the output is 6.6.
        self.assertNotEqual(add(-2,-2), 0) #test when 2.3000 and 4.3000 is given as input the output is not 0.
        
unittest.main()