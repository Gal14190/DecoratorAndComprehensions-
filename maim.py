import unittest

class Q1:
    def run():
        pass

class Q2:
    def run():
        pass

class Q3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(self.composeStr(['a','h','f','e','y','u'] , [1,5,3,6,2,4])
                                        , "ayfuhe")
    def test_2(self):
        self.assertEqual(self.composeStr(['n','h','t','y','p','o'] , [5,4,3,2,6,1])
                                        , "python")

    def composeStr(self, L1, L2):
        return "".join([L1[index - 1] for index in L2])
        

class Q4(unittest.TestCase):
    def test_1(self):
        self.assertEqual(self.composeLst([(4,9),(0,2),(1,4),(3,2)])
                                        , [2,4,-1000,2,9])

    def test_2(self):
        self.assertEqual(self.composeLst([(3,1),(5,2),(1,3),(4,4)])
                                        , [-1000, 3, -1000, 1, 4, 2])

    def composeLst(self, L):
        return [([value for indexTuple, value in L if indexTuple == indexList] + [-1000])[0] for indexList in range(max([i for i, x in L])+1)]

if __name__ == "__main__":
    
    Q1.run()
    Q2.run()
    

    unittest.main()