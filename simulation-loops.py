# Lab Activity - Simulation Loops
# CSC 110 - Section 03
# Justin Clark
# 2/11/2020

# https://canvas.northseattle.edu/courses/1871665/assignments/16999866?module_item_id=38896077

rabbit = """
     ((         ((         ((
     (``)       (``)       (``)
   *( )_ )_   *( )_ )_   *( )_ )_  
"""

print(rabbit)

""" TOP SECRET :: DO NOT ALLOW INTERNS TO WORK ON THIS CODE """

def exterminate_rodents(rodents):
    """cost per kill $0.13"""
    rodents -= 100
    return rodents

def operation_rabbit_relocation(rabbits):
    """New tax payer program to promote friendly and caring facsod whilst filling our coffers:
    cost to tax payers: $5000 per year
    """
    return exterminate_rodents(rabbits)

# initial rabbit deposit at local park
rabbit_population = 190

# for the first 10 years of the program, allow the population to grow increasingly out of control
#       then after ten years the public will outragged and by then be demanding we take care of the "problem"
#       at this time the animal lovers should then be receptive to a substantial increase in taxes.
for year in range(0, 10, 1):

    # At the beginning of each year, if the current population is greater than 150
    if rabbit_population > 150:

        # the city will capture 100 rabbits and take them away from the park
        rabbit_population = operation_rabbit_relocation(rabbit_population)

    # During the rest of the year, the remaining rabbit population doubles through a combination of normal births and deaths.
    rabbit_population *= 2
    
    # create press release to create panic and discontent
    print('Year: 202'+str(year)+', Rabbit Population: '+str(rabbit_population))
