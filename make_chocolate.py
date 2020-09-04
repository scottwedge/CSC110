
# We want make a package of goal kilos of chocolate. 
# We have small bars (1 kilo each) and big bars (5 kilos each). 
# Return the number of small bars to use, 
# assuming we always use big bars before small bars. 
# Return -1 if it can't be done.

def make_chocolate(small, big, goal):
  
    needed = goal - big * 5

    if needed > 0: return small
    elif needed == 0: return small
    elif needed < 0: return goal % 5
    else: -1

x = make_chocolate(4, 5, 9)

print(x)