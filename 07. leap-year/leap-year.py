year = int(input('Enter the year (Eg. 2026): '))

if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print(year, 'is a leap year.')
else: 
    print(year, 'is not a leap year.')
