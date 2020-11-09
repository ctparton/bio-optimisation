import pathlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas

if __name__ == '__main__':
    REPEATS = 30
    output_file = "survivors.csv"
    generational_fitness = []
    generation = 1
    with open(pathlib.Path.cwd().parent / 'CW1' / 'out.txt', 'r', encoding="utf-16") as reader:
        for line in reader:
            try:
                exists = list(filter(lambda g: g['generation'] == int(line.split(" ")[0]), generational_fitness))
                if len(exists) < 1:
                    generational_fitness.append(
                        {'generation': int(line.split(" ")[0]), 'fitness': float(line.split(" ")[1]),
                         "popSize": line.split(" ")[2], "numSurvivors": line.split(" ")[3],
                         "tournamentSize": line.split(" ")[4], "probMutation": line.split(" ")[5],
                         "probCrossover": line.split(" ")[6], "duration": float(line.split(" ")[7])})

                else:
                    generational_fitness[generational_fitness.index(exists[0])]['fitness'] = exists[0][
                                                                                                 'fitness'] + float(
                        line.split(" ")[1])
                    generational_fitness[generational_fitness.index(exists[0])]['duration'] = exists[0][
                                                                                                  'duration'] + float(
                        line.split(" ")[7])
            except ValueError:
                pass

    for generation in generational_fitness:
        generation['fitness'] = generation['fitness'] / REPEATS
        generation['duration'] = generation['duration'] / REPEATS

    runtime = sum(gen['duration'] for gen in generational_fitness)
    best_fitness = min(gen['fitness'] for gen in generational_fitness)
    for gen in generational_fitness:
        gen.update({"overallTime": runtime, "bestFitness": best_fitness})
    csv_file = pathlib.Path.cwd() / 'output' / 'csv' / output_file
    if csv_file.exists():
        pandas.DataFrame(generational_fitness).to_csv(csv_file, index=False, mode='a', header=False)
    else:
        pandas.DataFrame(generational_fitness).to_csv(csv_file, index=False)


