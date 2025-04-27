import pandas as pd
import plotly.express as px

# --- Load & Preprocess Dataset ---
df = pd.read_csv("preprocessed_crime_dataset.csv")

# Ensure correct datetime format
df["datetime"] = pd.to_datetime(df["datetime"])

# Extract Month for animation frames
df["Month"] = df["datetime"].dt.to_period("M").astype(str)

# --- 1. Animated Bar Chart: Crime Type Frequency Over Time ---
# Group by Crime Type and Month
bar_data = df.groupby(["Month", "Crime Type"]).size().reset_index(name="Frequency")

# Create animated bar chart
fig_bar = px.bar(
    bar_data,
    x="Crime Type",
    y="Frequency",
    color="Crime Type",
    animation_frame="Month",
    animation_group="Crime Type",
    title="Animated Bar Chart: Crime Type Frequency Over Time",
    range_y=[0, bar_data["Frequency"].max() + 10],
    template="plotly_white"
)

# Sort bars within each frame
fig_bar.update_layout(xaxis={'categoryorder': 'total descending'})

# Show and Save
fig_bar.show()
fig_bar.write_html("animated_crime_type_bar.html")
print("✅ Saved: animated_crime_type_bar.html")


# --- 2. Animated Time Series: Crime Frequency Over Time by Type ---
# Group by datetime and Crime Type
time_data = df.groupby(["datetime", "Crime Type"]).size().reset_index(name="Frequency")

# Create animated line chart
fig_line_animated = px.line(
    time_data,
    x="datetime",
    y="Frequency",
    color="Crime Type",
    title="Animated Crime Frequency Timeline (by Crime Type)",
    labels={"datetime": "Date", "Frequency": "Number of Crimes"},
    animation_frame="Crime Type",
    template="simple_white"
)

fig_line_animated.update_layout(
    font=dict(size=14),
    title_font=dict(size=22),
    plot_bgcolor='white',
    hovermode="x unified"
)

# Show and Save
fig_line_animated.show()
fig_line_animated.write_html("animated_crime_timeline.html")
print("✅ Saved: animated_crime_timeline.html")


# --- 3. Static Line Chart: Daily Crime Frequency Trend ---
# Group only by Date
daily_data = df.groupby(df["datetime"].dt.date).size().reset_index(name="Frequency")

# Create simple daily trend line chart
fig_daily = px.line(
    daily_data,
    x="datetime",
    y="Frequency",
    title="Daily Crime Frequency Trend",
    labels={"datetime": "Date", "Frequency": "Number of Crimes"},
    template="plotly_white"
)

fig_daily.update_traces(mode='lines+markers')  # Adds points
fig_daily.update_layout(
    font=dict(size=14),
    title_font=dict(size=22),
    plot_bgcolor='white',
    hovermode="x unified"
)

# Show and Save
fig_daily.show()
fig_daily.write_html("daily_crime_trend.html")
print("✅ Saved: daily_crime_trend.html")
