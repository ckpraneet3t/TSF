import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("OISST_60.125E_5.125N.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['timestamp', 'target']).sort_values('timestamp')
plt.figure(figsize=(12,5))
plt.plot(df['timestamp'], df['target'], marker='o', linewidth=1.5)
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.xticks(rotation=45, ha='right')
plt.xlabel("Date")
plt.ylabel("SST (°C)")
plt.title(f"SST time series — {df['item_id'].iloc[0] if 'item_id' in df.columns else ''}")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("sst_timeseries_60.125_5.125.png", dpi=300)
plt.show()
