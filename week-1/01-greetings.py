# Asks the user to input their name and their favorite number.
# Stores the inputs in variables of appropriate types.
# Creates a list of greetings: ["Hello", "Hi", "Hey", "Greetings"].
# Selects a greeting based on the user's favorite number (use the remainder when dividing the number by the list length).
# Prints the selected greeting followed by the user's name, formatted like:
# 	Hey Alex! It's nice to meet you.



print("I am a Greeting Generator")

# Ask for user name
name = input("Enter your name: ")

# Ask for user favourite number and convert to integer
fav_number = int(input("Enter your favourite number: "))

# List of greetings
greetings = ["Hello", "Hi", "Hey", "Greetings"]
    
# Select greeting based on the favorite number
selected_greeting = greetings[fav_number % len(greetings)]

# Print the final greeting
print(f"{selected_greeting} {name}! It's nice to meet you.")
