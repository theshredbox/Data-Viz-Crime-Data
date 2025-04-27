import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components
import base64

# --- Page Setup ---
st.set_page_config(page_title="Crime Data Dashboard - Bloomington Campus", layout="wide")

# --- Custom Background Only (No container) ---
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    css = f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    html, body, [class*="css"] {{
        font-family: 'Segoe UI', sans-serif;
        color: white;
        background-color: transparent;
    }}
    h1, h2, h3 {{
        color: white;
        text-align: center;
    }}
    .subtitle {{
        text-align: center;
        font-size: 1.1rem;
        color: #cccccc;
        margin-bottom: 2rem;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# --- Load Background ---
add_bg_from_local("iu_logo.jpg")

# --- Load Dataset ---
df = pd.read_csv("preprocessed_crime_dataset.csv")
df['datetime'] = pd.to_datetime(df['datetime'])
df['Month'] = df['datetime'].dt.to_period("M").astype(str)
df['Hour'] = df['datetime'].dt.hour
df['Weekday'] = df['datetime'].dt.day_name()

# --- Title and Subtitle ---
st.title("Crime Data Dashboard - Bloomington Campus")
st.markdown('<div class="subtitle">This dashboard presents a comprehensive analysis of campus crime data, focusing on temporal patterns, crime types, locations, and case outcomes.</div>', unsafe_allow_html=True)
st.write("---")

# --- Quick Insights ---
st.header("Quick Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Month with Most Crimes", df['Month'].value_counts().idxmax())

with col2:
    st.metric("Most Common Crime Type", df['Crime Type'].value_counts().idxmax())

with col3:
    st.metric("Most Common Case Status", df['Status'].value_counts().idxmax())

st.write("---")

# --- Explore the Dataset ---
st.header("Explore the Dataset")

# --- Top 5 Locations ---
st.subheader("Top 5 Locations with Highest Crime Reports")

top_locations = df['Location'].value_counts().head(5)

fig_top_locations = px.bar(
    x=top_locations.index,
    y=top_locations.values,
    labels={'x': 'Location', 'y': 'Number of Incidents'},
    title="Top 5 Locations",
    color_discrete_sequence=['red']
)

fig_top_locations.update_layout(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font_color='white',
    title_font_color='white',
    xaxis_title_font=dict(color='white'),
    yaxis_title_font=dict(color='white')
)
st.plotly_chart(fig_top_locations, use_container_width=True)

st.markdown("_Inference:_ The most reported incidents occurred near major student housing and parking facilities.")

st.write("---")

# --- Visualizations Section ---
st.header("Crime Visualizations")

# --- Animated Daily Crime Timeline ---
st.subheader("Animated Daily Crime Frequency Timeline")
with open(r"C:\Users\Aryan\PycharmProjects\DataViz\visualizations\animated_crime_timeline.html", "r", encoding="utf-8") as f:
    timeline_html = f.read()
components.html(timeline_html, height=650, scrolling=True)
st.markdown("_Inference:_ Highlights periods of peak crime reporting, often aligned with major campus activities.")

st.write("---")

# --- Animated Monthly Crime Type Trends ---
st.subheader("Animated Monthly Crime Type Trends")
with open(r"C:\Users\Aryan\PycharmProjects\DataViz\visualizations\animated_crime_type_bar.html", "r", encoding="utf-8") as f:
    crime_type_html = f.read()
components.html(crime_type_html, height=650, scrolling=True)
st.markdown("_Inference:_ Monthly patterns suggest seasonal crime trends and effectiveness of interventions.")

st.write("---")

# --- Animated Crime Type to Outcome Flow (Sankey) ---
st.subheader("Crime Type to Case Outcome Flow (Animated Sankey)")
with open(r"C:\Users\Aryan\PycharmProjects\DataViz\visualizations\animated_sankey.html", "r", encoding="utf-8") as f:
    sankey_html = f.read()
components.html(sankey_html, height=650, scrolling=True)
st.markdown("_Inference:_ Visualizes resolution pathways from reported crime to final status outcomes.")

st.write("---")

# --- 3D Interactive Crime Location Map ---
st.subheader("3D Interactive Crime Location Map")
with open(r"C:\Users\Aryan\PycharmProjects\DataViz\visualizations\crime_data_kepler.html", "r", encoding="utf-8") as f:
    map_html = f.read()
components.html(map_html, height=650, scrolling=True)
st.markdown("_Inference:_ Highlights hotspots and emerging clusters of activity across campus locations.")

st.write("---")

# --- Crime Density Heatmap ---
st.subheader("Crime Density Heatmap")
with open(r"C:\Users\Aryan\PycharmProjects\DataViz\visualizations\crime_heatmap.html", "r", encoding="utf-8") as f:
    heatmap_html = f.read()
components.html(heatmap_html, height=650, scrolling=True)
st.markdown("_Inference:_ Confirms highest-density regions for strategic safety initiatives.")

st.write("---")

# --- Static Geospatial Crime Map ---
st.subheader("Animated Radar Plot")
with open(r"C:\Users\Aryan\PycharmProjects\DataViz\visualizations\radar_plot.html", "r", encoding="utf-8") as f:
    static_html = f.read()
components.html(static_html, height=650, scrolling=True)
st.markdown("_Inference:_ Mapping corroborates hotspot patterns with dynamic analytics.")

st.write("---")

# --- Download Section ---
st.header("Download Dataset")

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download Preprocessed Crime Dataset",
    data=csv,
    file_name='preprocessed_crime_dataset.csv',
    mime='text/csv',
)

# --- Footer ---
# --- Footer ---
st.write("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 18px; padding: 10px;">
        <strong>Made with care by:</strong><br><br>
        <ul style="list-style-position: inside; text-align: left; display: inline-block;">
            <li>Aryan Ahuja</li>
            <li>Freny Reji</li>
            <li>Neha Kothavade</li>
            <li>Vanshika Kapur</li>
        </ul>
        <br>
        Indiana University Bloomington | Powered by Streamlit
    </div>
    """, unsafe_allow_html=True
)

