
import random

word_list = ["advark", "baboon", "camel"]
 
chosen_word = random.choice(word_list)

print(f'Passst, the solutio is {chosen_word}.')

display = []
word_lengeh = len(chosen_word)
for letter in range(word_lengeh):
    display += "_"
print(display)

end_of_game = False
while not end_of_game: 
    guess = input("Guess a letter: ").lower()

    for position in range(word_lengeh):
        letter = chosen_word[position]
        # print(f"Current position : {position} \n Curret letter : {letter} \n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

