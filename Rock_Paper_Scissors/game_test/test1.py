import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Rock_Paper_Scissors import game
import unittest
class TestTextNode(unittest.TestCase):

    def test_rock(self):

        test_outcome = "rock"
        lose = game(test_outcome, "paper")
        self.assertEqual(False, lose)
        win = game(test_outcome, "scissors")
        self.assertEqual(True, win)
        draw = game(test_outcome, "rock")
        self.assertEqual(-1, draw)

    def test_paper(self):
    
        test_outcome = "paper"
        lose = game(test_outcome, "scissors")
        self.assertEqual(False, lose)
        win = game(test_outcome, "rock")
        self.assertEqual(True, win)
        draw = game(test_outcome, "paper")
        self.assertEqual(-1, draw)

    def test_scissors(self):
        
        test_outcome = "scissors"
        lose = game(test_outcome, "rock")
        self.assertEqual(False, lose)
        win = game(test_outcome, "paper")
        self.assertEqual(True, win)
        draw = game(test_outcome, "scissors")
        self.assertEqual(-1, draw)

if __name__ == "__main__":
    unittest.main()