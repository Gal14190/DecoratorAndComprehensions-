# Afeka college 2022
# Assignment 2
##
# Created at 15/12/2022
# Authors:  Gal Ashkenazi   (315566752)
#           Roy Vaygue      (318860848)
##

## import moduls
import unittest
import logging

## setup logger file
logging.basicConfig(filename='Logger.log', encoding='utf-8', level=logging.DEBUG)

'''
Solusion for Question 1
'''

def pep8(func):
    # put '_' and lower letter
    def changeLetter(char):
        if not char.isupper():
            return char

        return f"_{char.lower()}"

    # find caps letters and push '_' before
    def convertToLowCase(str):
        str = str[0].lower() + str[1:]   # make sure that the first letter is lower

        while not str.islower(): # continue until the string is lower case
            for i, c in enumerate(str):
                if c.isupper():
                    str = str[:i] + changeLetter(c) + str[1 + i:]
                    break

        return str

    def foo(*args, **kwargs):
        logging.info('pep8 function run')

        new_Kwargs = {}
        for key in kwargs:
            new_Key = convertToLowCase(key)
            new_Kwargs[new_Key] = kwargs[key]     # push the value into the new key

        logging.debug(f"original keys: {kwargs}\nnew Keys:  {new_Kwargs}")
            
        return func(*args, **new_Kwargs)    # call the original function

    return foo

@pep8
def f(x, foo_bar, stam, yet_another_silly_name):
    logging.info('f function (pep8) run')

    logging.debug(f"x: {x}, foo_bar: {foo_bar}, stam: {stam}, yet_another_silly_name: {yet_another_silly_name}")
    logging.debug(f"x * 1000 + foo_bar * 100 + stam * 10 +  yet_another_silly_name  = {x * 1000 + foo_bar * 100 + stam * 10 +  yet_another_silly_name }")

    return x * 1000 + foo_bar * 100 + stam * 10 +  yet_another_silly_name 


'''
Solusion for Question 2
'''

class Car:
    def __init__(self, description):
        logging.info(f'make new Car {description}')

        self._description = description 
    
    def description(self):
        return self._description
    
    def safety_rating(self):
        return 0

class SuperMini(Car):
    def description(self): # override   
        return super().description() + "(SuperMini)" 
    
    def safety_rating(self): # override
        return 1
 
class SUV(Car):
    def description(self): # override   
        return super().description() + "(SUV)"
    
    def safety_rating(self): #override
        return 2

## car decorator class
class CarDecorator(Car):
    _Car: Car = None

    def __init__(self, car: Car):
        logging.info(f'edit Car safety device: {car.description()}')

        self._Car = car

    def description(self): # override   
        return self._Car.description()
    
    def safety_rating(self): # override
        return self._Car.safety_rating()

class KeyLess(CarDecorator):
    def description(self): # override   
        logging.info(super().description() + " is keyless")

        return super().description() + " is keyless"

    def safety_rating(self): # override
        return self._Car.safety_rating() + 0

class ABS(CarDecorator):
    def description(self): # override 
        logging.info(super().description() + " with ABS")

        return super().description() + " with ABS"
    
    def safety_rating(self): # override
        return self._Car.safety_rating() + 2

class AEB(CarDecorator):
    def description(self): # override   
        logging.info(super().description() + " with AEB")

        return super().description() + " with AEB"
    
    def safety_rating(self): # override
        return self._Car.safety_rating() + 4

'''
Solusions & UnitTests
'''

class Q1(unittest.TestCase):
    def test_1(self):
        self.assertEqual(f(1, YetAnotherSillyName=2, stam=9, fooBar=4)
                            , 1492)
    def test_2(self):
        self.assertEqual(f(1, YetAnotherSillyName=3, Stam=9, fooBar=4)
                            , 1493)
    def test_3(self):
        self.assertEqual(f(1, 4, Stam=9, yetAnotherSillyName=3)
                        , 1493)
    def test_4(self):
        self.assertEqual(f(1, 4, 9, 3)
                        , 1493)
    def test_5(self):
        self.assertEqual(f(x=1, YetAnotherSillyName=3, Stam=9, fooBar=4)
                            , 1493)

class Q2(unittest.TestCase):
    def test_1(self):
        car1 = SuperMini("Scoda Fabia")
        car1 = KeyLess(car1)
        car1 = AEB(car1)

        self.assertEqual(car1.description()
                        , "Scoda Fabia(SuperMini) is keyless with AEB")
        self.assertEqual(car1.safety_rating()
                        , 5)

        # install ABS in the car
        car1 = ABS(car1)
        car1.description()

        self.assertEqual(car1.description()
                        , "Scoda Fabia(SuperMini) is keyless with AEB with ABS")
        self.assertEqual(car1.safety_rating()
                        , 7)
        
    def test_2(self):
        car1 = SUV("Mercedes EQE")
        car1 = KeyLess(car1)
        car1 = ABS(car1)

        self.assertEqual(car1.description()
                        , "Mercedes EQE(SUV) is keyless with ABS")
        self.assertEqual(car1.safety_rating()
                        , 4)

class Q3(unittest.TestCase):
    def test_1(self):
        self.assertEqual(self.composeStr(['a','h','f','e','y','u'] , [1,5,3,6,2,4])
                                        , "ayfuhe")
    def test_2(self):
        self.assertEqual(self.composeStr(['n','h','t','y','p','o'] , [5,4,3,2,6,1])
                                        , "python")

    def test_composeStr_empty(self):
        self.assertEqual(self.composeStr([], [])
                                        ,"")

    def test_composeStr_single(self):
        self.assertEqual(self.composeStr(['a'], [1])
                                        ,"a")

    def composeStr(self, L1, L2):
        return "".join([L1[index - 1] for index in L2])
        
class Q4(unittest.TestCase):
    def test_1(self):
        self.assertEqual(self.composeLst([(4,9),(0,2),(1,4),(3,2)])
                                        , [2,4,-1000,2,9])

    def test_2(self):
        self.assertEqual(self.composeLst([(3,1),(5,2),(1,3),(4,4)])
                                        , [-1000, 3, -1000, 1, 4, 2])
    
    def test_composeLst_empty(self):
        self.assertEqual(self.composeLst([])
                                        ,[])

    def test_composeLst_single(self):
        self.assertEqual(self.composeLst([(0, 1)])
                                        ,[1])

    def test_composeLst_multiple_same_index(self):
        self.assertEqual(self.composeLst([(0, 1), (0, 2), (0, 3)])
                                        ,[1])

    def composeLst(self, L):
        return [([value for indexTuple, value in L if indexTuple == indexList] + [-1000])[0] for indexList in range(max([i for i, x in L], default=-1)+1)]
        '''
        for indexList in range of the max index in the tuple
            for indexTuple, value in L
                if indexTuple == indexList
                    list[indexList] = [value]
        
        push to every columns the value -1000. 
            ex. [[2, -1000],[4, -1000],[-1000],[2, -1000],[9, -1000]]
        return the first column in every sub list
            ex. [2, 4, -1000, 2, 9]
        '''

if __name__ == "__main__":
    unittest.main()