# geospatial_radar.py

# Importing necessary libraries
import pandas as pd
import geopandas as gpd
import folium
from shapely.geometry import Point
import matplotlib.pyplot as plt
import mpld3

# --- Load Dataset ---
# Replace 'path_to_your_dataset.csv' with your actual CSV path
df = pd.read_csv(r'C:\Users\Aryan\PycharmProjects\DataViz\preprocessed_crime_dataset.csv')

# --- Display First Few Rows ---
print(df.head())

# --- Create GeoDataFrame ---
# Assuming your CSV has 'Longitude' and 'Latitude' columns
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# --- Plot Static Map ---
fig, ax = plt.subplots(figsize=(10, 8))
gdf.plot(ax=ax, marker='o', color='red', markersize=5)
plt.title("Geospatial Radar - Static Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Save static map as HTML using mpld3

html_static = mpld3.fig_to_html(fig)
with open("static_map.html", "w") as f:
    f.write(html_static)

plt.close(fig)

# --- Create Interactive Map with Folium ---
# Set a starting location (e.g., mean of the coordinates)
start_coords = (df['Latitude'].mean(), df['Longitude'].mean())
folium_map = folium.Map(location=start_coords, zoom_start=10)

# Add points to the map
for idx, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']],
                  popup=f"{row['Location']} ({row['Description']})").add_to(folium_map)

# Save the folium map as HTML
folium_map.save('interactive_map.html')

print("Static plot saved as 'static_map.html' and interactive map saved as 'interactive_map.html'.")
