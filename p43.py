#scarch and replace

import re

pattern=r"colour"
text="my fav colour is red"

text2=re.sub(pattern,"color",text)

print(text2)

pattern=r"colour"
text="my fav colour is red,colour is colour"

text2=re.sub(pattern,"color",text,count=3)

print(text2)