# Install cartopy if not available
# !pip install cartopy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# -----------------------------
# Example: load your CSV
# -----------------------------
# Assuming your dataset looks like:
# id,date,sst
# 60.125_5.125,01-Sep-0081,27.95
# 60.125_5.375,01-Sep-0081,26.75
# ...
df = pd.read_csv("OISST_60E_72E_5N_20N.csv")

# -----------------------------
# Step 1: Parse coordinates from 'id'
# -----------------------------
df[['lon','lat']] = df['id'].str.split('_', expand=True).astype(float)

# -----------------------------
# Step 2: Filter for a single date (01-Sep-1981)
# -----------------------------
date_filter = "01-Sep-0081"   # matches your formatting
df_day = df[df['date'] == date_filter]

# -----------------------------
# Step 3: Pivot to make 2D grid
# -----------------------------
pivot = df_day.pivot_table(index='lat', columns='lon', values='sst')

lons = pivot.columns.values
lats = pivot.index.values
sst = pivot.values

# -----------------------------
# Step 4: Plot with Cartopy
# -----------------------------
plt.figure(figsize=(12,6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_global()

# Add coastlines & features
ax.coastlines()
ax.add_feature(cfeature.BORDERS, linewidth=0.5)
ax.add_feature(cfeature.LAND, facecolor="lightgray")

# Plot heatmap
mesh = ax.pcolormesh(lons, lats, sst, transform=ccrs.PlateCarree(), cmap="coolwarm")

# Colorbar
cbar = plt.colorbar(mesh, orientation="horizontal", pad=0.05, aspect=50)
cbar.set_label("Sea Surface Temperature (°C)")

plt.title("OISST - Sea Surface Temperature\n1 September 1981")
plt.show()
