# Assignment 8 - Just for Fun
# CSC 110 - Section 03
# Justin Clark
# 3/12/2020

# https://canvas.northseattle.edu/courses/1871665/assignments/16999849?module_item_id=38896164

# open input file
file_input = open('WorldData2018.txt')

# data lists
countries = []
populations = []
landareas = []
population_densities = []

# process every line in the input file
for line in file_input:

    # get all comma positions
    commas = []
    for ch in range(len(line)):
        if line[ch] == ',':
            commas.append(ch)

    # use comma positions to extract data from line
    country = line[0:commas[0]]
    population = line[commas[0]+1:commas[1]]
    landarea = line[commas[1]+1:len(line)]

    # convert text of numbers to floats
    population = float(population)
    landarea = float(landarea.rstrip())

    # calculate population density
    population_density = population / landarea

    # fill data lists
    countries.append(country)
    populations.append(population)
    landareas.append(landarea)
    population_densities.append(population_density)

# get stats
countries_count = len(countries)
world_population = sum(populations)
most_populated = countries[populations.index(max(populations))]
least_populated = countries[populations.index(min(populations))]
most_landarea = countries[landareas.index(max(landareas))]
least_landarea = countries[landareas.index(min(landareas))]
most_dense = countries[population_densities.index(max(population_densities))]
least_dense = countries[population_densities.index(min(population_densities))]
average_density = sum(population_densities) / len(countries)

# population density data
densely_populated = []
sparsely_populated = []

# get index value of countries with high and low population_densities 
# save indexes to population density data lists
for i in range(len(population_densities)):
    if population_densities[i] > average_density * 2:
        densely_populated.append(i)
    if population_densities[i] < average_density * .01:
        sparsely_populated.append(i)

# print report
print(
    '-'*50+'\n'+\
    'Total Countries: {:,.0f}'.format(countries_count)+'\n'+\
    'World Population: {:,.0f}'.format(world_population)+'\n'+\
    'Most Populated Country: '+most_populated+'\n'+\
    'Least Populated Country: '+least_populated+'\n'+\
    'Country with Most Land Area: '+most_landarea+'\n'+\
    'Country with Least Land Area: '+least_landarea+'\n'+\
    'Country with Highest Population Density: '+most_dense+'\n'+\
    'Country with Lowest Population Density: '+least_dense+'\n'+\
    'Average Density of All Countries: {:,.0f}'.format(average_density)
)

# use indexes gathered in population density data lists
# to get corresponding country names
print('-'*50+'\nMost Densely Populated Countries: ')
for i in densely_populated:
    print(countries[i])
print('-'*50+'\nLeast Densely Populated Countries: ')
for i in sparsely_populated:
    print(countries[i])

# close input file
file_input.close()