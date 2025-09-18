#queue

from collections import deque

bank=deque(["mahim","tamim","mahin"])

bank.popleft()
print(bank)

if not bank:
    print("empty")