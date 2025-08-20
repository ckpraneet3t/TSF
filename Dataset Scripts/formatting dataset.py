import os
import pandas as pd
from pprint import pprint

path = "OISST_60E_72E_5N_20N.csv"
if not os.path.exists(path):
    raise FileNotFoundError(f"File not found: {path}")

df = pd.read_csv(path)
rows, cols = df.shape
col_names = df.columns.tolist()
dtypes = df.dtypes.apply(lambda x: x.name).to_dict()
non_null = df.notnull().sum().to_dict()
memory_bytes = int(df.memory_usage(deep=True).sum())

date_col = None
for c in df.columns:
    if c.lower() in ("date","timestamp","time","day"):
        date_col = c
        break

date_info = None
if date_col:
    dates = pd.to_datetime(df[date_col], dayfirst=True, errors='coerce')
    date_info = {
        "column": date_col,
        "min": str(dates.min()),
        "max": str(dates.max()),
        "na_count": int(dates.isna().sum())
    }

first_row = df.iloc[0].to_dict()
last_row = df.iloc[-1].to_dict()

unique_info = {}
if "id" in df.columns:
    unique_info["unique_ids"] = int(df["id"].nunique())
    unique_info["top_10"] = df["id"].value_counts().head(10).to_dict()
elif "item_id" in df.columns:
    unique_info["unique_ids"] = int(df["item_id"].nunique())
    unique_info["top_10"] = df["item_id"].value_counts().head(10).to_dict()

summary = {
    "path": path,
    "rows": int(rows),
    "columns": int(cols),
    "column_names": col_names,
    "dtypes": dtypes,
    "non_null_counts": non_null,
    "memory_bytes": memory_bytes,
    "date_info": date_info,
    "first_row": first_row,
    "last_row": last_row,
    "unique_id_info": unique_info
}

pprint(summary)

# write outputs
pd.DataFrame([summary]).to_json("OISST_summary.json", orient="records", lines=True)
df.iloc[[0]].to_csv("OISST_first_row.csv", index=False)
df.iloc[[-1]].to_csv("OISST_last_row.csv", index=False)
