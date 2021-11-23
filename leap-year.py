# To get year (integer input) from the user
# This is my first explanation
year = int(input("Enter a year: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

        # Alternative Lösung

jahr = int(input('Geben Sie ein Jahr ein: '))

if jahr % 400 == 0 or (jahr % 400 != 0 and jahr % 100 != 0 and jahr % 4 == 0 ):
    print(f"{jahr} ist ein Schaltjahr")
else:
    print(f"{jahr} ist kein Schaltjahr")
