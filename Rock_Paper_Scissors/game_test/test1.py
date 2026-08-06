import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Rock_Paper_Scissors import main
import unittest
class TestTextNode(unittest.TestCase):

    def test_rock(self):

        test_outcome = "rock"
        lose = main(test_outcome, "paper")
        self.assertEqual(False, lose)
        win = main(test_outcome, "scissors")
        self.assertEqual(True, win)
        draw = main(test_outcome, "rock")
        self.assertEqual(-1, draw)

    def test_paper(self):
    
        test_outcome = "paper"
        lose = main(test_outcome, "scissors")
        self.assertEqual(False, lose)
        win = main(test_outcome, "rock")
        self.assertEqual(True, win)
        draw = main(test_outcome, "paper")
        self.assertEqual(-1, draw)

    def test_scissors(self):
        
        test_outcome = "scissors"
        lose = main(test_outcome, "rock")
        self.assertEqual(False, lose)
        win = main(test_outcome, "paper")
        self.assertEqual(True, win)
        draw = main(test_outcome, "scissors")
        self.assertEqual(-1, draw)

if __name__ == "__main__":
    unittest.main()