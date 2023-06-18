import random
import numpy as np
import matplotlib.pyplot as plt

def rand_pt(p1, p2, p3):
    s = np.random.uniform(0, 1, size=(1, 2))
    r1 = np.sqrt(s[0, 0])
    r2 = s[0, 1] * (1 - r1)
    x = (1 - r1) * p1[0] + r1 * (1 - r2) * p2[0] + r1 * r2 * p3[0]
    y = (1 - r1) * p1[1] + r1 * (1 - r2) * p2[1] + r1 * r2 * p3[1]
    return np.array([x, y])

def select(cum_probs, tri_pts):
    rand_p = random.random()
    for p in cum_probs:
        if rand_p<p:
            vertex = tri_pts[cum_probs.index(p)]
            return vertex

def move(pt, vertex):
    vec = (vertex - pt)/2
    return pt + vec

def hundred(tri_pts, pt, cum_probs):
    point = pt
    for i in range(100):
        vertex = select(cum_probs, tri_pts)
        next_pt = move(point, vertex)
        point = next_pt
        '''ax.scatter(point[0], point[1])
        print(vertex, point)'''

    return point

tri_x = np.array([19, 8, 23])
tri_y = np.array([11, 25, 22])
tri_pts = [(19, 11), (8, 25), (23, 22)]

probs = [0.5, 0.3, 0.2]
cumulative_probabilities = [sum(probs[:i + 1]) for i in range(len(probs))]

pt = rand_pt(tri_pts[0], tri_pts[1], tri_pts[2])
fig, ax = plt.subplots()

for _ in range(1000):
    point = hundred(tri_pts, pt, cumulative_probabilities)
    ax.scatter(point[0], point[1])
    pt = point

plt.savefig('un_equalprobs.jpg')
ax.clear()

probs = [1/3, 1/3, 1/3]
cumulative_probabilities = [sum(probs[:i + 1]) for i in range(len(probs))]

pt = rand_pt(tri_pts[0], tri_pts[1], tri_pts[2])
fig, ax = plt.subplots()

for _ in range(1000):
    point = hundred(tri_pts, pt, cumulative_probabilities)
    ax.scatter(point[0], point[1])
    pt = point

plt.savefig('equalprobs.jpg')
