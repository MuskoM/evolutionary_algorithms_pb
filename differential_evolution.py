import numpy as np
import typing as t

class DifferentialEvolution:

    def __init__(
            self,
            mutation_func,
            test_func,
            population=12,
            diff_weight = 0.8,
            iterations = 10
            ):
        self.F = diff_weight
        self.number_of_solutions = population
        self.solutions = []
        self.number_of_iterations = iterations

        self.mutate = mutation_func
        self.test = test_func
        self.best = None
        self.best_vector = None

        for i in range(self.number_of_solutions):
            # size of vector should be defined by a test function or param?
            solution = np.random.normal(size=5)
            self.solutions.append(solution)


    def run(self):
        for _ in range(self.number_of_iterations):
            for indx, curr_solution in enumerate(self.solutions):
                if indx == 0:
                    self.best = self.test(curr_solution)
                a,b,c = self.get_candidates(indx)
                mutation = self.mutate(self.F, a,b,c)
                new_value = self.test(mutation)
                if new_value < self.best:
                    self.best = new_value
                    self.best_vector = mutation


    def get_candidates(self, curr_solution_indx: int):
        selected_indxs = []
        candidates = []
        for i in range(3):
            random_num = np.random.randint(0, self.number_of_solutions)
            if random_num == curr_solution_indx or random_num in selected_indxs:
                random_num = np.random.randint(0, self.number_of_solutions)
            candidates.append(self.solutions[random_num])
            selected_indxs.append(random_num)
        return candidates