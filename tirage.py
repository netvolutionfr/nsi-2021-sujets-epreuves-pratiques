import random
import json

sujets = list(range(1, 31))

with open('deja_tires.json', 'r') as f:
    try:
        dejatires = json.load(f)
    except:
        dejatires = []

k = random.randint(1, 31)
while k in dejatires:
    k = random.randint(1, 31)

dejatires.append(k)
dejatires.sort()

with open('deja_tires.json', 'wb') as f:
    json.dump(dejatires, f)

print(k)
