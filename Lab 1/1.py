#predefined variables
cleaningrate=60
cavityrate=200
xrayrate=100
tax=15/100
discount1=5/100
discount2=10/100

#inputs
patient_name=str(input('Enter your Name:'))
cleaning=str(input('Was cleaning performed? (y/n):'))
if cleaning=="y":
    total=cleaningrate
else:
    total=0
cavity_filling=str(input('Was cavity-filling performed? (y/n):'))
if cavity_filling=="y":
    total=total+cavityrate
else:
    total = total
xray=str(input('Was X-Ray performed? (y/n):'))
if xray=="y":
    total=total+xrayrate
else:
    total=total

#calculations
totalwithtax= (total + (total*tax))
if totalwithtax > 300:
    billtotal=(totalwithtax-(totalwithtax*discount2))
elif totalwithtax > 200:
    billtotal=(totalwithtax-(totalwithtax*discount1))
else:
    billtotal=totalwithtax

#output
print('         Melanie Dental Clinic')
print('    * ----------------------------*')
print('    Receipt for patient name:',patient_name)
print('----------------------------------------------')
print('             subtotal:', total )
print('             tax:', totalwithtax-total)
print('----------------------------------------------')
print('             Total',billtotal)