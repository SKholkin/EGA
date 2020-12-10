from crossover.classic_crossover import single_point_crossover, double_point_crossover
import warnings


def launch_crossover(population, config):
    descendants = []
    if config.crossover == "double":
        if not len(population) % 2 == 0:
            warnings.warn("Amount of parents after selection isn't dividing by 2"
                          "\nPlease check selection and breeding algorithms")
        for i in range(len(population) // 2):
            descendants += single_point_crossover(population[i], population[i + 1])
    elif config.crossover == "single":
        if not len(population) % 2 == 0:
            warnings.warn("Amount of parents after selection isn't dividing by 2"
                          "\nPlease check selection and breeding algorithms")
        for i in range(len(population) // 2):
            descendants += single_point_crossover(population[i], population[i + 1])
    raise AttributeError('Wrong crossover algorithm chosen. Please check config.')

