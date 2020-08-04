with open('data.txt') as f:
    a = f.readlines()
# print(a)
d = {}
for line in a:
    p = line.split("\t")
    d[p[0]] = p[1]
# print(d)
amt = int(input('Enter amount: '))
print('Available Currency Options):\n')
[print(item) for item in d.keys()]
print('\n')
c = input('Enter 1 from above: ')
try:
    print(f"{amt} INR = {amt * float(d[c])} {c}")
except KeyError:
    print('Please enter from available currency options.')





