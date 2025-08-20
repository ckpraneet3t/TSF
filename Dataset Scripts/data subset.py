import pandas as pd

df = pd.read_csv("OISST_60E_72E_5N_20N.csv")

cell_id = "60.125_5.125"
df_cell = df[df['id'] == cell_id]

df_cell.to_csv("OISST_timeseries_60.125_5.125.csv", index=False)
