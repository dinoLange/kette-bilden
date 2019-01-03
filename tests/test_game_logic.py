import unittest

from game.game_logic import get_random_dice_numbers

class RandomDiceTestCases(unittest.TestCase):

    def test_range(self):
        dices = get_random_dice_numbers()
        for i in range(0, 100):
            self.assertTrue(dices[0] > 0, "dice numbers must be greater than 0")
            self.assertTrue(dices[1] > 0, "dice numbers must be greater than 0")

            self.assertTrue(dices[0] <= 6, "dice numbers must be less than or equal to 6")
            self.assertTrue(dices[1] <= 6, "dice numbers must be less than or equal to 6")

