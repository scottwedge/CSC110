# Assignment 7 - Working with Lists
# CSC 110 - Section 03
# Justin Clark
# 3/11/2020

# DUE: 3/13 (Friday)

import statistics as stats

# takes a list of sales figures as a parameter and 
# returns the list with special formatting
def format_sales_figures(sales_figures):
    formated_data = '{'
    for figure in range(len(sales_figures)):
        formated_data += '${:.2f}'.format(sales_figures[figure])
        if figure < len(sales_figures) - 1:
            formated_data += ', '
    formated_data += '}'
    return formated_data

# takes a list of sales figures and 
# returns the maximum value in the list
def max2(sales_figures):
    highest = sales_figures[0]
    for figure in sales_figures:
        if figure > highest:
            highest = figure
    return highest

# takes a list of sales figures and 
# returns the minium value in the list
def min2(sales_figures):
    lowest = sales_figures[0]
    for figure in sales_figures:
        if figure < lowest:
            lowest = figure
    return lowest

# takes a list of sales figures and 
# returns the sum of all values in the list
def sum2(sales_figures):
    total = 0
    for figure in sales_figures:
        total += figure
    return total

# takes a list of sales figures and 
# returns the average value of the list
def average(sales_figures):
    return sum2(sales_figures) / len(sales_figures)

# takes a list of sales figures and a threshold value and
# returns a new list of all sales figures that meet or
# exceed the given threshold
def acceptable_sales_figures(threshold, sales_figures):
    acceptable_list = []
    for figure in sales_figures:
        if figure >= threshold:
            print('figure: '+str(figure)+', threshold: '+str(threshold))
            acceptable_list.append(figure)
    return acceptable_list

# main program function
def main():
    
    # list to hold sales figures
    sales_figures = []

    # input message
    message_prompt = 'Enter monthly sales amount (negative value to stop): '

    # get sales input from user and append first sales figure 
    sales_amount = float(input(message_prompt))

    # exit program if first value is negative
    if sales_amount > 0:
        sales_figures.append(sales_amount)
    else: return

    # continue getting sales figures until negative value entered
    while sales_amount > 0:
        sales_amount = float(input(message_prompt))

        # only add current value if greater than zero
        if sales_amount > 0:
            sales_figures.append(sales_amount)

    # output section
    print(format_sales_figures(sales_figures))

    print(max(sales_figures))
    print(max2(sales_figures))

    print(min(sales_figures))
    print(min2(sales_figures))

    print(sum(sales_figures))
    print(sum2(sales_figures))

    print(stats.mean(sales_figures))
    print(average(sales_figures))

    acceptable_threshold_value = float(input('Enter a sales threshold value: '))
    print(acceptable_sales_figures(acceptable_threshold_value, sales_figures))

main()

# =================================================
# Test Cases
# Program output matches all three test cases below
# Test cases verified with MS Excel 
# and built-in python functions
# Threshold function verified visually
# -------------------------------------------------
# 	    Test 1	Test 2	Test 3
#----------------------------- 
# 	    100	    111	    10
# 	    200	    222	    10
# 	    300	    333	    10
# 	    400	    444	    10
# 	    500	    555	    20
# 	    600	    666	    10
# 	    700	    777	    10
# 	    800	    888	    10
# 	    900	    999	    10
#-----------------------------
# max   900	    999	    20
# min	100	    111	    10
# sum	4500	4995	100
# avg   500	    555	    11.11111111
# =================================================