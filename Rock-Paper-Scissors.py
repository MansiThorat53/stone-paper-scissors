import random
print("Welcome to Rock Paper Scissors")
print("Rock=1  Paper=2  Scissor=3")
def game():
    user = int(input("Enter choice: "))
    computer = random.randint(1, 3)
    print("Computer chose:", computer)
    if user == computer:
        print("Draw")
        return 0
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):

        print("You Win")
        return 1
    else:
        print("Computer Wins")
        return 2
p1 = 0
p2 = 0
for i in range(3):
    result = game()
    if result == 1:
        p1 += 1
    elif result == 2:
        p2 += 1
print("\nFinal Score")
print("You =", p1)
print("Computer =", p2,"\n")
if p1 > p2:
    print("You Won Congrats")
elif p2 > p1:
    print("Computer Won")
else:
    print("Match Draw")