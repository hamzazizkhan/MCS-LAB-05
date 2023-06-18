import numpy as np
from painter_play import painter_play
import random
import matplotlib.pyplot as plt

# reeturn a list of size 100 with avg_fit value for each chrs
def avg_fit_play(chrs, room):
    avg_fit_list = []
    for chr in chrs:
        fit_list = []
        for i in range(10):
            fit_list.append(painter_play(chr, room)[0])
        avg_fit_list.append(sum(fit_list)/len(fit_list))
    return avg_fit_list

# returns list of 2 selected chrs
def roulette_wheel_selection(chrs, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    cumulative_probabilities = [sum(probabilities[:i + 1]) for i in range(len(probabilities))]

    selected = []
    for _ in range(2):  # Select two parents
        spin = random.random()
        for i, cum_prob in enumerate(cumulative_probabilities):
            if spin <= cum_prob:
                selected.append(chrs[i])
                break

    return selected

# returns list of 2 np.arrays of child
def cross(selected):
    pt1 = random.randint(0,53)
    pt2 = random.randint(0,53)

    low = min(pt1,pt2)
    high = max(pt1,pt2)

    child1 = np.zeros(54)
    child2 = np.zeros(54)
    for i in range(54):
        if i>= low and i<=high:
            child1[i] = selected[1][i]
            child2[i] = selected[0][i]
        else:
            child1[i] = selected[0][i]
            child2[i] = selected[1][i]
    return [child1, child2]

# returns 1 mutated child
def mut(child):
    mutation = 0.005
    for i in range(54):
        p = random.random()
        if p<=mutation:
            locus = random.randint(0, 3)
            child[i] = locus
    return child

# data fram for chrs of each gen
chrs = []
# initialize data frame
chrs_init = np.array([[random.randint(0,3) for _ in range(54)] for _ in range(100)])
room = np.array([[random.randint(0,1) for _ in range(60)] for _ in range(30)])
chrs.append(chrs_init)

for i in range(200):
    # get each chrs fitness
    avg_fit_list = avg_fit_play(chrs[i], room)

    # chrs for next gen
    data_new = []
    for _ in range(50):
        # get two chrs according to fitness
        selected = roulette_wheel_selection(chrs[i], avg_fit_list)
        # cross the two chrs
        two_cross_chrs = cross(selected)
        # mutate childs
        child1 = mut(two_cross_chrs[0])
        child2 = mut(two_cross_chrs[1])

        # append to next gen data
        data_new.append(child1)
        data_new.append(child2)

    chrs.append(data_new)

# plot final set of chrs[-1] - how?
fig, ax = plt.subplots()

# Plot the chromosomes
ax.imshow(chrs[-1], cmap='viridis', aspect='auto')

# Set labels and title
ax.set_xlabel('Locus')
ax.set_ylabel('Chromosome')
ax.set_title('Set of Chromosomes')


plt.savefig('chromosome.jpg')
#plt.show()
plt.clf()
# example traj - play each chrs, find most succesful and plot trajectory
fitness = []
trajectory = []
for chr in chrs[-1]:
    f = painter_play(chr, room)
    fit = f[0]
    traj = f[1]

    fitness.append(fit)
    trajectory.append(traj)

chr_index = fitness.index(max(fitness))
plot_traj = trajectory[chr_index]
time_steps = np.arange(len(plot_traj))

ax.set_xlabel('time step')
ax.set_ylabel('trajectory')
ax.set_title('trajectory')

# plot positions
plt.plot(time_steps, plot_traj, marker='o')
plt.savefig('trajectory.jpg')
#plt.show()

