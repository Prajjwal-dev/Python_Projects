'''WAP to play the game Snake, Water, Gun Game with the computer
Snake (s) drinks Water (w) → Snake wins.
Water (w) douses Gun (g) → Water wins.
Gun (g) shoots Snake (s) → Gun wins.
'''
import random

# Function to determine who wins
def gameWin(comp, you):
    if comp == you:
        return None  # It's a tie
    elif comp == 's':  # If computer chose Snake
        if you == 'w':  # Water loses to Snake
            return False
        elif you == 'g':  # Gun beats Snake
            return True
    elif comp == 'w':  # If computer chose Water
        if you == 'g':  # Gun loses to Water
            return False
        elif you == 's':  # Snake beats Water
            return True
    elif comp == 'g':  # If computer chose Gun
        if you == 's':  # Snake loses to Gun
            return False
        elif you == 'w':  # Water beats Gun
            return True

print("Computer is choosing: Snake(s), Water(w), or Gun(g)...")
randNo = random.randint(1, 3)  # Randomly choose 1, 2, or 3 for comp
if randNo == 1:
    comp = 's'  # Snake
elif randNo == 2:
    comp = 'w'  # Water
elif randNo == 3:
    comp = 'g'  # Gun

# Get user's input and ensure it's valid
you = input("Your Turn: Snake(s), Water(w), or Gun(g)? ").lower()

# Check if user entered a valid option
if you not in ['s', 'w', 'g']:
    print("Invalid choice! Please choose Snake (s), Water (w), or Gun (g).")
else:
    a = gameWin(comp, you)  # Determine the winner

    # Output the result
    print(f"Computer chose {comp}")
    print(f"You chose {you}")

    if a == None:
        print("The game is a tie!")
    elif a:
        print("You Win!")
    else:
        print("You Lose!")
