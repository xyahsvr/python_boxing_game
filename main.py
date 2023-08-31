import random
import time

from colorama import Fore

# Define opponents' data
opponents = [
    {"health": 100, "name": "Jermimane Suckleding III", "damage": [5, 45]},
    {"health": 135, "name": "Christian Soro", "damage": [2, 30]},
    {"health": 75, "name": "Naum Angelevoski", "damage": [10, 60]}
]

# Initialize global variables
player_health = 100
current_opponent = 0


def check_player_health():
    """Check if the player's health reaches zero."""
    global player_health

    if player_health <= 0:
        print('You lose!!')
        time.sleep(1)
        print("You lost, leaving the arena...")
        time.sleep(1.5)
        input("Press enter to leave the arena: ")
        quit()


def check_opponent_health():
    """Check if the opponent's health reaches zero and update opponent."""
    global current_opponent, player_health

    if opponents[current_opponent]["health"] <= 0:
        if current_opponent < len(opponents) - 1:
            current_opponent += 1
            player_health = 100
            select_opponent()
        else:
            print("You win the championship!!")
            input("Leave the arena: ")
            quit()


def select_opponent():
    """Select the next opponent."""
    if not current_opponent >= len(opponents):
        print("Your opponent is...")
        time.sleep(1.5)
        print(opponents[current_opponent]["name"])
        time.sleep(0.5)


def countdown():
    """Display a countdown before the fight starts."""
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print("Fight!")


def player_damage():
    """Calculate damage dealt by the player."""
    return random.randint(5, 45)


def opponent_damage():
    """Calculate damage dealt by the opponent."""
    damage_range = opponents[current_opponent]['damage']
    return random.randint(damage_range[0], damage_range[1])


def player_turn():
    """Handle the player's turn."""

    # if current_opponent == len(opponents) - 1:
    #     return

    global player_health

    hit = input("1. Punch\n2. Block\n: ")

    if hit == "1":
        if random.randint(0, 100) < 20:
            damage_dealt = round(player_damage() * 1.35)
            print(Fore.LIGHTBLUE_EX + '\033[1m' + "You got a critical!" + '\033[0m')
        else:
            damage_dealt = player_damage()

        opponents[current_opponent]['health'] -= damage_dealt

        if opponents[current_opponent]['health'] > 0:
            print(Fore.LIGHTRED_EX + f"{opponents[current_opponent]['health']} HP left..." + Fore.RESET)
            time.sleep(2)
            opponent_dmg = opponent_damage()
            player_health -= opponent_dmg
            print(Fore.LIGHTGREEN_EX + f"You dealt {damage_dealt} damage to the opponent!" + Fore.RESET)
            print(f"You've been hit for {opponent_dmg}!")
            print(Fore.LIGHTRED_EX + f"You have {0 if player_health < 0 else player_health} health..." + Fore.RESET)
            check_player_health()
        else:
            check_opponent_health()
    elif hit == "2":
        player_health -= random.randint(5, 20)
        print(Fore.LIGHTRED_EX + f"You have {0 if player_health < 0 else player_health} health..." + Fore.RESET)
        check_player_health()


def main():
    select_opponent()
    countdown()
    print("Your Turn!")

    while True:
        if current_opponent == len(opponents):
            break
        else:
            player_turn()

    print("You Win!!!")


if __name__ == "__main__":
    main()
