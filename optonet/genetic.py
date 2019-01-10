from abc import ABC, abstractmethod


class EvolutionHandler:
    """
    EvolutionHandler handles evolution of the population.
    """
    def __init__(self, starting_population, selection_handler, mutation_handler, crossover_handler, replacement_handler, config):
        """
        Initialize EvolutionHandler with necessary components
        :param starting_population: Population of chromosomes to start the evolution with
        :param selection_handler: An object that will handle selecting parents from every population
        :param mutation_handler: An object that will handle mutation of given population
        :param crossover_handler: An object that will handle crossover between
        :param config: A dictionary with necessary parameters
        """
        self.__population = starting_population
        self.__mutation_handler = mutation_handler
        self.__crossover_handler = crossover_handler
        self.__selection_handler = selection_handler
        self.__replacement_handler = replacement_handler
        self.__config = config
        self.__age = 0

    def evolve(self):
        if self.__config['debug']:
            print("Current population age: {}".format(self.__age))

        fitnesses = [chromosome.fitness for chromosome in self.__population]
        print("Fitness sum: {}, avg: {}, max: {}".format(sum(fitnesses), sum(fitnesses)/len(fitnesses), max(fitnesses)))

        parents = self.__selection_handler.choose_parents(self.__population)
        new_population = self.__crossover_handler.crossover(parents)
        mutated_population = self.__mutation_handler.mutate(new_population)
        # if len(mutated_population) != self.__config['population_size']:
        #     self.save_population()
        #     raise Exception("New population size: {}. Expected: {}".format(
        #         len(mutated_population),
        #         self.__config['population_size'])
        #     )
        self.__population = self.__replacement_handler.replace_generation(self.__population, mutated_population)
        self.__age += 1

    def save_population(self):
        """
        Saves current population
        :return:
        """

    def get_best_chromosome(self):
        best = self.__population[0]
        for chromosome in self.__population:
            if chromosome.fitness > best.fitness:
                best = chromosome
        return best

class BaseCrossoverHandler(ABC):
    """
    BaseCrossoverHandler is base class that every crossover handler should inherit from
    """
    @abstractmethod
    def crossover(self, parents):
        """
        crossover takes parent population, performs crossover using them and returns child population
        :param parents:
        :return: child population
        """


class BaseMutationHandler(ABC):
    """
    BaseMutationHandler is base class that every mutation handler should inherit from
    """
    @abstractmethod
    def mutate(self, population):
        """
        Mutate given population
        :param population: population to mutate
        :return: mutated population
        """


class BaseSelectionHandler(ABC):
    """
    BaseSelectionHandler is the base class that every selection handler should inherit from
    """
    @abstractmethod
    def choose_parents(self, population):
        """
        Choose suitable parents for crossover from given population
        :param population: population to choose from
        :return: parent population
        """


class BaseReplacementHandler(ABC):
    """
    BaseReplacementHandler is the base class that every replacement handler should inherit from
    """
    @abstractmethod
    def replace_generation(self, old_population, offsprings):
        """
        Decide which individuals from old population should be replaced with generated offsprings
        :param old_population: current generation
        :param offsprings: generated offsprings of current generation
        :return: updated population
        """
