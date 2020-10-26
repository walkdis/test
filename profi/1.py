import random

before = []
after = []
# fill list
for i in range(random.randint(5, 15)):
    before.append(random.randint(1, 30))
print(before)

# Asymptotic complexity = O(n(n-1)/2)
for i in before:
    if i not in after:
        after.append(i)
print(after)
