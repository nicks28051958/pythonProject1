import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атаковал {other.name} и нанёс {damage} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print(f"Начинается битва между {self.player.name} и {self.computer.name}!")
        while self.player.is_alive() and self.computer.is_alive():
            self.play_turn()
        self.declare_winner()

    def play_turn(self):
        # Случайный выбор, кто будет атаковать
        if random.choice([True, False]):
            self.player_turn()
        else:
            self.computer_turn()

    def player_turn(self):
        self.player.attack(self.computer)
        print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    computer_name = "Компьютер"
    game = Game(player_name, computer_name)
    game.start()
