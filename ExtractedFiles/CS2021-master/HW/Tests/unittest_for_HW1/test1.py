import unittest

from hog import roll_dice, take_turn, select_dice, is_swap, play
from dice import make_fair_dice, make_test_dice, four_sided , six_sided 



class Test_test1(unittest.TestCase):
    def test_roll_dice1(self):
        val = roll_dice(1,make_test_dice(4, 2, 1, 3))
        self.assertTrue(val ==4)

    def test_roll_dice2(self):
        val = roll_dice(2,make_test_dice(4, 2, 1, 3))
        self.assertTrue(val ==6)

    def test_roll_dice3(self):
        val = roll_dice(3,make_test_dice(4, 2, 1, 3))
        self.assertTrue(val ==1)

    def test_roll_dice4(self):
        val = roll_dice(4,make_test_dice(4, 2, 1, 3))
        self.assertTrue(val ==1)

    def test_take_turn1(self):
        val = take_turn(2, 0, make_test_dice(4, 6, 1))
        self.assertTrue(val==10)

    def test_take_turn2(self):
        val = take_turn(3, 0, make_test_dice(4, 6, 1))
        self.assertTrue(val==1)

    def test_take_turn3(self):
        val = take_turn(0, 35)
        self.assertTrue(val==6)

    def test_take_turn4(self):
        val = take_turn(0, 71)
        self.assertTrue(val==8)

    def test_take_turn5(self):
        val = take_turn(0, 7)
        self.assertTrue(val==8)

    def test_take_turn6(self):
        val = take_turn(0, 0)
        self.assertTrue(val==1)

    def test_take_turn7(self):
        val = take_turn(0, 9)
        self.assertTrue(val==10)

    def test_take_turn8(self):
        val = take_turn(2, 0, make_test_dice(6))
        self.assertTrue(val==12)

    def test_take_turn9(self):
        val = take_turn(0, 50)
        self.assertTrue(val==6)

    def test_select_dice1(self):
        val = select_dice(4, 24) 
        self.assertTrue(val == four_sided)

    def test_select_dice2(self):
        val = select_dice(16, 64)
        self.assertTrue(val == six_sided)

    def test_select_dice3(self):
        val = select_dice(0, 0) 
        self.assertTrue(val == four_sided)

    def test_select_dice4(self):
        val = select_dice(50, 80)
        self.assertTrue(val == six_sided)

    def test_is_swap1(self):
        self.assertTrue(is_swap(19, 91))

    def test_is_swap2(self):
        self.assertTrue(not is_swap(20, 40))

    def test_is_swap3(self):
        self.assertTrue(is_swap(41, 14))

    def test_is_swap4(self):
        self.assertTrue(not is_swap(23, 42))

    #def test_is_swap5(self):
    #    self.assertTrue(is_swap(55, 55))

    def test_is_swap6(self):
        self.assertTrue(is_swap(114, 41))


if __name__ == '__main__':
    unittest.main()
