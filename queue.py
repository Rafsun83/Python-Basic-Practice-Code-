from collections import deque

bank = deque(["rafsun", " azim", "faisal"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)

bank.popleft()
if not bank:
    print("no value")