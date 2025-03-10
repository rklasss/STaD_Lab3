import unittest
from game import Game

class TestGameCreation(unittest.TestCase):
    def test_game_instance(self):
        game = Game("TEST")
        self.assertIsNotNone(game)

class TestGameInitialization(unittest.TestCase):
    def test_masked_word_initialization(self):
        game = Game("PYTHON")
        self.assertEqual(game.get_masked_word(), "______")

class TestGameGuess(unittest.TestCase):
    def test_correct_guess(self):
        game = Game("PYTHON")
        game.guess('P')
        self.assertEqual(game.get_masked_word(), "P_____")

    def test_incorrect_guess(self):
        game = Game("PYTHON")
        result = game.guess('Z')
        self.assertFalse(result)
        self.assertEqual(game.get_masked_word(), "______")

    def test_win_condition(self):
        game = Game("HI")
        game.guess('H')
        game.guess('I')
        self.assertTrue(game.is_won())
   


if __name__ == '__main__':
    unittest.main()
