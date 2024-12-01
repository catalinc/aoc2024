import sys
import pandas as pd


def read_input(fname: str) -> pd.DataFrame:
    return pd.read_csv(fname, sep=r'\s+', header=None)

def part1(df: pd.DataFrame) -> int:
    df[0] = df[0].sort_values().values
    df[1] = df[1].sort_values().values    
    df['diff'] = df[1] - df[0]
    df['diff'] = df['diff'].abs()
    return df['diff'].sum()

def part2(df: pd.DataFrame) -> int:
    similarity = 0
    df_counts = df[1].value_counts()
    for _, n in df[0].items():
        similarity += n * df_counts.get(n, 0)
    return similarity

def main():
    input_file = 'input/day1.txt'
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
    df = read_input(input_file)
    print(part1(df))
    print(part2(df))

if __name__ == '__main__':
    main()