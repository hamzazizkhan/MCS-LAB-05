# MCS-LAB-05
### FILES
lab5.py - Part 1 code\
chromosome.jpg - Final set of chromosomes\
trajectory.jpg - Final trajectory (most efficient chromosome)

part2.py - part2 code\
equalprobs.jpg - plot with equal probabilities for vertices\
un_equalprobs - plot with unequal probabilities for vertices

## PART 1
In part 1 we are supposed to use a genetic algorithm to find the optimal set of rules that a painter should follow.

### CONTENT Lab5.PY
The outline of the algorithm is as follows:
- Define functions 
- initialize data frame
- Evolution over 200 generations.
- plot final set of chromosomes and trajectory

### DEFINE FUNCTIONS
There are four functions in the code:

1) **avg_fit_play(chrs, room)** - Takes the set of chromosomes and the room as input arguments.\
It returns a list of size 100 with the average fitness value for each chromosome.\
The function plays each chromosome ten times and gets the average fitness value from the ten iterations.


2) **roulette_wheel_selection(chrs, fitness_values)** - Takes the set of chromosomes and a list of the average fitness values for each chromosome.\
It returns a list of two selected chromosomes for crossover and mutation.\
The function gets the probabilities for each chromosome by taking the average fitness value divided by the total sum of fitness values.
The cumulative probabilities are then obtained.
Next, we select two parents by generating a random probability and comparing it with the cumulative probabilites.
If it is less than or equal to a cumulative probability, we take the chromosome at the index of the matched cumulative probability.


3) **cross(selected)** - Takes the selected chromosomes from function 2 as input arguments.\
It returns a list of two children.\
The function performs a two-point crossover.\
First we generate two random indexes, one lower(low) and one higher(high). 
We loop through all the indexes (i = 53) and find the interval low<= i <=high.
This interval of the first childs locus will take the second parents locus at the same interval.
Similarly, the second childs locus will take the first parents locus at this interval.
Outside of this interval, the first childs locus will take the first parents locus.
Similarly, the second childs locus will take the second parents locus.


4) **mut(child)** - Takes one child chromosome as an argument.\
Returns a mutated child.\
The muatation rate is 0.005.
First, we loop through the locus of the child and generate a random probability for each locus.
If the probability is less than or equal to the mutation rate the locus is assigned a random value from the interval 0-3.

### INITIALIZE DATA FRAME
The data frame is initialized by appending a set of chromosomes of size 100x54 with random values between 0-3.
The room is initialized with random values from 0-1 of size 30x60.

### EVOLUTION OVER 200 GENERATIONS
A for loop is run with range 200. The following is done in each iteration :
- function 1 is called to get each chromosomes' fitness.

- Next, we get the next generation of chromosomes by running a for loop of range 50.
In each iteration, we select two chromosomes according to fitness by calling function 2 and subsequently perform two point cross over and mutation on the two children.
The two children are added to the next generation dataset.
After the for loop is run we will have 100 children.

### PLOT FINAL SET OF CHROMOSOMES AND TRAJECTORY.
To get the most efficient chromosome, the final set of chromosomes are played again and the trajectory of the chromosome with the highest fitness is plotted.\
Please view chromosome.jpg and trajectory.jpg

## PART 2
### CONTENT PART2.PY
The outline of the algorithm is as follows:
- Define functions 
- initialize triangle
- Main loop to plot current position
- plots for unequal and equal probabilities.

### DEFINE FUNCTIONS
1) **rand_pt(p1, p2, p3)** - Takes the three vertices of the triangle as input arguments.\
Returns a random point in the triangle.\
The function generates a random point within the triangle using the Barycentric coordinates method. The function uses two random numbers r1 and r2 generated from a uniform distribution to calculate the coordinates of the random point.


2) **select(cum_probs, tri_pts)** - Takes the cumulative probabilities of the vertices and the vertex points as arguments.\
Returns the selected vertex according to probabilities.\
The function generates a random probability and compares it with the cumulative probabilities of vertices.
If it is less than the cumulative probability of a vertex, we choose that vertex.


3) **move(pt, vertex)** - Takes the current position in the triangle and the selected vertex as arguments.\
Returns the new point that has moved half the distance from the old point to the vertex.\
The function gets the vector pointing to the vertex from the point and divides this by two.
This vector is added to the current point.


4) **hundred(tri_pts, pt, cum_probs)** - Takes vertices, current point in triangle, cumulative probabilities of vertices.
Returns a final point after 100 iterations of selecting a vertex and moving half the distance from the current point to the vertex.\
This function runs function 2 and 3 one hundred times in a for loop. The current point selects a vertex and moves half the distance to the vertex 100 times, each time selecting a vertex according to the probabilities.

   
### INITIALIZE TRIANGLE AND PROBABILITIES
The triangle is initialized with (19, 11), (8, 25), (23, 22) as vertices.\
The unequal probabilities chosen were 0.5, 0.3, 0.2.

### MAIN LOOP
Before the main loop, a random point inside the triangle is generated using function 1.

A for loop of size 100 is run.
in each iteration:
- function 4 is called producing a point which is plotted.

This is repeated for equal probabilities.

## QUESTION 1
vertices (19, 11), (8, 25), (23, 22).\
The unequal probabilities chosen were 0.5, 0.3, 0.2 respectively.

The limit set for equal probabilities will be the entire triangle. The algorithm covers the entire triangle uniformly.

The limit set for unequal probabilities will be biased towards the vertex with a higher probability (in this case vertex 19,11).
This vertex will be visited most often and has the highest concentration of points around it (in the limit set) while
vertex 23,22 has the least concentration of points around it as it has the lowest probability.

## QUESTION 2
Let A, B, C be the three vertices of the triangle, and let P be the current position.

Randomly select one of the three vertices with probabilities p1, p2, p3, respectively.
Calculate the midpoint M between the current position P and the selected vertex.
Update the current position P to be the new midpoint M.

The iterated function system transformation rules can be expressed as:

f1(x, y) = ((x + A[0]) / 2, (y + A[1]) / 2)\
f2(x, y) = ((x + B[0]) / 2, (y + B[1]) / 2)\
f3(x, y) = ((x + C[0]) / 2, (y + C[1]) / 2)

These functions represent the transformation rules for each vertex of the triangle. 
Given the current position (x, y), applying one of these functions will move the position halfway towards the corresponding vertex.

To obtain the iterated function system, randomly select one of these functions with probabilities p1, p2, p3, and iteratively apply them to the current position.









