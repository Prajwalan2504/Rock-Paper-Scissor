import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images=[rock,paper,scissor]
user_choice=int(input("What do you choose? 0 for rock,1 for paper or 2 for scissor.."))
if user_choice>=3:
    print("You chose a invalid no.!!!! ,You lose")
else: 
    print(game_images[user_choice])
    computer_choice=random.randint(0,2)
    print("Computer chose")
    print(game_images[computer_choice])
    if user_choice==0 and computer_choice==2:
        print("You win!!")
    elif computer_choice==0 and user_choice==2:
        print("You lose")
    elif computer_choice>user_choice:
        print("You win")
    elif user_choice>computer_choice:
        print("You win")
    elif user_choice==computer_choice:
        print("Its a draw")