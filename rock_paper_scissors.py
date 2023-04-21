
import random

rock = """

     ______________
----'    __________)
        (___________)
        (___________)
        (_________)
----.___(_______)
"""

paper = """

        ___________
-----'      _______)______
                    ______)
                    ________)
                    _______)
----._________________)

"""

scissors = """

        _____________
------'       _______)______
                 ___________)
            ________________)
            (______)
------'_____(_____)

"""

# print( f"{rock} '\n' {paper} '\n' {scissors} ")

game_images = [rock, paper, scissors]

chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[chose])

computer_chose = random.randint(0,2)

print(f"{game_images[computer_chose]}\n Computer chose :")
print(f"{game_images[chose]} \n You chose :")

if chose==0 and computer_chose==1:
    
    print("you lose")

elif chose==0 and computer_chose==2:
    
    print("You win")

elif chose==1 and computer_chose==0:
   
    print("You win")

elif chose==1 and computer_chose==2:
    
    print("you lose")

elif chose==2 and computer_chose==0:
    
    print("You win")

elif chose==2 and computer_chose==1:
    
    print("you lose")

elif chose == computer_chose:
    
    print("Draws")

else:
    print("you type invalid number")
