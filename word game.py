import random

# List of names to choose from
name_list = [
    "apple", "balloon", "cactus", "dance", "elephant", "fire", "garden", "house", "island", "jungle",
    "kangaroo", "lemon", "mountain", "night", "ocean", "pencil", "queen", "rabbit", "star", "tree",
    "umbrella", "volcano", "watermelon", "xylophone", "yellow", "zebra", "airplane", "bicycle", "chocolate", 
    "dog", "eggplant", "fish", "giraffe", "helicopter", "iguana", "jump", "king", "lion", "moon",
    "notebook", "owl", "pizza", "quiet", "rainbow", "snowflake", "turtle", "unicorn", "van", "window",
    "yawn", "alphabet", "baseball", "camera", "doctor", "envelope", "friend", "garden", "happiness", "ice",
    "juice", "koala", "leaf", "magic", "notebook", "orange", "penguin", "puzzle", "rocket", "school",
    "train", "underwater", "wizard", "x-ray", "yoga", "adventure", "chocolate", "discovery", "education",
    "frog", "heartbeat", "intelligence", "jellyfish", "knowledge", "lighthouse", "monkey", "observation", 
    "puzzle", "question", "robot", "science", "treasure", "universe", "vacation", "wonder", "yarn", 
    "zip", "angel", "balloon", "cloud", "dream"
]

lives = 6

# Select a random name from the list
rand_char = random.choice(name_list)

# Shuffle the letters of the selected name
shuffled_name = list(rand_char)  # Convert the name to a list of characters
random.shuffle(shuffled_name)  # Shuffle the list
shuffled_name = "".join(shuffled_name)  # Join the list back to a string for display

print(f"Shuffled name: {shuffled_name}")

# Create placeholders for the word
placeholders = "_" * len(rand_char)
print("Guess the name:", placeholders)

game_over = False
correct_letters = []

while not game_over:
    word_name = input("Enter your guess (or type 'hint' for a hint): ").lower() 

    # Provide a hint if the player requests it
    if word_name == "hint":
        for letter in rand_char:
            if letter not in correct_letters:
                correct_letters.append(letter) 
                break
        print(f"Hint: A letter in the word is '{letter}'")
        continue

    display = ""

    for letter in rand_char:
        if letter == word_name and letter not in correct_letters: 
            display += letter
            correct_letters.append(letter) 
        elif letter in correct_letters:
            display += letter  
        else:
            display += "_"

    print("Current word:", display)

    if word_name not in rand_char and word_name != "hint":
        lives -= 1
        print(f"Wrong guess! You have {lives} lives remaining.")
        if lives == 0:
            game_over = True
            print("You lose! The correct word was:", rand_char)

    if "_" not in display:
        game_over = True
        print(f"You win! The correct word was {rand_char}.")
