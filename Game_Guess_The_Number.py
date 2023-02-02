import random

LOGO = """
   ____     _   _ U _____ u ____    ____          _____    _   _  U _____ u      _   _       _   _   __  __     ____  U _____ u   ____     
U /"___|uU |"|u| |\| ___"|// __"| u/ __"| u      |_ " _|  |'| |'| \| ___"|/     | \ |"|   U |"|u| |U|' \/ '|uU | __")u\| ___"|/U |  _"\ u  
\| |  _ / \| |\| | |  _|" <\___ \/<\___ \/         | |   /| |_| |\ |  _|"      <|  \| |>   \| |\| |\| |\/| |/ \|  _ \/ |  _|"   \| |_) |/  
 | |_| |   | |_| | | |___  u___) | u___) |        /| |\  U|  _  |u | |___      U| |\  |u    | |_| | | |  | |   | |_) | | |___    |  _ <    
  \____|  <<\___/  |_____| |____/>>|____/>>      u |_|U   |_| |_|  |_____|      |_| \_|    <<\___/  |_|  |_|   |____/  |_____|   |_| \_\   
  _)(|_  (__) )(   <<   >>  )(  (__))(  (__)     _// \\_  //   \\  <<   >>      ||   \\,-.(__) )(  <<,-,,-.   _|| \\_  <<   >>   //   \\_  
 (__)__)     (__) (__) (__)(__)    (__)         (__) (__)(_") ("_)(__) (__)     (_")  (_/     (__)  (./  \.) (__) (__)(__) (__) (__)  (__) 
"""
print(LOGO)
print("Welcome to the number guessing game!")
print("Guess the number between 1 and 100")
difficulty = input("Choose difficulty: type 'Easy' (10 chances) or 'Hard' (5 chances): ").lower()
number = random.randrange(1, 100)
end_of_game = False


def guess_the_number():
    global end_of_game
    print(f"You have {i} attempts remaining")
    guess = int(input("Make a guess:"))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("You guessed it! Congrats!!!")
        end_of_game = True


if difficulty == "easy":
    i = 10
    while i > 0 and end_of_game is False:
        guess_the_number()
        i = i - 1
    print(f"The number was {number}. End of the game.")
elif difficulty == "hard":
    i = 5
    while i > 0 and end_of_game is False:
        guess_the_number()
        i = i - 1
    print(f"The number was {number}. End of the game.")
else:
    print("There is no such difficulty. Please retry.")
