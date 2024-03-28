import a1, unittest

class TestNumBuses(unittest.TestCase):
    #Test class for a1.num_buses

    def test_num_buses_zero_persons(self):
        #num_buses for 0 person: 0 person needs 0 buses
        act = a1.num_buses(0)
        expct = 0
        self.assertEqual(expct, act)

    def test_num_buses_one_person(self):
        #num_buses for 1 person
        act = a1.num_buses(1)
        expct = 1
        self.assertEqual(expct, act)

    def test_num_buses_fifty_persons(self):
        #num_buses for 50 persons
        act = a1.num_buses(50)
        expct = 1
        self.assertEqual(expct, act)
        
    def test_num_buses_fiftyone_persons(self):
        #num_buses for 51 persons
        act = a1.num_buses(51)
        expct = 2
        self.assertEqual(expct, act)

    def test_num_buses_fivehundred_persons(self):
        #num_buses for 555 persons
        act = a1.num_buses(555)
        expct = 12
        self.assertEqual(expct, act)

if __name__ == '__main__':
    unittest.main(exit=False)