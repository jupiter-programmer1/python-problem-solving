print('1: Feet to Meters \n2: Meters to Feet \n')
choice = int(input('Enter Choice: '))

match choice:
    case 1:
        num = float(input('Enter number of feet: '))
        print('Meters:', round((num / 3.28), 3))
    case 2:
        num = float(input('Enter number of meters: '))
        print('Feet:', round((num * 3.28), 3))
    case _:
        print('Invalid choice! Please try again..')
