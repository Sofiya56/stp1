import random

class GuessNumberGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def play_game(self):
        print("Комп'ютер загадав число від 1 до 100. Спробуйте вгадати!")

        while True:
            try:
                guess = int(input("Ваш варіант: "))
                self.attempts += 1

                if guess < self.secret_number:
                    print("Більше")
                elif guess > self.secret_number:
                    print("Менше")
                else:
                    print(f"Вітаю! Ви вгадали число {self.secret_number} за {self.attempts} спроб.")
                    break
            except ValueError:
                print("Будь ласка, введіть ціле число!")

# Запуск гри
if __name__ == "__main__":
    game = GuessNumberGame()
    game.play_game()

