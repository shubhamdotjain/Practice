
import datetime

def get_day(year):
	day = datetime.datetime(year,2,29).strftime("%A")
	return day

def get_print(year, day):
	print( "For Leap year " + str(year) + " day is " + str(day))

def get_day_of_leap_year(year):
	year = int(year)
	if (year%4)==0:
		day = get_day(year)
		get_print(year,day)

	elif (year%4)==1 or (year%4)==3:
		year = year + (year%4) - 2
		day = get_day(year)
		get_print(year,day)


	else:
		day1 = get_day(year + 2)
		get_print(year + 2, day1)

		day2 = get_day(year- 2)
		get_print(year - 2, day2)



year = raw_input("Enter year:")
try :
	get_day_of_leap_year(year)

except Exception as e:
	print e


