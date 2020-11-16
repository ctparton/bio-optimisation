import pathlib
import argparse
import pandas

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pso', help='add value of true if using pso')
    args = parser.parse_args()
    REPEATS = 30
    output_file = "test4.csv"
    generational_fitness = []
    print(f"Writing to {output_file}")
    if args.pso:
        df = pandas.read_csv(pathlib.Path.cwd().parent / 'CW1' / 'out.txt', sep=" ",
                             names=['generation', 'fitness', 'numParticles',
                                    'neighWeight',
                                    'inertiaWeight',
                                    'personalWeight',
                                    'globalWeight',
                                    'duration'], encoding="utf-16")
    else:
        df = pandas.read_csv(pathlib.Path.cwd().parent / 'CW1' / 'out.txt', sep=" ",
                             names=['generation', 'fitness', 'popSize',
                                    'numSurvivors',
                                    'tournamentSize',
                                    'probMutation',
                                    'probCrossover',
                                    'duration'], encoding="utf-16")
    df = df.groupby('generation', as_index=False).mean()
    df['overallTime'] = df['duration'].sum()
    df['bestFitness'] = df['fitness'].min()
    print(df)
    csv_file = pathlib.Path.cwd() / 'output' / 'csv' / output_file
    if csv_file.exists():
        df.to_csv(csv_file, index=False, mode='a', header=False)
    else:
        df.to_csv(csv_file, index=False, header=True)
