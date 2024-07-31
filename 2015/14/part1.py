import re

with open("./2015/14/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

total_time = 2503
reindeer = []

for line in lines:
    match = re.match(r'([A-Za-z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', line)

    name, speed, active_time, resting_time = match.groups()

    speed = int(speed)
    active_time = int(active_time)
    resting_time = int(resting_time)

    periods = total_time // (active_time+resting_time)
    remaining = total_time - periods*(active_time+resting_time)

    distance = (speed*active_time)*periods + speed*min(active_time, remaining)
    reindeer.append((name, distance))

print(max(reindeer, key=lambda x: x[1]))
