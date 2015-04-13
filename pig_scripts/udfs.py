from pig_util import outputSchema
import csv

@outputSchema('as:int')
def square(num):
    if num is None:
        return None
    return num ** 2


_cols = 'Name,JobTitle,AgencyID,Agency,HireDate,AnnualSalary,GrossPay'.split(',')

# This function takes in the raw csv line from the baltimore data
# It returns a dictionary where the keys are the column names (see 'cols' above)
#   and the values are the stored values as strings
def _parse_line(line_str):
    return dict(zip(_cols, [ a.strip() for a in csv.reader([line_str]).next()]))


@outputSchema('pay:int')
def extract_dollar(line):
    try:
        return int(float(_parse_line(line)['GrossPay'].strip().strip('$')))
    except KeyError:
        return -1
    except ValueError:
        return -2
