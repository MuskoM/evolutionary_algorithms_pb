import differential_evolution as de
import test_functions as test
import mutation_functions as mut
from visualization import Visualize
from metrics import Metrics

from argparse import ArgumentParser
import inspect

TEST_FUNCTIONS = [fun[0] for fun in inspect.getmembers(test, inspect.isfunction)]
MUTATION_FUNCTIONS = [fun[0] for fun in inspect.getmembers(mut, inspect.isfunction)]

if __name__ == '__main__':

    argument_parser = ArgumentParser('Differential Evolutjion')
    argument_parser.add_argument(
        '-p', '--population', default=12, help='Number of samples in population'
    )
    argument_parser.add_argument(
        '-i', '--iteration', default=100, help='Number of iterations for the algorithm'
    )
    argument_parser.add_argument(
        '-l', '--vector_length', default=4, help='Length of a vector'
    )
    argument_parser.add_argument(
        '--test', default='michalewicz', help='Name of testing function',
        choices=TEST_FUNCTIONS
    )

    argument_parser.add_argument(
        '--mutation', default='de_best_2', choices=MUTATION_FUNCTIONS, help='Name of mutation strategy'
    )

    argument_parser.add_argument(
        '--log_by', required=True, choices=['population', 'test_function', 'mutation_strategy', 'vector_length']
    )

    input_args = argument_parser.parse_args()

    population = 6
    algorithm = de.DifferentialEvolution(
        population=int(input_args.population),
        iterations=int(input_args.iteration),
        test_func=getattr(test, input_args.test),
        mutation_func=getattr(mut, input_args.mutation),
        vector_len=int(input_args.vector_length)
    )

    print('===Running Differential Evolution===')
    print('===Params===')
    print(f'Population: {input_args.population}')
    print(f'Vector length: {input_args.vector_length}')
    print(f'Iterations: {input_args.iteration}')
    print(f'Test function: {input_args.test}')
    print(f'Mutation strategy: {input_args.mutation}')


    algorithm.run()
    print("\n===Best output===")
    print(f'Value: {algorithm.best}')
    print(f'Value: {algorithm.best_vector}')
    print(f'History: {algorithm.iteration_values}')

    vis = Visualize(getattr(test, input_args.test), getattr(mut, input_args.mutation))
    # vis.show_best([*algorithm.best_vector[:2],algorithm.best])
    # vis.plot_history(algorithm.iteration_values)
    
    metrics = Metrics(algorithm) 
    metrics.log(input_args.log_by, getattr(input_args, input_args.log_by))
