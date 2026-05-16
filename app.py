import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================================
# 1. ARCHITECTURE: PAGE CONFIG & STYLING
# =====================================================================
st.set_page_config(
    page_title="Global Terrorism Analytics Dashboard",
    page_icon="📊",
    layout="wide"  # Uses the entire screen width instead of a narrow column
)

# =====================================================================
# 2. PERFORMANCE: CACHED DATA PIPELINE (UPDATED FOR SAFETY)
# =====================================================================
@st.cache_data
def load_and_preprocess_data():
    import os
    
    # This automatically finds the exact folder where your app.py is sitting
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "data", "processed data", "gtd_asia_cleaned.csv")
    
    # Fallback check to print a clear message in your terminal if the file is missing
    if not os.path.exists(DATA_PATH):
        print(f"\n❌ ERROR: System cannot find the dataset file at: {DATA_PATH}\n")
        
    df = pd.read_csv(DATA_PATH)
    df['Log_Total_Casualties'] = np.log1p(df['Killed'] + df['Wounded'])
    return df

df = load_and_preprocess_data()
# =====================================================================
# 3. INTERACTIVE LAYOUT: SIDEBAR FILTERS
# =====================================================================
st.sidebar.title("📌 Dashboard Controls")
st.sidebar.markdown("Filter the visual scopes dynamically:")

# Dynamic dropdown population from the dataset
countries = ["All Asian Countries"] + sorted(df['Country'].dropna().unique().tolist())
selected_country = st.sidebar.selectbox("Select Country/Region", countries)

# State Management: Filter dataframe based on user interaction
if selected_country != "All Asian Countries":
    filtered_df = df[df['Country'] == selected_country]
else:
    filtered_df = df

# =====================================================================
# 4. VIEW LAYOUT: MAIN UI & SUMMARY METRICS
# =====================================================================
st.title("📊 Global Terrorism Analysis Dashboard (Asia Focus)")
st.markdown(f"### Currently viewing: **{selected_country}** (1970–2017)")
st.markdown("---")

# High-Level KPI Summary Cards
metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric(label="Total Recorded Incidents", value=f"{len(filtered_df):,}")
with metric_col2:
    st.metric(label="Total Human Fatalities", value=f"{int(filtered_df['Killed'].sum()):,}")
with metric_col3:
    st.metric(label="Attack Success Rate", value=f"{(filtered_df['Success'].mean() * 100):.1f}%")

st.markdown("---")

# =====================================================================
# 5. DATA VISUALIZATION LAYER (COLUMNS)
# =====================================================================
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("📈 Chronological Attack Volatility")
    
    # Aggregate data for the native interactive line chart
    timeline_data = filtered_df.groupby('Year').size().reset_index(name='Incidents')
    
    # Streamlit native charts are fast, interactive, and hover-responsive
    st.line_chart(data=timeline_data, x='Year', y='Incidents', use_container_width=True)

with chart_col2:
    st.subheader("🎯 Top 5 Targeted Sectors")
    
    # Matplotlib/Seaborn visualization pipeline
    fig, ax = plt.subplots(figsize=(7, 4.5))
    target_counts = filtered_df['Target_Type'].value_counts().head(5)
    
    sns.barplot(x=target_counts.values, y=target_counts.index, ax=ax, palette="flare")
    ax.set_xlabel("Incident Absolute Count")
    ax.set_ylabel("")
    plt.tight_layout()
    
    # Explicitly pass the figure object to prevent rendering overlaps
    st.pyplot(fig)