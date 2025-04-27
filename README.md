# Crime Data Visualization

## 📖 About the Project
This project presents a comprehensive dashboard to analyze and visualize crime data reported on the Bloomington campus. Using interactive and animated plots, we identify crime patterns, hotspots, trends, and case outcomes in an intuitive and accessible format.

The dashboard is built using Python, Streamlit, Kepler, and Plotly, designed for both academic presentation and practical insight into campus safety.

---

## 📊 About the Dataset
The dataset consists of preprocessed crime incident reports from Bloomington campus security logs.  
It contains fields such as:
- Date and time of reporting
- Crime type
- Case status
- Location of incident
- Other contextual details

The dataset has been cleaned, structured, and prepared for time series, categorical, and spatial analysis.

---

## 🛠️ Methodologies
- **Data Preprocessing**: Cleaned and standardized time, location, and categorical attributes.
- **Time Series Analysis**: Identified daily, monthly, and seasonal crime patterns.
- **Spatial Visualization**: Mapped crime occurrences using static and interactive maps.
- **Categorical Aggregations**: Grouped crimes by type and case status for flow analysis.
- **Interactive Dashboard**: Built a full web application to explore the visualizations dynamically.

---

## 📈 Visualizations Used & Inferences

| Visualization | Description | Key Inference |
|:--------------|:-------------|:--------------|
| **Animated Daily Crime Timeline** | Shows the daily reporting pattern over time. | Major spikes in crime reports align with campus events and breaks. |
| **Animated Monthly Crime Type Trends** | Monthly frequency of top crime types. | Certain crime types show seasonal variation, peaking in specific months. |
| **Animated Sankey Diagram (Crime Type to Outcome Flow)** | Tracks flow from crime types to case statuses. | Some crime types are more likely to be closed while others remain open or referred. |
| **Top 5 Crime Types Bar Chart** | Highlights the most reported crime categories. | Larceny and property crimes dominate the incident reports. |
| **Top 5 Crime Locations Bar Chart** | Shows the locations with highest number of reports. | Student housing and public parking areas are critical hotspots. |
| **3D Interactive Crime Location Map (Kepler.gl)** | Plots crime locations in 3D. | Crimes cluster heavily around main campus entry points and residential hubs. |
| **Crime Density Heatmap** | Visualizes zones with highest crime concentration. | Confirms repeat activity near popular student zones. |
| **Static Geospatial Radar Map** | Provides an alternative static view of spatial crime distribution. | Supports identification of consistent crime-prone zones. |

---

## 🌟 Impact
- Helps campus safety teams identify high-risk areas and times.
- Allows administrators and policymakers to allocate resources strategically.
- Aids awareness campaigns by showcasing seasonal and location-based patterns.
- Provides a real-world example of combining **data science + visualization** for actionable insights.

---

## 🚀 How to Use

1. Clone this repository or download the files.
2. Ensure you have the following Python libraries installed: `pip install streamlit pandas plotly folium mpld3 keplergl`
3. Run the Streamlit application using: `streamlit run crime_dashboard_app.py`
4. The dashboard will open automatically in your web browser.  
You can interact with the visualizations, explore trends, and download the dataset.

> **Note:** You must have the preprocessed dataset and all HTML visualization files in the specified folders (`visualizations/`) for full functionality.

---

## 👩‍💻 Authors
- Aryan Ahuja
- Freny Reji
- Neha Kothavade
- Vanshika Kapur

---

# 🏛️ Indiana University Bloomington | Spring 2025
 
