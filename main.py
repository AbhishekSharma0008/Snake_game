import random

'''
1 for Snake 
-1 for Water
0 for Gun
'''

# Computer randomly chooses
computer = random.choice([1, 0, -1])

# User input with better prompts
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

# Validate input
if youstr not in youDict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    # Display choices
    print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

    # Determine winner
    if computer == you:
        print("It's a draw!")
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win! 🎉")
    else:
        print("You lose! 😢")
