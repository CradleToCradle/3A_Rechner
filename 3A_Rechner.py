# Ein einfacher Zinsrechner

import os
import datetime as dt
from decimal import Decimal



Today = int(dt.datetime.today().strftime("%Y"))
print('Today:', dt.datetime.today().strftime("%d/%m/%Y"))

Money = round(int(input('How much Money du you already have in your 3A Account?: ')))
Pay = round(int(input('How much Money do you pay yearly?: ')))
CompoundInterest = float(input('How much interest you get?: '))
Duration = int(input('How long until retirement in years?: '))
Interest = CompoundInterest
MoneyAfterInterest = Money


for Year in range (0, Duration +1):
    Today = Today + 1
    Interest = Money / 100 * CompoundInterest
    print('Money: %s' % Money)
    print('Interest: %s' % Interest)
    Money = round(Pay + (Money + Interest))
    print('Money including interest in Year: %s = %s' % (Today, Money,))



print('----------------------- Money without Interest -----------------------')
print('Total Interest: ' + ' $ ' , Interest * Year)

if CompoundInterest < 0.5:
    print('With this low interest rate, you are not going anywhere...')

print(dt.datetime.today().strftime("%m/%d/%Y"))

input('Press ENTER to exit')
