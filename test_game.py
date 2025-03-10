import unittest
from game import Game

class TestGameCreation(unittest.TestCase):
    def test_game_instance(self):
        game = Game("TEST")
        self.assertIsNotNone(game)

if __name__ == '__main__':
    unittest.main()
