# animated_sankey.py

import plotly.graph_objects as go
import pandas as pd
import numpy as np

# --- Load Dataset ---
df = pd.read_csv(r'C:\Users\Aryan\PycharmProjects\DataViz\preprocessed_crime_dataset.csv')

# --- Prepare Data ---
df["datetime"] = pd.to_datetime(df["datetime"])
df["Month"] = df["datetime"].dt.to_period("M").astype(str)

sankey_data = df.groupby(["Month", "Crime Type", "Status"]).size().reset_index(name="Count")

labels = list(pd.unique(sankey_data['Crime Type'].tolist() + sankey_data['Status'].tolist()))
label_indices = {label: i for i, label in enumerate(labels)}
months = sorted(sankey_data["Month"].unique())

# --- Define Color Palette ---
cosmic_palette = [
    (138, 43, 226), (0, 255, 255), (255, 105, 180), (30, 144, 255), (0, 206, 209),
    (255, 165, 0), (148, 0, 211), (255, 20, 147), (135, 206, 250), (72, 61, 139)
]

crime_types = sankey_data["Crime Type"].unique()
base_colors = {crime: cosmic_palette[i % len(cosmic_palette)] for i, crime in enumerate(crime_types)}

frames = []
all_sources, all_targets, all_values = [], [], []
bloom_steps = 5

# --- Build Animation Frames ---
for idx, month in enumerate(months):
    month_data = sankey_data[sankey_data["Month"] == month]
    month_sources = month_data['Crime Type'].map(label_indices).tolist()
    month_targets = month_data['Status'].map(label_indices).tolist()
    month_values = month_data['Count'].tolist()

    for bloom in range(1, bloom_steps + 1):
        bloom_sources = all_sources + month_sources
        bloom_targets = all_targets + month_targets
        bloom_values = all_values + month_values

        frame_colors = []
        for i in range(len(bloom_sources)):
            source_idx = bloom_sources[i]
            source_label = labels[source_idx] if source_idx < len(labels) else None
            r, g, b = base_colors.get(source_label, (0, 191, 255))
            alpha = 0.3 + 0.7 * (bloom / bloom_steps)
            frame_colors.append(f"rgba({int(r)},{int(g)},{int(b)},{alpha:.2f})")

        frame = go.Frame(
            data=[go.Sankey(
                arrangement="snap",
                node=dict(
                    pad=20,
                    thickness=30,
                    line=dict(color="black", width=0.5),
                    label=labels,
                    color="rgba(20,20,20,0.95)"
                ),
                link=dict(
                    source=bloom_sources,
                    target=bloom_targets,
                    value=bloom_values,
                    color=frame_colors
                )
            )],
            name=f"{month} - bloom {bloom}"
        )
        frames.append(frame)

    all_sources += month_sources
    all_targets += month_targets
    all_values += month_values

# --- Initialize First Frame ---
initial_sources = sankey_data[sankey_data["Month"] == months[0]]['Crime Type'].map(label_indices).tolist()
initial_targets = sankey_data[sankey_data["Month"] == months[0]]['Status'].map(label_indices).tolist()
initial_values = sankey_data[sankey_data["Month"] == months[0]]['Count'].tolist()

initial_colors = []
for src in initial_sources:
    label = labels[src]
    r, g, b = base_colors.get(label, (0, 191, 255))
    initial_colors.append(f"rgba({int(r)},{int(g)},{int(b)},0.3)")

# --- Create Figure ---
fig = go.Figure(
    data=[go.Sankey(
        arrangement="snap",
        node=dict(
            pad=20,
            thickness=30,
            line=dict(color="black", width=0.5),
            label=labels,
            color="rgba(20,20,20,0.95)"
        ),
        link=dict(
            source=initial_sources,
            target=initial_targets,
            value=initial_values,
            color=initial_colors
        )
    )],
    frames=frames
)

fig.update_layout(
    font=dict(size=14, color='white'),
    plot_bgcolor='black',
    paper_bgcolor='black',
    height=750,
    width=1200,
    updatemenus=[dict(
        type="buttons",
        showactive=False,
        buttons=[dict(label="▶️ Bloom", method="animate", args=[None, {
            "frame": {"duration": 1200, "redraw": True},
            "fromcurrent": True,
            "transition": {"duration": 1000, "easing": "linear"}
        }])]
    )],
    sliders=[dict(
        steps=[dict(method="animate", args=[[f"{month} - bloom {bloom}"], {"frame": {"duration": 1200, "redraw": True}, "mode": "immediate"}], label=f"{month} - {bloom}") for month in months for bloom in range(1, bloom_steps+1)],
        transition={"duration": 1000},
        x=0.1,
        len=0.8
    )]
)

# --- Display the Figure ---
fig.show()

# --- Save as HTML ---
fig.write_html("animated_sankey.html")

print("Animated Sankey diagram saved as 'animated_sankey.html'.")