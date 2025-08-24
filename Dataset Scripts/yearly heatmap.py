import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("OISST_60.125E_5.125N.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['timestamp', 'target'])

df['month'] = df['timestamp'].dt.month_name()

plt.figure(figsize=(12, 6), dpi=200)

month_order = [
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
]

sns.boxplot(x='month', y='target', data=df, order=month_order, palette='coolwarm')

plt.title("Monthly SST Distribution", fontsize=16)
plt.ylabel("SST (°C)")
plt.xlabel("Month")
plt.xticks(rotation=45, ha='right')
plt.grid(alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig("sst_monthly_boxplot.png", dpi=200)
plt.show()