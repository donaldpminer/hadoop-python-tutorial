from mrjob.job import MRJob
from mrjob.step import MRStep
import csv
import datetime

# EXERCISE:
#   Build a mapping of years of service to median salary on the baltimore data

# Here are some sample records:
# "Abbene,Anthony M",POLICE OFFICER TRAINEE,A99416,Police Department ,07/24/2013,$43999.00,$39686.95
# "Abbey,Emmanuel",CONTRACT SERV SPEC II,A40001,M-R Info Technology ,05/01/2013,$52000.00,$47019.75

# Here is what I'd like the output to look like:
# [Years of service], [median salary, count of people with this many years]
# e.g.,
#  ...
# 10	[45581, 480]
# 23	[62000, 121]
#  ...

# At the bottom of this file there is a number of TODO's that you need to fill in.
# Use the other mrjob examples to help figure out what you need to do!


# THESE FUNCTIONS ARE HERE TO HELP YOU OUT, DON'T CHANGE THEM

cols = 'Name,JobTitle,AgencyID,Agency,HireDate,AnnualSalary,GrossPay'.split(',')

# This function takes in the raw csv line from the baltimore data
# It returns a dictionary where the keys are the column names (see 'cols' above)
#   and the values are the stored values as strings
def parse_line(line_str):
    return dict(zip(cols, [ a.strip() for a in csv.reader([line_str]).next()]))

# This function takes in a string of the form 'MM/DD/YYYY'
# HireDate in the Baltimore salary data is of this form
# It returns the number of years ago (rounded down) that date was
def parse_HireDate(date_str):
    if date_str == '':
        return -1

    hd = datetime.datetime.strptime(date_str, '%m/%d/%Y')
    years = (datetime.datetime.now() - hd).days / 365

    return years

# This function takes the AnnualSalary and converts it to an integer
# In the Baltimore salary data, it is stored as "$53414.00"
def parse_AnnualSalary(salary_str):
    return int(float(salary_str.strip().strip('$')))

# This function returns the median from a list of integers
def median(list_of_ints):

    return sorted(list_of_ints)[len(list_of_ints)/2]

### END OF HELPER FUNCTIONS

############## EXERCISE STARTS HERE ###############


# TODO: Define a class that inherits off of MRJob
class SeniorityVsSalary(MRJob):
    # inside the class, TODO: define the mapper function
    def mapper(self, _, line):

        # inside the mapper function, TODO:
        #   1. parse the line from its current CSV form
        pl = parse_line(line)

        #   2. get the number of years of service based on HireDate
        years = parse_HireDate(pl['HireDate'])

        #   3. get the annual salary from AnnualSalary
        salary = parse_AnnualSalary(pl['AnnualSalary'])

        #   4. yield a key and a value
        yield years, salary


    # inside the class, TODO: define the reducer function
    def reducer(self, key, values):

        # inside the reducer function, TODO:
        #   1. convert the generator to a list (since we'll be doing stuff to the list)
        values = list(values)

        #   2. calculate the median of the list
        med = median(values)

        #   3. get the length of the list
        ll = len(values)

        #   4. yeild the information we need
        yield key, (med, ll)

        
# TODO: use .run() on the class you defined above
SeniorityVsSalary.run()
