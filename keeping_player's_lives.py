

import random

stages = [
    '''
    +---+
    |    |
    O    |
   /|\   |
   /  \  |
         |
   =========

    ''',
    '''
    +---+
    |    |
    O    |
   /|\   |
   /     |
         |
   =========
    ''',
    '''
    +---+
    |    |
    O    |
   /|\   |
         |
         |
   =========
    ''',
    '''
    +---+
    |    |
    O    |
   /|    |
         |
         |
   =========
    ''',
    '''
    +---+
    |    |
    O    |
   /     |
         |
         |
   =========
    ''',
    '''
    +---+
    |    |
    O    |
         |
         |
         |
   =========
    ''',
    '''
    +---+
    |    |
         |
         |
         |
         |
   =========
    ''',
    '''
    +---+
         |
         |
         |
         |
         |
   =========
    ''',
]

end_of_game = False
word_list = ["advark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_lengeh = len(chosen_word)

lives = 6

print(f'Passt, the solution is {chosen_word}')

display = []
for _ in range(word_lengeh):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ".lower())

    for position in range(word_lengeh):
        letter = chosen_word[position]
        # print(f"Current position : {position} \n Curret letter : {letter} \n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    # print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOu lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win.")

    print(stages[lives])
