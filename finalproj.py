import requests

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word?number=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()[0]
    except requests.RequestException:
        return None

def display_word(word, guesses):
    return ''.join([char if char in guesses else '_' for char in word])

def game_loop():
    word = get_random_word()
    if word is None:
        print("Failed to get a word from the API, please check your connection.")
        return

    guesses = set()
    attempts = 7

    while attempts > 0:
        print(display_word(word, guesses))
        guess = input('Guess a letter: ').lower()

        if guess in guesses:
            print("You already guessed that letter.")
            continue

        guesses.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess. Attempts remaining:", attempts)

        if all(char in guesses for char in word):
            print("Congratulations! You guessed the word:", word)
            break
    else:
        print("Out of attempts! The word was:", word)

if __name__ == '__main__':
    game_loop()
