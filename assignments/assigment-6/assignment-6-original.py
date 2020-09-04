# Assignment 6 - Retirement Planner - Part II
# CSC 110 - Section 03
# Justin Clark
# 2/29/2020 (leap year)

#  https://canvas.northseattle.edu/courses/1871665/assignments/16999845?module_item_id=38896161

def test(file_name):
    read_output = open(file_name, 'r')
    for line in read_output:
        print(line.rstrip())
    read_output.close()

def main():
    # file_name = input('Enter the name of a file to process: ')
    file_name = 'PresidentialElections.txt'

    input_file = open(file_name, 'r')
    output_file = open('REPORT-'+file_name, 'w')

    election_details = ''
    line_type = 1

    year = 0
    eligible = 0
    registered = 0
    voted = 0

    registered_percent = 0
    voted_percent = 0

    total_years = 0
    total_eligible = 0
    total_registered = 0
    total_voted = 0

    count_low_turnout = 0
    percent_high_turnout = 0

    percent_registered_voted = 0

    for line in input_file:

        line = line.rstrip()

        if line_type == 1:
            year = line
            total_years += 1

        elif line_type == 2:
            eligible = float(line)
            total_eligible += eligible

        elif line_type == 3:
            registered = float(line)
            registered_percent = (registered / eligible) * 100
            total_registered += registered_percent

        elif line_type == 4:
            voted = float(line)

            total_voted += voted

            voted_percent = (voted / eligible) * 100
            percent_registered_voted = (voted / registered) * 100
            
            if percent_registered_voted < 60: count_low_turnout += 1
            if percent_registered_voted > 80: 
                percent_high_turnout += 1

            election_details += 'In '+year+', '+\
                '{:.2f}'.format(registered_percent) +'% registered '+\
                'and {:.2f}'.format(voted_percent) +'% voted \n'

        line_type += 1
        if line_type == 5: line_type = 1

    average_registered = total_registered / total_years
    percent_high_turnout = (percent_high_turnout / total_years) * 100

    election_summary = '\n'+\
        'The total number of years listed: '+str(total_years)+'\n\n'+\
        'Total ballots cast in all these years: {:,.0f}'.format(total_voted)+'\n\n'+\
        'Average percentage of eligible voters registered: {:.2f}'.format(average_registered)+'%\n\n'+\
        'Number of years with less than 60% of registered voters casting ballots: {}'.format(count_low_turnout)+'\n\n'+\
        'Percentage of years with more than 80% of registered voters casting ballots: {:.1f}'.format(percent_high_turnout)+'\n\n'+\
        'An output file named '+output_file.name+' has been created.'

    output_file.write(election_details+election_summary)

    input_file.close()
    output_file.close()

    print('report file created')

    test(output_file.name)

main()
