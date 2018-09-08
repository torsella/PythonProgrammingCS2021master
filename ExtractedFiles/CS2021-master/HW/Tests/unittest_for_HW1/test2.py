import unittest

from hog import roll_dice, take_turn, select_dice, is_swap, play
from hog import make_averaged, max_scoring_num_rolls, max_scoring_num_rolls, always_roll, average_win_rate, bacon_strategy, swap_strategy, final_strategy
from dice import make_fair_dice, make_test_dice, four_sided , six_sided 



class Test_test1(unittest.TestCase):
 

    def test_make_averaged(self):
        dice = make_test_dice(4, 2, 5, 1)
        averaged_dice = make_averaged(dice, 1000)
        val = averaged_dice()
        self.assertEqual(val,3.0)

    def test_make_averaged(self):
        dice = make_test_dice(1, 6)
        val=  max_scoring_num_rolls(dice)
        self.assertEqual(val,1)


    def test_run_experiments(self):
        """Run a series of strategy experiments and report results."""
        if True:  # Change to False when done finding max_scoring_num_rolls
            six_sided_max = max_scoring_num_rolls(make_fair_dice(6),1000)
            print('Max scoring num rolls for six-sided dice:', six_sided_max)

        if True:  # Change to False when done finding max_scoring_num_rolls
            four_sided_max = max_scoring_num_rolls(make_fair_dice(4),1000)
            print('Max scoring num rolls for four-sided dice:', four_sided_max)

        if True:  # Change to True to test always_roll(3)
            print('always_roll(3) win rate:', average_win_rate(always_roll(3)))

        if True:  # Change to True to test always_roll(4)
            print('always_roll(4) win rate:', average_win_rate(always_roll(4)))


        if True:  # Change to True to test always_roll(5)
            print('always_roll(5) win rate:', average_win_rate(always_roll(5)))

        if True:  # Change to True to test always_roll(6)
            print('always_roll(6) win rate:', average_win_rate(always_roll(6)))

        if True:  # Change to True to test always_roll(7)
            print('always_roll(7) win rate:', average_win_rate(always_roll(7)))


        if True:  # Change to True to test always_roll(8)
            print('always_roll(8) win rate:', average_win_rate(always_roll(8)))



        if True:  # Change to True to test bacon_strategy
            print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

        if True:  # Change to True to test swap_strategy
            print('swap_strategy win rate:', average_win_rate(swap_strategy))

        if True:  # Change to True to test final_strategy
            print('final_strategy win rate:', average_win_rate(final_strategy))

if __name__ == '__main__':
    unittest.main()
