import numpy as np
import inspect 
import typing as t
import random as rnd

class DifferentialEvolution:

    def __init__(
            self,
            mutation_func,
            test_func,
            population=12,
            diff_weight = 0.5,
            iterations = 10,
            vector_len = 4,
            cross_const = 0.1,
            ):
        self.F = diff_weight
        self.cr = cross_const
        self.number_of_solutions = population
        self.solutions = []
        self.number_of_iterations = iterations
        self.vector_len = vector_len

        self.mutate = mutation_func
        self.test = test_func
        self.best = None
        self.best_vector = None
        self.iteration_values = []

        for i in range(self.number_of_solutions):
            # size of vector should be defined by a test function or param?
            solution = np.random.normal(size=self.vector_len)
            self.solutions.append(solution)


    def run(self):
        for iteration in range(self.number_of_iterations):
            for indx, curr_solution in enumerate(self.solutions):
                if indx == 0 and iteration == 0 :
                    self.best = abs(0.0 - self.test(curr_solution))
                    self.best_vector = curr_solution
                candidates = self.get_candidates(indx, self.mutate)
                mutation = self.mutate(self.F, *candidates)
                test_solution = self.crossover(curr_solution, mutation)
                new_value = self.test(test_solution)
                loss = abs(0.0 - new_value)
                if loss < self.best:
                    self.best = loss
                    self.best_vector = mutation
            self.iteration_values.append(self.best)


    def get_candidates(self, curr_solution_indx: int, function: t.Callable):
        number_of_candidates = len(inspect.signature(function).parameters) - 1
        function_type = function.__name__.split('_')[1]
        selected_indxs = []
        candidates = []
        for i in range(number_of_candidates):
            random_num = np.random.randint(0, self.number_of_solutions)
            if random_num == curr_solution_indx or random_num in selected_indxs:
                random_num = np.random.randint(0, self.number_of_solutions)
            candidates.append(self.solutions[random_num])
            selected_indxs.append(random_num)
        
        if function_type == 'best':
            candidates[0] = self.best_vector

        return candidates
    
    def crossover(self, parent, mutation):
        d = rnd.randint(0, len(mutation)-1)
        result = []
        for j in range(len(parent)):
            cur_rnd = rnd.uniform(0.0, 1.0)
            if cur_rnd < self.cr or j == d:
                result.append(mutation[j])
            else:
                result.append(parent[j])
        return result