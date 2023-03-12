import numpy as np

class DifferentialEvolution:

    def __init__(self, population=12, diff_weight = 0.8):
        self.F = diff_weight
        self.solutions = []
        self.best = None
        self.best_vector = None
        self.number_of_solutions = population
        for i in range(self.number_of_solutions):
            solution = np.random.normal(size=5)
            self.solutions.append(solution)

    def run(self):
        for indx, curr_solution in enumerate(self.solutions):
            if indx == 0:
                self.best = self.sphere_function(curr_solution)
            a,b,c = self.get_candidates(indx)
            mutation = self.mutate(a,b,c)
            new_value = self.sphere_function(mutation)
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
    
    def mutate(self, a, b, c):
        return a * self.F * (b - c)
    
    def sphere_function(self, vec: np.ndarray):
        return (vec**2).sum()