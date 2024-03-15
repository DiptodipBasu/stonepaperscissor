import random
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
res=input("Enter your prompt : ").lower()
x=random.randint(0,2)
if x==1:
    comp=rock
elif x==0:
    comp=paper
else:
    comp=scissor        
print("Your choice : \n")
if res=="scissor":
    print(scissor)
elif res=="paper":
    print(paper)
else:
    print(rock)
if res==comp:
    print("Its a draw")
elif res=="scissor":
    if comp==rock:
        print("Computor chose : \n",rock)
        print("You loose")
    else:
        print("computor choose : \n",paper)
        print("You win")
elif res=="rock":
    if comp==paper:
        print("Computor chose : \n",paper)
        print("You loose")
    else:
        print("computor choose : \n",scissor)
        print("You win")      
elif res=="paper":
    if comp==rock:
        print("Computor chose : \n",rock)
        print("You win")
    else:
        print("computor choose : \n",scissor)
        print("You loose")        