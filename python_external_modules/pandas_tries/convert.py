import pandas as pd # create a sample DataFrame with a column of float type


def main():
    df = pd.DataFrame({'col1': [1.0, 2.0, float('nan'), 4.0]})# convert the column to int type while preserving NaN values
    print(f'Initial:\n{df}')
    df.info()
    df['col1'] = df['col1'].astype('Int64')
    print(f'\nConverted:\n {df=}')
    df.info()

if __name__ == '__main__':
    main()
