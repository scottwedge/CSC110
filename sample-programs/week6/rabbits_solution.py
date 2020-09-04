# rabbits_solution.py
# Rabbits Lab -- One Possible Solution

# CSC 110
# Fall 2011

pop = 190                  # set the initial population value

for year in range(1,11):   # simulate the passage of 10 years
    if pop > 150:          # if pop at beginning of the year is > 150...
        pop -= 100         # take away 100 rabbits.
    pop *= 2               # population doubles over the rest of the year
    print('End of year ' + str(year) + ': population = ' + str(pop))

print('\nEnd of simulation.  The final population is ' + str(pop) + '.')
