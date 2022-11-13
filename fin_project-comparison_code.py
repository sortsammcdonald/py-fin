# Incomplete code - this is not fully functional
# My intention here was to create a version
# of my American Express statement that had 
# fully entries for the month i.e. zero for 
# days with no spending, that I could then 
# use to compare with other similarly formated
# files.


from re import S
from tabnanny import check
import pandas as pd
import numpy as np

class compare:

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
        

    def check(self):
        if self.x < self.y:
            return -1
        else:
            return 1

class amend:

    def __init__(self,x,y,z) -> None:
        self.x = x
        self.y = y   
        self.z = z
        self.a = []

    def amend(self):
        if compare(self.x, self.y) == -1:
            return self.z
        else:
            while self.x < self.y:
               self.a.append(0)
            return self.a

    

class calender_month:    

    def __init__(self) -> None:
        days_in_month = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul':31, 'Aug':31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
        
        self.days_in_month = days_in_month

    def __str__(self) -> str:
        return '{}'.format(self.days_in_month)

class statement_month_AMEX:

    def __init__(self, statement) -> None:
        self.dates = pd.read_csv(statement, decimal=",").iloc[:,0]
        self.dates_unique = np.unique(np.array(self.dates))
        self.iso_month = str(self.dates_unique[0]).split("/")[1]

    def __str__(self) -> str:
        return '{}'.format(self.iso_month)
      

class month_compare:

    def __init__(self, statement) -> None:
        amex_month_conv = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec' }
        self.amex_month_conv = amex_month_conv
        self.total_days_year =  calender_month()
        self.amex_days = statement_month_AMEX(statement)
        self.month_conv = self.amex_month_conv[str(self.amex_days)]
        self.month_conv_days = self.total_days_year.days_in_month[self.month_conv]
        self.comp_days = compare(len(self.amex_days.dates_unique),self.month_conv_days)
        self.comp_result = self.comp_days.check()
        self.comp_vals = amend(self.month_conv_days, len(self.amex_days.dates_unique), self.amex_days.dates_unique)
        self.comp_vals2 = self.comp_vals.amend()
        
    

    def __str__(self) -> str:
        return '{}'.format(self.comp_vals2)

    
        

if __name__ == '__main__':
    year = calender_month()
    Feb_days = year.days_in_month['Feb']
    # You'll have to provide your own CSV file for this
    # to work
    amex_months = statement_month_AMEX(x)
    test = month_compare(x)
