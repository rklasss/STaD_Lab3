class Game:
    def __init__(self, secret_word):
        self.secret_word = secret_word.upper()
        self.guessed_letters = set()

    def get_masked_word(self):
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.secret_word)

    def guess(self, letter):
        letter = letter.upper()
        if letter in self.secret_word:
            self.guessed_letters.add(letter)
            return True
        else:
            return False
