class Game:
    """
    Класс для реализации логики игры "Поле чудес".
    Содержит загаданное слово и методы для обработки угадывания.
    """
    def __init__(self, secret_word):
        self.secret_word = secret_word.upper()
        self.guessed_letters = set()

    def get_masked_word(self):
        """Возвращает текущее состояние слова, где неотгаданные буквы заменены '_'."""
        return ''.join(letter if letter in self.guessed_letters else '_' for letter in self.secret_word)

    def guess(self, letter):
        """
        Обрабатывает попытку угадать букву.
        Если буква есть в слове, добавляет её в guessed_letters.
        Возвращает True, если буква угадана, иначе False.
        """
        letter = letter.upper()
        if letter in self.secret_word:
            self.guessed_letters.add(letter)
            return True
        else:
            return False

    def is_won(self):
        """Проверяет, что все буквы слова отгаданы."""
        return all(letter in self.guessed_letters for letter in self.secret_word)
