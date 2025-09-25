#creating modules

#from math import pow,sqrt,

#or from math import * 

#print(pow(2,3))


#user import

#from p40 import add




#regular expression

import re

pattern=r"colour"

if re.match(pattern,"red is a colour"):#frist string match korbe pattern ar comma ar  bitorer string
    print("match")

else:
    print("not match")


if re.search(pattern,"red is a colour"):#any position a string match korbe  pattern ar comma ar  bitorer string ar sathe colour ar col holew hobe
    print("match")

else:
    print("not match")


print(re.findall(pattern,"red is a colour"))# joto gula  match korbe tarr listt dekhabe
    

pattern=r"colour"
text="my fav colour is red"

match=re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())


