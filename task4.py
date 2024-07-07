import random
selection = ["rock","paper","scissor"]
player_score = 0
computer_score = 0
turns_count = 0
maximum_turns = 5
def choose_winner(player,computer):
 global player_score,computer_score
 if player == computer:
      return "it's a tie"
 elif(player == "rock" and computer == "scissor") or \
      (player == "paper" and computer == "rock") or \
      (player == "scissor" and computer == "paper"):
          player_score += 1
          return ("You win this round")
 else:
      computer_score += 1
      return ("computer wins this round")
while turns_count < maximum_turns:
 player = input("Enter rock,paper,or scissor: ").lower()
 if player not in selection :
   print("Invalid")
   continue
 computer = random.choice(selection)
 print(f"Computer choose:{computer}")
 result=choose_winner(player,computer)
 print(result)
 turns_count += 1
 print(f"Score : You {player_score} - {computer_score} computer\n")
print("Game over")
if player_score > computer_score:
    print("you won the game")
elif player_score < computer_score:
    print("The computer won the game ")
else:
  print("It's a tie game")      
           
    
  