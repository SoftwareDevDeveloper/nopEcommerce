import unittest
from test.customer.add_customer_test import AddCustomer
from test.customer.search_customer_test import SearchCustomer
from test.home.login_test import LoginTests

# get all tests from Assert together
testCase1 = unittest.TestLoader().loadTestsFromTestCase(AddCustomer)
testsCase2 = unittest.TestLoader().loadTestsFromTestCase(SearchCustomer)
testCase3 = unittest.TestLoader().loadTestsFromTestCase((LoginTests))

# create a test suite to combine all test cases
sanityTest = unittest.TestSuite([testCase1, testsCase2, testCase3])
unittest.TextTestRunner(verbosity=3).run(sanityTest)
