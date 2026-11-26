import pandas as pd
from pathlib import Path

#formatting stuff to make it more readable
def section(title):
    print(f"\n{'=' * 50}\n{title}\n{'=' * 50}")

df = pd.read_csv("test_run.csv", comment="#")
print(df)
df["time_s"] = (df["Millis"] - df["Millis"].iloc[0]) / 1000 #time stamp since start
df["dt_s"] = df["time_s"].diff() #time between consecutive samples - used for integration later so as to not assume time step
section("Data trend for detla t")
print(df["dt_s"].describe()) #if corrections are needed
section("# of Updates from telem")
print(df[["Speed_kmh", "Latitude", "Altitude_m"]].nunique())
section("Amount of missing values:")
print(df.isna().sum())
