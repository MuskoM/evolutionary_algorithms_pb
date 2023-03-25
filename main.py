import differential_evolution as de
import test_functions as test
import mutation_functions as mut

if __name__ == '__main__':
    population = 6
    algorithm = de.DifferentialEvolution(
        population=12,
        iterations=100,
        test_func=test.spherical,
        mutation_func=mut.rand1bin
    )

    algorithm.run()
    print("Best output:")
    print(f'Value: {algorithm.best}')
    print(f'Value: {algorithm.best_vector}')