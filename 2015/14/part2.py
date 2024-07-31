import re

with open("./2015/14/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

total_time = 2503
reindeer = []

# setup class
class Reindeer(object):
    def __init__(self, name, speed, active_time, resting_time) -> None:
        self.name = name
        self.speed = int(speed)
        self.active_time = int(active_time)
        self.resting_time = int(resting_time)
        self.points = 0

    def __str__(self) -> str:
        return f"{self.name}, {self.points}" #{self.speed}, {self.active_time}, {self.resting_time}"

    def distance_travelled(self, time) -> int:
        periods = time // (self.active_time+self.resting_time)
        remaining = time - periods*(self.active_time+self.resting_time)
        return (self.speed*self.active_time)*periods + self.speed*min(self.active_time, remaining)


# setup loop
for line in lines:
    match = re.match(r'([A-Za-z]+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.', line)
    reindeer.append(Reindeer(*match.groups()))

# racing loop
for i in range(1, 2504):
    # get the distance per reindeer
    winner_dist = max(reindeer, key=lambda r: r.distance_travelled(i)).distance_travelled(i)

    # print(i, [(str(r), r.distance_travelled(i)) for r in reindeer])

    for rd in reindeer:
        if rd.distance_travelled(i) == winner_dist:
            rd.points += 1

print([str(r) for r in reindeer])
print(max(reindeer, key=lambda r: r.points))
