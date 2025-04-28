# Dehumanization Escalation Monitoring Dashboard
# Run: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title='Dehumanization Escalation Dashboard', layout='wide')

# Sidebar
st.sidebar.title('Navigation')
option = st.sidebar.radio("Select View:", ["Overview", "Heatmap", "Theme Tracker", "Forecast", "Word Cloud"])

# Simulated Data (Replace with real data feeds)
dates = pd.date_range('2024-01-01', periods=52, freq='W')
data = pd.DataFrame({
    'Date': dates,
    'China-Taiwan': np.clip(np.linspace(40, 90, 52) + np.random.randn(52)*3, 0, 100),
    'India-Pakistan': np.clip(np.linspace(30, 55, 52) + np.random.randn(52)*3, 0, 100),
    'China-Philippines': np.clip(np.linspace(20, 50, 52) + np.random.randn(52)*3, 0, 100)
})

# Overview
if option == "Overview":
    st.title('Dehumanization Intensity Trends')
    fig = px.line(data, x='Date', y=['China-Taiwan', 'India-Pakistan', 'China-Philippines'],
                  labels={'value': 'Intensity Index', 'Date': 'Week'},
                  title='Dehumanizing Language Intensity Over Time')
    st.plotly_chart(fig, use_container_width=True)

# Heatmap
elif option == "Heatmap":
    st.title('Event-Rhetoric Heatmap')
    heatmap_data = pd.DataFrame(np.random.randint(0, 3, (3, 12)),
                                index=['China-Taiwan', 'India-Pakistan', 'China-Philippines'],
                                columns=[f'Month {i+1}' for i in range(12)])
    fig = px.imshow(heatmap_data, color_continuous_scale='Reds',
                    labels=dict(x="Month", y="Conflict", color="Event Intensity"),
                    title="Heatmap of Real-World Event Intensity")
    st.plotly_chart(fig, use_container_width=True)

# Theme Tracker
elif option == "Theme Tracker":
    st.title('Top Dehumanizing Themes')
    themes = ['Purification', 'Traitors', 'Tumors', 'Infestation', 'Purge']
    mentions = np.random.randint(50, 200, size=len(themes))
    theme_df = pd.DataFrame({'Theme': themes, 'Mentions': mentions})
    fig = px.bar(theme_df, x='Theme', y='Mentions', title='Top Aggressive Themes')
    st.plotly_chart(fig, use_container_width=True)

# Forecast
elif option == "Forecast":
    st.title('Escalation Forecast')
    forecast_dates = pd.date_range('2025-01-01', periods=12, freq='M')
    forecast_df = pd.DataFrame({
        'Date': forecast_dates,
        'China-Taiwan': np.clip(np.linspace(85, 98, 12), 0, 100),
        'India-Pakistan': np.clip(np.linspace(55, 65, 12), 0, 100),
        'China-Philippines': np.clip(np.linspace(50, 60, 12), 0, 100)
    })
    fig = px.line(forecast_df, x='Date', y=['China-Taiwan', 'India-Pakistan', 'China-Philippines'],
                  labels={'value': 'Forecast Intensity', 'Date': 'Month'},
                  title='12-Month Escalation Risk Forecast')
    st.plotly_chart(fig, use_container_width=True)

# Word Cloud
elif option == "Word Cloud":
    st.title('Dominant Dehumanizing Terms')
    conflict_choice = st.selectbox("Select Conflict", ["China-Taiwan", "India-Pakistan", "China-Philippines"])
    phrases = {
        "China-Taiwan": "separatists tumors traitors purification cleansing surgical malignant",
        "India-Pakistan": "terrorists extremists infiltrators cowards insurgents backstabbers",
        "China-Philippines": "trespassers violators sovereignty provocateurs troublemakers instigators"
    }
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(phrases[conflict_choice])
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
