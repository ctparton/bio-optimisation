import pathlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv

if __name__ == '__main__':
    REPEATS = 30
    generational_fitness = {}

    with open(pathlib.Path.cwd().parent / 'CW1' / 'out.txt', 'r', encoding="utf-16") as reader:
        for line in reader:
            try:
                if not generational_fitness.get(int(line.split(" ")[0])):
                    generational_fitness.update({int(line.split(" ")[0]): float(line.split(" ")[1])})

                else:
                    generational_fitness[int(line.split(" ")[0])] = generational_fitness.get(
                        int(line.split(" ")[0])) + float(line.split(" ")[1])
            except ValueError:
                if not generational_fitness.get(line.split(" ")[0]):
                    generational_fitness.update({line.split(" ")[0]: float(line.split(" ")[1])})

                else:
                    generational_fitness[line.split(" ")[0]] = generational_fitness.get(line.split(" ")[0]) + float(
                        line.split(" ")[1])

    for key in generational_fitness.keys():
        generational_fitness[key] = generational_fitness[key] / REPEATS

    runtime = "Runtime " + str(generational_fitness.get("exec")) + " (S)"
    fitness = "Best Fitness " + str(generational_fitness.get("best"))
    generational_fitness.pop("exec")
    generational_fitness.pop("best")

    fig, ax = plt.subplots()

    x, y = zip(*sorted(generational_fitness.items()))
    ax.plot(x, y)
    ax.text(0.95, 0.95, runtime,
            horizontalalignment='right',
            verticalalignment='top',
            transform=ax.transAxes)
    ax.text(0.95, 0.85, fitness,
            horizontalalignment='right',
            verticalalignment='top',
            transform=ax.transAxes)
    ax.set(xlabel='Generation', ylabel='Fitness',
           title='Baseline GA')
    output_path = pathlib.Path.cwd() / 'output'
    output_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path / 'output_increased_mutation.png')
    plt.show()
