import unittest
from game import Game

class TestGameCreation(unittest.TestCase):
    """
    Тестовый класс для проверки создания экземпляра игры.
    """

    def test_game_instance(self):
        """
        Проверяет, что при создании объекта Game он не равен None.
        Это базовый тест, демонстрирующий, что конструктор класса корректно создает экземпляр.
        """
        game = Game("TEST")
        self.assertIsNotNone(game)

class TestGameInitialization(unittest.TestCase):
    """
    Тестовый класс для проверки корректной инициализации маскированного слова.
    """

    def test_masked_word_initialization(self):
        """
        Проверяет, что после создания игры с заданным словом (например, "PYTHON")
        метод get_masked_word возвращает строку, состоящую из символов '_' длиной, равной количеству букв слова.
        """
        game = Game("PYTHON")
        self.assertEqual(game.get_masked_word(), "______")

class TestGameGuess(unittest.TestCase):
    """
    Тестовый класс для проверки метода угадывания буквы и выигрыша.
    """

    def test_correct_guess(self):
        """
        Проверяет, что при угадывании правильной буквы (например, 'P' для слова "PYTHON")
        метод guess возвращает True, а маскированное слово обновляется с учетом угаданной буквы.
        """
        game = Game("PYTHON")
        game.guess('P')
        self.assertEqual(game.get_masked_word(), "P_____")

    def test_incorrect_guess(self):
        """
        Проверяет, что при угадывании неправильной буквы (например, 'Z' для слова "PYTHON")
        метод guess возвращает False, а маскированное слово остается неизменным.
        """
        game = Game("PYTHON")
        result = game.guess('Z')
        self.assertFalse(result)
        self.assertEqual(game.get_masked_word(), "______")

    def test_win_condition(self):
        """
        Проверяет, что игра фиксирует победу (метод is_won возвращает True),
        когда все буквы загаданного слова отгаданы.
        Например, для слова "HI" угадывание букв 'H' и 'I' должно привести к победе.
        """
        game = Game("HI")
        game.guess('H')
        game.guess('I')
        self.assertTrue(game.is_won())

if __name__ == '__main__':
    unittest.main()
