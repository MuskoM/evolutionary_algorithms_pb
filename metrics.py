import typing as t
from datetime import datetime

import numpy as np
import pandas as pd
from pathlib import Path
from differential_evolution import DifferentialEvolution


class Metrics:
    def __init__(self, algorithm: DifferentialEvolution):
        self.SEP = ';'
        self.algorithm: DifferentialEvolution = algorithm
        self.test_function_name = algorithm.test.__name__
        self.mutation_strategy_name = algorithm.mutate.__name__
        self.fig_path = Path('runs')

    def _create_file(self):
        if not self.fig_path.exists():
            self.fig_path.mkdir(parents=True)

    def log(self, log_by, value):
        timestamp = datetime.now().strftime(r'%y%m%d%H%M%S')
        dest = self.fig_path.joinpath(log_by)
        if not dest.exists():
            dest.mkdir()
        with open(dest.joinpath(str(value)+'.csv'),'+a') as file:
            file.write('Iteration;Value;Population;Vector_len;Test;Mutation\n')
            for i, v in enumerate(self.algorithm.iteration_values):
                file.write(f'{i};{v};{self.algorithm.number_of_solutions}{self.algorithm.vector_len};{self.test_function_name};{self.mutation_strategy_name}\n')

    def plot_log(self):
        df = pd.read_csv(self.fig_path.joinpath('tested_value.csv'))