import pandas as pd

df = pd.read_csv("OISST_60E_72E_5N_20N.csv")
df.to_parquet("OISST_60E_72E_5N_20N.parquet", engine="pyarrow", compression="snappy")
