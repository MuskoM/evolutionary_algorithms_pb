import differential_evolution as de
import test_functions as test
import mutation_functions as mut
from visualization import Visualize
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
        '--test', default='michalewicz', help='Name of testing function',
        choices=TEST_FUNCTIONS
    )

    argument_parser.add_argument(
        '--mutation', default='de_best_2', choices=MUTATION_FUNCTIONS, help='Name of mutation strategy'
    )

    input_args = argument_parser.parse_args()

    population = 6
    algorithm = de.DifferentialEvolution(
        population=int(input_args.population),
        iterations=int(input_args.iteration),
        test_func=getattr(test, input_args.test),
        mutation_func=getattr(mut, input_args.mutation)
    )

    print('===Running Differential Evolution===')
    print('===Params===')
    print(f'Population: {input_args.population}')
    print(f'Iterations: {input_args.iteration}')
    print(f'Test function: {input_args.test}')
    print(f'Mutation strategy: {input_args.mutation}')


    algorithm.run()
    print("\n===Best output===")
    print(f'Value: {algorithm.best}')
    print(f'Value: {algorithm.best_vector}')

    vis = Visualize(getattr(test, input_args.test))
    vis.show_best([*algorithm.best_vector,algorithm.best])