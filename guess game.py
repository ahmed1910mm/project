def rg():
    if guess_count == 2:
        return "guess"
    else:
        return "guesses"

secret_word = "hey"
hint1 = "it starts with h"
hint2 = "it's a greeting"
hints = ["it starts with h", "it's a greeting"]
guess_count = 0
guess = ""
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        if guess != secret_word and guess_count == 1:
            print(f"You have {rg()} left.")
            print("Hint:", hint1)
        if guess != secret_word and guess_count == 2:
            print(f"You have {rg()} left.")
            print("Hint:", hint2)
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Sorry, you lose, the secret word is 'hey'")
else:
    print("Congratulations, you win!")
