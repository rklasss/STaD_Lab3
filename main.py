from game import Game

def main():
    game = Game("PYTHON")
    print("Добро пожаловать в игру 'Поле чудес'!")
    
    while not game.is_won():
        print("Слово: ", game.get_masked_word())
        guess = input("Введите букву: ")
        if not guess:
            break
        if game.guess(guess):
            print("Угадали!")
        else:
            print("Нет такой буквы.")
    
    if game.is_won():
        print("Поздравляем, вы выиграли! Слово:", game.secret_word)
    else:
        print("Игра окончена.")

if __name__ == "__main__":
    main()
