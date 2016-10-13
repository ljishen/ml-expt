#!/usr/bin/env python

# Simulate a large number (say 10,000) of coin tosses with two dependent coins.

from __future__ import division
import random

# Generate tosses results
NUM_OF_TOSSES = 10000
tosses = []
for _ in range(NUM_OF_TOSSES):
    # this ensures X and Y cannot be repeated, such that
    # X and Y is not independent
    tosses.append(random.sample(range(1, 3), 2))

# Verify p(X,Y) = p(X) * p(Y)
x = 1
y = 2

count_x_y = 0
count_x = 0
count_y = 0
for toss in tosses:
    if toss[0] == x and toss[1] == y:
        count_x_y += 1
    if toss[0] == x:
        count_x += 1
    if toss[1] == y:
        count_y += 1
p_x_y = count_x_y / NUM_OF_TOSSES
p_x = count_x / NUM_OF_TOSSES
p_y = count_y / NUM_OF_TOSSES

## Show results summary
print "p_x =", p_x
print "p_y =", p_y
print "p_x * p_y =", (p_x * p_y)
print "p_x_y =", p_x_y
print "distance between p_x_y and p_x * p_y : ", abs(p_x_y - p_x * p_y), "\n"


# Verify E(XY) = E(X) * E(Y)
rg = range(1, 3)

## Calculate E(XY)
x_y_values=[]
x_y_count=[]
for i in rg:
    for j in rg:
        if i == j: continue
        m = i * j
        if m not in x_y_values:
            x_y_values.append(m)
            x_y_count.append(1)
        else:
            x_y_count[x_y_values.index(m)] += 1

cases = sum(x_y_count)
x_y_expt = 0
for i in range(len(x_y_values)):
    x_y_expt += x_y_values[i] * x_y_count[i] / cases

print "x_y_expt =", x_y_expt

## Calculate E(X) or E(Y)
x_expt = 0
for i in rg:
    x_expt += i * 1 / len(rg)

y_expt = x_expt

## Show results summary
print "x_expt =", x_expt
print "y_expt =", y_expt

print "distance between x_y_expt and x_expt * y_expt : ", abs(x_y_expt - x_expt * y_expt)
