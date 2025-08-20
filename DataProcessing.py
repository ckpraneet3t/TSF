import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

df = pd.read_csv("OISST_60E_72E_5N_20N.csv")
df[['lon','lat']] = df['id'].str.split('_', expand=True).astype(float)
df_day = df[df['date'] == "01-Sep-0081"]

pivot = df_day.pivot_table(index='lat', columns='lon', values='sst')
lons = pivot.columns.values
lats = pivot.index.values
sst = pivot.values

plt.figure(figsize=(10,6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([60, 72, 5, 20], crs=ccrs.PlateCarree())
ax.coastlines(resolution="10m")
ax.add_feature(cfeature.LAND, facecolor="lightgray")

mesh = ax.pcolormesh(lons, lats, sst, transform=ccrs.PlateCarree(), cmap="coolwarm", shading="auto")
cbar = plt.colorbar(mesh, orientation="horizontal", pad=0.05, aspect=40)
cbar.set_label("Sea Surface Temperature (°C)")

plt.title("OISST - SST\n1 September 1981")
plt.show()
