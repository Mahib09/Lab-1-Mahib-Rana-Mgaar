def displayResult(firstnumber,secondnumber,sign):
    if sign == '+':
        return firstnumber + secondnumber
    elif sign == '-':
        return firstnumber - secondnumber
    elif sign == '*':
        return firstnumber * secondnumber
    elif sign == '/':
        return firstnumber / secondnumber
    else:
        print ("I don't understand")
def takeInput():
    firstnumber =    int(input('Enter any number:'))
    secondnumber   =   int(input('Enter any number:'))
    sign=(input('Enter the operator (+,-,*,/)'))

    print(firstnumber, sign, secondnumber, "=",displayResult(firstnumber,secondnumber,sign) )

takeInput()