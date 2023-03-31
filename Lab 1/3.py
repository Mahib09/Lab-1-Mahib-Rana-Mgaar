PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100
pennies=int(input('Enter the number of pennies:'))
nickel=int(input('Enter the number of pennies:'))
dimes=int(input('Enter the number of pennies:'))
quater=int(input('Enter the number of pennies:'))
totalcent=int(pennies*PENNY_VALUE+nickel*NICKEL_VALUE+dimes*DIME_VALUE+quater*QUARTER_VALUE)
totaldollar=int(totalcent / PENNIES_IN_DOLLAR)
if totaldollar>1.0:
    print ('“Sorry, the amount you entered was more than one dollar.”')
elif totaldollar<1.0:
    print ('“Sorry, the amount you entered was less than one dollar.”')
else:
    print("Congratulations! \nThe amount you entered was exactly one dollar! \nYou win the game!!")