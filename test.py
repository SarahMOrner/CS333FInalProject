import unittest
from unittest.mock import patch
from finalproj import HangmanGame, HangmanDisplay

class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('requests.get')
        self.mock_get = self.patcher.start()
        self.mock_get.return_value.status_code = 200
        self.mock_get.return_value.json.return_value = ['python']

    def tearDown(self):
        self.patcher.stop()

    def test_get_random_word(self):
        game = HangmanGame()
        self.assertEqual(game.word, 'python')

    def test_display_word_initial(self):
        game = HangmanGame()
        game.guesses = set()
        self.assertEqual(game.display_word(), '______')

    def test_display_word_with_guesses(self):
        game = HangmanGame()
        game.guesses = {'p', 't', 'h', 'o'}
        self.assertEqual(game.display_word(), 'p_tho_')

    @patch('builtins.input', lambda *args: 'x')
    def test_make_guess_wrong(self):
        game = HangmanGame()
        game.make_guess()
        self.assertIn('x', game.guesses)
        self.assertEqual(game.attempts, 6)

    @patch('builtins.input', lambda *args: 'p')
    def test_make_guess_correct(self):
        game = HangmanGame()
        game.make_guess()
        self.assertIn('p', game.guesses)
        self.assertEqual(game.attempts, 7)

    def test_game_won(self):
        game = HangmanGame()
        game.guesses = {'p', 'y', 't', 'h', 'o', 'n'}
        self.assertTrue(game.is_word_guessed())

    def test_game_lost(self):
        game = HangmanGame()
        game.attempts = 0
        self.assertFalse(game.play())

class TestHangmanDisplay(unittest.TestCase):
    def test_initial_display(self):
        display = HangmanDisplay()
        self.assertEqual(len(display.stages), 7)

if __name__ == '__main__':
    unittest.main()
