import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("OISST_60.125E_5.125N.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['timestamp','target']).sort_values('timestamp')

plt.figure(figsize=(24,4), dpi=200)
plt.plot(df['timestamp'], df['target'], linewidth=0.5, alpha=0.9)
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
plt.xticks(rotation=30, ha='right')
plt.xlabel("Date")
plt.ylabel("SST (°C)")
plt.title(df['item_id'].iloc[0] if 'item_id' in df.columns else "SST time series")
plt.grid(alpha=0.22)
plt.tight_layout()
plt.savefig("sst_timeseries_60.125_5.125_wide.png", dpi=200)
plt.show()
