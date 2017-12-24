import collections
import operator
import sys

lines = [line.rstrip('\n') for line in open('in20.txt')]

class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

    def step(self):
        for i in xrange(3):
            self.velocity[i] += self.acceleration[i]
            self.position[i] += self.velocity[i]

    def distance(self, time):
        vt = [elem * time for elem in self.velocity]
        att = [elem * time * time for elem in self.acceleration]
        dist = map(operator.add, self.position, vt)
        dist = map(operator.add, dist, att)
        dist = [elem/2 for elem in dist]
        return sum([abs(elem) for elem in dist])

    def manhattan(self):
        return sum([abs(elem) for elem in self.position])

####### Part 1 #######
min_idx = 0
min_dist = sys.maxint
particles = dict()
for i in xrange(len(lines)):
    info = lines[i].strip().split(", ")
    position = [int(x) for x in info[0][3:-1].split(',')]
    velocity = [int(x) for x in info[1][3:-1].split(',')]
    accelation = [int(x) for x in info[2][3:-1].split(',')]
    particle = Particle(position, velocity, accelation)
    dist = particle.distance(100000)
    if dist < min_dist:
        min_dist = dist
        min_idx = i
    particles[i] = particle

print min_idx

####### Part 2 #######
while True:
    for i, particle in particles.iteritems():
        particle.step()

    # position -> list of indexes
    positions = collections.defaultdict(lambda : [])
    for i, particle in particles.iteritems():
        positions[tuple(particle.position)].append(i)

    for position, indexes in positions.iteritems():
        if len(indexes) > 1:
            for i in indexes:
                del particles[i]

    print len(particles)
