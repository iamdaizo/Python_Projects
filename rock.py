import random   
item_list = ["Rock", "Paper", "Scissors"]

computer_choice = random.choice(item_list)
user_choice = input("Enter your move = Rock, Paper, Scissors = ")

print(f"User choice = {user_choice}, Computer's choice = {computer_choice} ")

if user_choice == computer_choice:
    print("The result is tie, both chose same")

elif user_choice == "Rock":
   if computer_choice == "Paper":
    print("Paper covers Rock = Computer wins.. ")
   else:
    print("Rock smashes Scissors")
   
elif user_choice == "Paper":
  if computer_choice == "Scissors":
    print("Scissors cut paper = Computer wins...")
  else:
    print("Rock is covered by Paper = User wins...")

elif user_choice == "Scissors":
  if computer_choice == "Rock":
    print("Rock breaks the scissor = Computer wins...")
  else:
    print("Scissors cuts the paper = User wins..")


