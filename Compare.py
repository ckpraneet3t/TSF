import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

df = pd.read_csv("OISST_60E_72E_5N_20N.csv")
df[['lon','lat']] = df['id'].str.split('_', expand=True).astype(float)

dates = ["01-Sep-0081","02-Sep-0081","03-Sep-0081","04-Sep-0081","05-Sep-0081"]

fig, axes = plt.subplots(1, 5, figsize=(25,6), subplot_kw={'projection': ccrs.PlateCarree()})

for i, date in enumerate(dates):
    df_day = df[df['date'] == date]
    pivot = df_day.pivot_table(index='lat', columns='lon', values='sst')
    lons = pivot.columns.values
    lats = pivot.index.values
    sst = pivot.values
    ax = axes[i]
    ax.set_extent([60, 72, 5, 20], crs=ccrs.PlateCarree())
    ax.coastlines(resolution="10m")
    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    mesh = ax.pcolormesh(lons, lats, sst, transform=ccrs.PlateCarree(), cmap="coolwarm", shading="auto")
    ax.set_title(date)

cbar_ax = fig.add_axes([0.25, 0.08, 0.5, 0.02])
cbar = fig.colorbar(mesh, cax=cbar_ax, orientation="horizontal")
cbar.set_label("Sea Surface Temperature (°C)")

plt.show()
