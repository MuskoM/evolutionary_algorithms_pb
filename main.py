import differential_evolution as de

if __name__ == '__main__':
    population = 6
    algorithm = de.DifferentialEvolution(population=12)
    algorithm.run()
    print("Best output:")
    print(f'Value: {algorithm.best}')
    print(f'Value: {algorithm.best_vector}')