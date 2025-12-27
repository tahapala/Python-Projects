import random

def number_guessing_game():
    
    hidden_number = random.randint(0, 100)
    number_of_rights = 5
    
    print("--- Welcome to the number guessing game! ---")
    print("I chose a number between 0 and 100.")
    print(f"You have a total of {number_of_rights}. Good luck!\n")

    while number_of_rights > 0:
        try:
            
            guess = int(input(f"What is your guess? (Remaining rights: {number_of_rights}): "))
        except ValueError:
            print("Please enter only numbers!")
            continue

        if guess == hidden_number:
            print(f"🎉 Congratulations! You guessed the number correctly: {hidden_number}")
            break 
        elif guess < hidden_number:
            print("🔼 Say a BIGGER number.")
        else:
            print("🔽 Say a SMALLER number.")

        
        number_of_rights -= 1

    if number_of_rights == 0:
        print(f"\n😔 I'm sorry, your rights have expired. The number I'm holding is: {hidden_number}")

if __name__ == "__main__":
    number_guessing_game()