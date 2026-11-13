import pandas as pd
from pathlib import Path


df = pd.read_csv(Path(__file__).parent / "test_run.csv")
print(df)

data = {

    'Name': ['Alice', 'Isaac', 'Cary'],
    'Age': [100, 50, 20],
    'Country': ['USA', 'Canada', 'North Korean']
}

gf = pd.DataFrame(data)
print(gf)
print(gf.loc[0, 'Country'])
print(df.head())
print(df.describe())
print(df.columns)