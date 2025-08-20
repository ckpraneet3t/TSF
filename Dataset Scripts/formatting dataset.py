import pandas as pd

df = pd.read_csv("OISST_60E_72E_5N_20N.csv")
df = df.rename(columns={'id':'item_id','date':'timestamp','sst':'target'})
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True, errors='coerce').dt.date
df_grouped = df.sort_values(['item_id','timestamp']).set_index(['item_id','timestamp'])[['target']]
df_grouped.to_csv("OISST_grouped_by_itemid_timestamp.csv")
print(df_grouped.head(20))
