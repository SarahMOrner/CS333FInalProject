#Sarah Ornerrrr
import requests

class HangmanGame:
    def __init__(self):
        self.word = self.get_random_word()
        if self.word is None:
            print("Failed to get a word from the API, please check your connection.")
            return
        self.guesses = set()
        self.attempts = 7
        self.display = HangmanDisplay()

    def get_random_word(self):
        url = "https://random-word-api.herokuapp.com/word?number=1"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()[0]
        except requests.RequestException:
            return None

    def display_word(self):
        return ''.join([char if char in self.guesses else '_' for char in self.word])

    def make_guess(self):
        guess = input('Guess a letter: ').lower()
        if guess in self.guesses:
            print("You already guessed that letter.")
            return
        self.guesses.add(guess)
        if guess not in self.word:
            self.attempts -= 1
            print("Wrong guess. Attempts remaining:", self.attempts)
        self.display.display(self.attempts)

    def is_word_guessed(self):
        return all(char in self.guesses for char in self.word)

    def play(self):
        while self.attempts > 0:
            print(self.display_word())
            self.make_guess()
            if self.is_word_guessed():
                print("Congratulations! You guessed the word:", self.word)
                break
        else:
            print("Out of attempts! The word was:", self.word)

class HangmanDisplay:
    def __init__(self):
        self.stages = [
            """
               ------
               |    |
               |
               |
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |    |
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   /
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |
            --------
            """
        ]

    def display(self, attempts_left):
        print(self.stages[len(self.stages) - attempts_left - 1])

if __name__ == '__main__':
    game = HangmanGame()
    if game.word:
        game.play()
