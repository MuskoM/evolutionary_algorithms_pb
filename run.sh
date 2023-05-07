#!/bin/bash
for p in 50 100 200 300 500; do
    python3 main.py --population $p --log_by population
done

for v in 2 4 8 12; do
    python3 main.py -l $v --log_by vector_length
done

for t in ackley dixonprice griewank levy michalewicz powell rastagin rosenbrock schwefel spherical; do
    python3 main.py --test $t --log_by test_function
done

for m in de_best_1 de_best_2 de_rand_1 de_rand_2; do
    python3 main.py --mutation $m --log_by mutation_strategy
done
