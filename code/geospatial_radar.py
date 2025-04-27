#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# In[16]:




# In[18]:


# Load the dataset
df = pd.read_csv('preprocessed_crime_dataset.csv')
df


# #  Geospatial Heat Maps with folium
# ## Visualize where crimes are concentrated geographically — "hot spots" across a map.

# In[24]:


import folium
from folium.plugins import HeatMap

# Center the map (Bloomington, IN)
m = folium.Map(location=[39.1653, -86.5264], zoom_start=14)

# Add heat map (requires lat/lon values)
heat_data = df[['Latitude', 'Longitude']].dropna().values.tolist()
HeatMap(heat_data).add_to(m)

# Save or display
m.save("crime_heatmap.html")
m


# # Clustered Crime Markers with Popups (folium)
# ## See individual incidents with details

# In[30]:


from folium.plugins import MarkerCluster

# Initialize map
m = folium.Map(location=[39.1653, -86.5264], zoom_start=14)

# Add cluster markers
marker_cluster = MarkerCluster().add_to(m)

for _, row in df.iterrows():
    popup = f"{row['Crime Type']}<br>{row['Description']}<br>{row['Date Reported']}"
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=popup
    ).add_to(marker_cluster)

m 


# # Time-Animated Crime Heatmap (folium + HeatMapWithTime)
# ## Shows how crime intensity changes over time

# In[36]:


from folium.plugins import HeatMapWithTime

# Prepare data by grouping by Month
df["Date Reported"] = pd.to_datetime(df["Date Reported"])
df["Month"] = df["Date Reported"].dt.to_period("M").astype(str)

# Group by month into separate lists
monthly_data = []
months = sorted(df["Month"].unique())

for month in months:
    monthly_df = df[df["Month"] == month]
    monthly_points = monthly_df[['Latitude', 'Longitude']].dropna().values.tolist()
    monthly_data.append(monthly_points)

# Create animated heatmap
m = folium.Map(location=[39.1653, -86.5264], zoom_start=14)
HeatMapWithTime(monthly_data, index=months, radius=10, auto_play=True).add_to(m)

m


# # Radar Plot (Polar Chart) with plotly
# ## Show distribution of crime types in a way that highlights extremes and balance across categories.

# In[26]:


import plotly.express as px

# Count of each crime type
crime_counts = df['Crime Type'].value_counts().reset_index()
crime_counts.columns = ['Crime Type', 'Count']

# Plot radar chart
fig = px.line_polar(crime_counts, r='Count', theta='Crime Type',
                    line_close=True, title="Crime Type Distribution",
                    template='plotly_dark')
fig.show()


# # Animated Crime Type Trends Over Time with plotly.express

# In[28]:


import pandas as pd
import plotly.express as px

# Prepare time column
df["Date Reported"] = pd.to_datetime(df["Date Reported"])
df["Month"] = df["Date Reported"].dt.to_period("M").astype(str)

# Group by Month and Crime Type
animated_data = df.groupby(["Month", "Crime Type"]).size().reset_index(name="Count")

# Create animated polar bar plot
fig = px.bar_polar(
    animated_data,
    r="Count",
    theta="Crime Type",
    color="Crime Type",
    animation_frame="Month",
    title="Animated Crime Type Trends Over Time",
    template="plotly_dark",
    range_r=[0, animated_data["Count"].max() + 10]
)

fig.show()


# In[ ]:




