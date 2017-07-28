import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_input_1_should_return_1(self):
        fizzbuzz = FizzBuzz()
        actual = fizzbuzz.say(1)
        expect = 1
        self.assertEqual(actual,expect)

    def test_input_3_should_return_Fizz(self):
        fizzbuzz = FizzBuzz()
        actual = fizzbuzz.say(3)
        expect = "Fizz"
        self.assertEqual(actual,expect)

    def test_input_5_should_return_Buzz(self):
        fizzbuzz = FizzBuzz()
        actual = fizzbuzz.say(5)
        expect = "Buzz"
        self.assertEqual(actual,expect)

    def test_input_15_should_return_FizzBuzz(self):
        fizzbuzz = FizzBuzz()
        actual = fizzbuzz.say(15)
        expect = "FizzBuzz"
        self.assertEqual(actual,expect)

class FizzBuzz():
    def say(self,number):
        return "Fizz"*(number%3==0) + "Buzz"*(number%5==0) or number
        # if(number==3):
        #     return "Fizz"
        # elif(number==5):
        #     return "Buzz"
        # elif(number==15):
        #     return "FizzBuzz"
        # else:
        #     return number

if __name__ == '__main__':
    unittest.main()
