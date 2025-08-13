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

# Let's say this arcade is small, so they only have one tier of pass available to buy. Each pass contains 90 tokens. One pass costs $45.00.

tokens_per_pass = 90
price_per_pass = 45.00

total_tokens = passes*tokens_per_pass
total_cost = passes*price_per_pass

# Each game in the arcade costs 7 tokens to play. 

games_available = total_tokens // 7




print(f"\nHere's your receipt summary: \n")
print(f'Customer Name: {name}')
print(f'You bought {passes} passes.')
print(f'You have {total_tokens} tokens total.')
print(f'Your total cost is: ${total_cost:.2f}')
print(f'You can play {games_available} games with this purchase.')

