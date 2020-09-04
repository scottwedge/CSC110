# Assignment 6 - Voter Participation Data
# CSC 110 - Section 03
# Justin Clark
# 2/29/2020 (leap year)

#  https://canvas.northseattle.edu/courses/1871665/assignments/16999845?module_item_id=38896161

import statistics as stats

def calc_percent(per, cent):
    """Takes the parameters "per" and "cent" 
    and returns the calculated percent."""
    return (per / cent) * 100

def test(file_name):
    """Takes the parameter "file_name" and 
    displays results from created as output to 
    that file and displays it into the console.
    """
    print('\nOutput file results:\n')
    read_output = open(file_name, 'r')
    for line in read_output:
        print(line.rstrip())
    read_output.close()

def main():
    """This is the main function of this program.
    It analyzes data from any given input file with 
    the correct format and creates a report in a 
    separate file plus another report in the console."""

    # get input file name from user
    file_name = input('Enter the name of a file to process: ')

    # open input file in read mode
    input_file = open(file_name, 'r')

    # open output file in write mode
    output_file = open('REPORT-'+file_name, 'w')

    # string variable to hold data to write to output file
    election_details = ''
  
    # create lists to store voting data
    years = []
    total_registered = []
    total_voted = []

    # variables for high and low voter turnout
    count_low_turnout = 0
    percent_high_turnout = 0

    # read the first line in the file
    line = input_file.readline().rstrip()

    # loop through all the lines in the file
    while line != '':

        # if the length of the line is 4 characters long it's a year (or a bad election!)
        if len(line) == 4: 

            # get the year
            year = int(line)

            # the next 3 lines go with the year
            eligible = float(input_file.readline().rstrip())
            registered = float(input_file.readline().rstrip())
            voted = float(input_file.readline().rstrip())

            # get the percent of eligible voters who registered
            registered_percent = calc_percent(registered, eligible)

            # fill data lists with election data
            years.append(year)
            total_registered.append(registered_percent)
            total_voted.append(voted)

            # get the percent of eligible voters who voted
            voted_percent = calc_percent(voted, eligible)

            # get the percent of registered voters who actually voted
            percent_registered_voted = calc_percent(voted, registered)

            # determine high and low voter turnout thresholds
            if percent_registered_voted < 60: count_low_turnout += 1
            if percent_registered_voted > 80: percent_high_turnout += 1 # <== value will later be used to calculate the percent

            # format data and save to variable for output file
            election_details += 'In '+str(year)+', '+\
                '{:.2f}'.format(registered_percent) +'% registered '+\
                'and {:.2f}'.format(voted_percent) +'% voted \n'

        # set the next line to read for the loop
        line = input_file.readline().rstrip()

    # get the length of the years list
    years = len(years)

    # use statistics module to calculate average (mean) of the total registered for each year
    average_registered = stats.mean(total_registered)

    # get the percent of years of high voter turnout
    percent_high_turnout = calc_percent(percent_high_turnout, years)

    # create election summary
    election_summary = '\n'+\
        'The total number of years listed: '+str(years)+'\n\n'+\
        'Total ballots cast in all these years: '+\
        '{:,.0f}'.format( sum(total_voted) )+'\n\n'+\
        'Average percentage of eligible voters registered: '+\
        '{:.2f}'.format( average_registered )+'%\n\n'+\
        'Number of years with less than 60% of registered voters casting ballots: '+\
        '{}'.format( count_low_turnout )+'\n\n'+\
        'Percentage of years with more than 80% of registered voters casting ballots: '+\
        '{:.1f}'.format( percent_high_turnout )+'\n\n'+\
        'An output file named '+ output_file.name +' has been created.'

    # write report to file
    output_file.write( election_details )
    
    # display report in the console
    print( election_summary )

    # close input and output files
    input_file.close()
    output_file.close()

    # call function to print the output report to the console
    test(output_file.name)

# call the program's main function
main()

# =================================================================================
# TEST CASES:
# ---------------------------------------------------------------------------------
# 
# Output created in external file by this program when processing the file
# PresidentialElections.txt, creates the exact same resuts as provided in
# the instructions for this assignment
# 
# In 1952, 90.81% registered and 72.80% voted
# In 1956, 89.45% registered and 71.75% voted
# In 1960, 87.10% registered and 71.73% voted
# In 1964, 85.15% registered and 68.73% voted
# In 1968, 83.53% registered and 66.38% voted
# In 1972, 85.64% registered and 65.91% voted
# In 1976, 81.12% registered and 62.24% voted
# In 1980, 74.75% registered and 57.58% voted
# In 1984, 77.24% registered and 60.70% voted
# In 1988, 73.14% registered and 56.28% voted
# In 1992, 73.72% registered and 60.89% voted
# In 1996, 74.68% registered and 55.65% voted
# In 2000, 76.37% registered and 57.62% voted
# In 2004, 75.51% registered and 62.09% voted
# In 2008, 72.45% registered and 61.30% voted
# In 2012, 74.79% registered and 60.77% voted
# In 2016, 76.83% registered and 60.52% voted
# 
# The total number of years listed: 17
# Total ballots cast in all these years: 34,436,792
# Average percentage of eligible voters registered: 79.55%
# Number of years with less than 60% of registered voters casting ballots: 0
# Percentage of years with more than 80% of registered voters casting ballots: 47.1
# An output file named REPORT-PresidentialElections.txt has been created.

# ---------------------------------------------------------------------------------
# The same exact results are also obtained by manually entering the same
# inputs into an Excel spreadsheet and plugging in the required calculations
# 
# year	eligible  registered  voted     %reg.   %voted  %reg-voted	rv>80%  rv<60%
# ----  --------  ----------  -------   -----   ------  ----------  -----   -----
# 1952	1533500	  1392594	  1116414	90.81	72.80	80.17	    80.17	
# 1956	1622500	  1451375	  1164104	89.45	71.75	80.21	    80.21	
# 1960	1753700	  1527510	  1257952	87.10	71.73	82.35	    82.35	
# 1964	1857900	  1582046	  1276956	85.15	68.73	80.72	    80.72	
# 1968	1975000	  1649734	  1310942	83.53	66.38	79.46		
# 1972	2306000	  1974849	  1519771	85.64	65.91	76.96		
# 1976	2546000	  2065378	  1584590	81.12	62.24	76.72		
# 1980	2992000	  2236603	  1722904	74.75	57.58	77.03		
# 1984	3182000	  2457667	  1931546	77.24	60.70	78.59		
# 1988	3417000	  2499309	  1923043	73.14	56.28	76.94		
# 1992	3818000	  2814680	  2324907	73.72	60.89	82.60	    82.60	
# 1996	4122000	  3078208	  2293895	74.68	55.65	74.52		
# 2000	4368000	  3335714	  2517028	76.37	57.62	75.46		
# 2004	4646000	  3508208	  2884783	75.51	62.09	82.23	    82.23	
# 2008	5010844	  3630118	  3071587	72.45	61.30	84.61	    84.61	
# 2012	5221125	  3904959	  3172930	74.79	60.77	81.25	    81.25	
# 2016	5557921	  4270270	  3363440	76.83	60.52	78.76		
# ----                        -------   -----                       -----   -----
# count                       sum       avg.                        count   count
# ----                        -------   -----                       -----   -----
#   17                		 34436792	79.55                           8	    0
# ---------------------------------------------------
# avg months of over 80% turnout: 17 / 8 * 100 = 47.1
# =================================================================================

# =================================================================================
# Without any "official" results, I reviewed the results of my program using
# the MidTermElections.txt file against the same inputs I entered manually into
# my Excel spreadsheet.  Here are the results of the output from my program,
# everything looks good and matches the results from my spreadsheet.
# 
# In 1958, 80.73% registered and 57.44% voted
# In 1962, 79.77% registered and 53.58% voted
# In 1966, 78.74% registered and 52.80% voted
# In 1970, 75.21% registered and 54.04% voted
# In 1974, 78.39% registered and 43.18% voted
# In 1978, 73.97% registered and 38.81% voted
# In 1982, 67.51% registered and 45.04% voted
# In 1986, 67.44% registered and 41.07% voted
# In 1990, 60.96% registered and 37.33% voted
# In 1994, 72.41% registered and 43.34% voted
# In 1998, 73.28% registered and 45.56% voted
# In 2002, 71.03% registered and 40.02% voted
# In 2006, 67.71% registered and 43.71% voted
# In 2010, 69.93% registered and 49.82% voted
# In 2014, 72.95% registered and 39.51% voted
# 
# The total number of years listed: 15
# Total ballots cast in all these years: 22,538,062
# Average percentage of eligible voters registered: 72.67%
# Number of years with less than 60% of registered voters casting ballots: 5
# Percentage of years with more than 80% of registered voters casting ballots: 0.0
# An output file named REPORT-MidTermElections.txt has been created.

# ---------------------------------------------------------------------------------
# And here is the out put from my spreadsheet.
# 
# year	eligible  registered  voted     %reg.   %voted  %reg-voted	rv>80%  rv<60%
# ----  --------  ----------  -------   -----   ------  ----------  -----   -----
# 1958	1703200	  1375035	  978400	80.73	57.44	71.15	
# 1962	1813500	  1446593	  971706	79.77	53.58	67.17	
# 1966	1869400	  1472054	  987134	78.74	52.80	67.06	
# 1970	2078000	  1562916	  1123000	75.21	54.04	71.85	
# 1974	2419000	  1896214	  1044425	78.39	43.18	55.08	            55.08
# 1978	2651000	  1960900	  1028854	73.97	38.81	52.47	            52.47
# 1982	3119000	  2105563	  1404831	67.51	45.04	66.72	
# 1986	3307000	  2230354	  1358160	67.44	41.07	60.89	
# 1990	3650000	  2225101	  1362651	60.96	37.33	61.24	
# 1994	4000000	  2896519	  1733471	72.41	43.34	59.85	            59.85
# 1998	4257000	  3119562	  1939421	73.28	45.56	62.17	
# 2002	4519000	  3209648	  1808720	71.03	40.02	56.35	            56.35
# 2006	4821000	  3264511	  2107370	67.71	43.71	64.55	
# 2010	5149729	  3601268	  2565589	69.93	49.82	71.24	
# 2014	5376986	  3922248	  2124330	72.95	39.51	54.16               54.16	
# ----                        -------   -----                       -----   -----
# count                       sum       avg                         count   count
# ----                        -------   -----                       -----   -----
#   15				         22538062  72.67			                0       5
# --------------------------------------------------
# avg months of over 80% turnout: 15 / 0 * 100 = 0.0
# =================================================================================
