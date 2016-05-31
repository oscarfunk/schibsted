import sys
import unittest
from tests import login
from tests import logout
from tests import search
 
class Test_Suite(unittest.TestCase):
   
    def test_main(self):
         
        # suite of TestCases
        self.suite = unittest.TestSuite()
        self.suite.addTests([            
            unittest.defaultTestLoader.loadTestsFromTestCase(login.login),
            unittest.defaultTestLoader.loadTestsFromTestCase(search.search),
            unittest.defaultTestLoader.loadTestsFromTestCase(logout.logout),
                                 
            ])
        runner = unittest.TextTestRunner()
        runner.run (self.suite)
 
import unittest
if __name__ == "__main__":
    unittest.main()