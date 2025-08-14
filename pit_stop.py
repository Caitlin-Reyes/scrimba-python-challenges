# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
race_time = int(input("What was the total race time (in seconds)? "))
# 2. Ask how many pit stops were made.
pit_stops = int(input("How many pit stops were made? "))
# 3. Ask for the average pit stop duration (in seconds).
avg_pit = int(input("What was the average pit stop duration (in seconds)? "))
#
# Then:
# - Calculate the total pit stop time.
total_pit = pit_stops*avg_pit
print(f'Your total pit stop time is: {total_pit} seconds')
# - Calculate the percentage of the race spent in the pits.
time_in_pits = (total_pit/race_time)*100
# - Round the percentage to 2 decimal places.
rounded_time = round(time_in_pits, 2)
print(f'You spent {rounded_time}% of the race in the pits')

# Finally, print all of the following:
# - Total pit stop time in seconds (DONE)
# - Percentage of race time spent in pits (DONE)
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"
crew_cutoff = 5
if (rounded_time > crew_cutoff):
    print(f'You need a new pit crew.')
