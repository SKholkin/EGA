from crossover.classic_crossover import single_point_crossover, double_point_crossover
import warnings


def launch_crossover(population, config):
    descendants = []
    if config.crossover == "double":
        if not len(population) % 2 == 0:
            warnings.warn("Amount of parents after breed isn't dividing by 2"
                          "\nPlease check breed and breeding algorithms")
        for i in range(len(population) // 2):
            descendants += single_point_crossover(population[i], population[i + 1])
        return descendants
    elif config.crossover == "single":
        if not len(population) % 2 == 0:
            warnings.warn("Amount of parents after breed isn't dividing by 2"
                          "\nPlease check breed and breeding algorithms")
        for i in range(len(population) // 2):
            descendants += single_point_crossover(population[i], population[i + 1])
        return descendants
    else:
        raise AttributeError('Wrong crossover algorithm chosen. Please check config.')

