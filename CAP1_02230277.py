#****************************************************************************
# Name: Ugyen Choeda 
# Department: Mechanocal Engineering 
# Student Id: 02230277
#*****************************************************************************
# Reference 
'''
1. https://youtu.be/OU1sHrjmbHw
2. https://youtu.be/ERCMXc8x7mc
3. https://youtu.be/0EgSo7hsRWM
'''
#*****************************************************************************
# Solution
# Solution Score: 50169
# Number: 7
#*****************************************************************************
# Function to read input from file
def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Read input from file
file_path = '/Users/Desktop/CAP1 Solution/input_7_cap1.txt'
lines = read_input(file_path)

# Initialize total score
total_score = 0

# Function to calculate score for each round
def calculate_score(my_choice, their_choice, outcome):
    choices = {'A': 1, 'B': 2, 'C': 3}
    results = {'X': 0, 'Y': 3, 'Z': 6}
    return choices[my_choice] + results[outcome]

# Iterate through each line
for line in lines:
    # Extract opponent's choice and result
    their_choice, outcome = line.strip().split()
    # Determine player's choice based on opponent's choice and result
    if their_choice == "A":
        my_choice = 'C' if outcome == "X" else ('A' if outcome == 'Y' else 'B')
    elif their_choice == "B":
        my_choice = 'A' if outcome == 'X' else ('B' if outcome == 'Y' else 'C')
    else:
        my_choice = 'B' if outcome == 'X' else ('C' if outcome == 'Y' else 'A')
    # Calculate round score
    round_score = calculate_score(my_choice, their_choice, outcome)
    # Add round score to total
    total_score += round_score

# Print total score
print("Total Score:", total_score)
