import random
def roll_dice():
    while True:
        input("Press Enter to roll the dice...")
        dice_value = random.randint(1, 6)
        print(f"You rolled a {dice_value}!")
        
        choice = input("Do you want to roll again? (y/n): ").lower()
        if choice != 'y':
            break

roll_dice()
