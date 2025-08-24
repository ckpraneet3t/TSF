import pandas as pd
import matplotlib.pyplot as plt
import calmap 

df = pd.read_csv("OISST_60.125E_5.125N.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['timestamp','target'])

df.set_index('timestamp', inplace=True)
events = df['target'] 

plt.figure(figsize=(16, 8), dpi=200)

calmap.yearplot(events, 
                year=2023, 
                cmap='viridis', 
                linewidth=1,
                daylabels='MTWTFSS')

plt.suptitle("Daily Sea Surface Temperature (SST) Heatmap for 2023", fontsize=16, y=0.92)
plt.tight_layout(pad=3.0)
plt.savefig("sst_heatmap_2023.png", dpi=200)
plt.show()