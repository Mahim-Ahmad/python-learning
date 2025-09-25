 #meta character

import re

pattern=r"colo..r"

if re.match(pattern,"colouar"):
    print("match")


pattern=r"^colo..r$"

if re.match(pattern,"colouar"):
    print("match")

pattern=r"a*"

if re.match(pattern,"acolouar"):
    print("match")

pattern=r"(ab)*"#0 ba akadik thaka

if re.match(pattern,"acolouar"):
    print("match")

pattern=r"a+"# akta ba tar besi thaka

if re.match(pattern,"colouar"):
    print("match")

pattern=r"a+b"#soro ab

if re.match(pattern,"acolouar"):
    print("match")

pattern=r"a*b"

if re.match(pattern,"acolouar"):
    print("match")

pattern=r"ice(-)cream"

if re.match(pattern,"icecream"):
    print("match")

pattern=r"ice(-)?cream"#0 or 0ne space 

if re.match(pattern,"icecream"):
    print("match")

pattern=r"a{1,3}$"#a use 1 to 3 time

if re.match(pattern,"icecream"):
    print("match")

