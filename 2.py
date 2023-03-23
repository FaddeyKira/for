from character import Character
from colorama import Fore

player1 = Character(name='Katy', health=70, damage=2, color = Fore.LIGHTRED_EX)
print(player1.get_stats())

player2 = Character(name='Ira', health=90, damage=1, color = Fore.LIGHTBLUE_EX)
print(player2.get_stats())

while player1.is_alive(True) and player2.is_alive(True):
    player1.attack(player2)
    player2.attack(player1)
    print(player1)
    print(player2)