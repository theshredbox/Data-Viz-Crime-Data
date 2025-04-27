import pandas as pd
import pydeck as pdk

# ✅ Your Mapbox token here
pdk.settings.mapbox_api_key = "pk.eyJ1IjoiYXJ5YW5haHVqYSIsImEiOiJjbTl3Z2VzaWwwdjZ6MmpvaHJ6Y2xkbnV5In0.TMT4HkO1bBDEwxT37SqrtQ"

# Load data
df = pd.read_csv("preprocessed_crime_dataset.csv")

# Compute centroids per Crime Type
crime_centroids = df.groupby("Crime Type")[["Latitude", "Longitude"]].mean().to_dict(orient="index")
df["source_lat"] = df["Crime Type"].map(lambda x: crime_centroids.get(x, {}).get("Latitude"))
df["source_lon"] = df["Crime Type"].map(lambda x: crime_centroids.get(x, {}).get("Longitude"))
df.dropna(subset=["source_lat", "source_lon", "Latitude", "Longitude"], inplace=True)

# Arc and Scatter layers
arc_layer = pdk.Layer("ArcLayer", df, get_source_position=["source_lon", "source_lat"],
                      get_target_position=["Longitude", "Latitude"], get_source_color=[255, 140, 0],
                      get_target_color=[0, 0, 255], auto_highlight=True, width_scale=0.0001,
                      width_min_pixels=1, get_width=5, pickable=True)

scatter_layer = pdk.Layer("ScatterplotLayer", df, get_position=["Longitude", "Latitude"],
                          get_fill_color=[0, 255, 255, 120], get_radius=20, radius_min_pixels=2,
                          radius_scale=1, pickable=True, elevation_scale=4, extruded=True)

view_state = pdk.ViewState(latitude=39.1653, longitude=-86.5264, zoom=12, pitch=60)

deck = pdk.Deck(layers=[scatter_layer, arc_layer],
                initial_view_state=view_state,
                tooltip={"text": "Crime: {Crime Type}\nLocation: {Location}\nStatus: {Status}"},
                map_style="mapbox://styles/mapbox/dark-v10")

deck.to_html("bloomington_crime_arcs.html")



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