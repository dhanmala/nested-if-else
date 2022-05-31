\
\
exp_date=int(input("enter expire date"))
exp_month=int(input("enter expire month"))
exp_year=int(input("enter expire year"))
return_date=int(input("enter the return date"))
return_month=int(input("enter the return month"))
return_year=int(input("enter the return year"))
return_month==exp_month and return_year==exp_year
if return_date<=exp_date:
    print("no fine")
elif return_date>=exp_date:
    fine=15*(return_date-exp_date)
    print(fine) 
else:
    print("no charge")
return_month>=exp_month and return_year==exp_year
if return_month>=exp_month:
    fine=500*(return_month-exp_month)
    print(fine)
else:
    print("fine  charge:,10000")