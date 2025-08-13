# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available


name = input("What is your name? ")
passes = int(input("How many passes do you want? "))
tokens = int(input("How many tokens do you want on your pass(es)? "))



print(f'Welcome {name}!')
print(f'You bought {passes} passes.')
print(f'You have {tokens} tokens per pass.')

