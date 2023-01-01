import calendar
year=int(input("Enter a year: "))
year=calendar.isleap(year)
if year:
	print("It is a leap year")
else:
	print("It is not a leap year")
