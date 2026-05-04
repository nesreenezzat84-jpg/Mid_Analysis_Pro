import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Medical No Show Dashboard", layout="wide")
st.title("Medical No Show Dashboard")

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "KaggleV2-May-2016.csv"

df = pd.read_csv(DATA_PATH)

# Data preprocessing
df.columns = df.columns.str.strip().str.lower().str.replace("-", "_")
df.rename(columns={"hipertension": "hypertension"}, inplace=True)

df['scheduledday'] = pd.to_datetime(df['scheduledday'])
df['appointmentday'] = pd.to_datetime(df['appointmentday'])

df = df[df['age'] >= 0]

df['waiting_days'] = (df['appointmentday'] - df['scheduledday']).dt.days
df = df[df['waiting_days'] >= 0]

df.drop_duplicates(inplace=True)

df["no_show"] = df["no_show"].map({"Yes": 1, "No": 0})

# Graphs
st.header("No-Show Analysis")

col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(df, x="no_show", title="Show (0) vs No-show (1)")
    st.plotly_chart(fig, width='stretch')

with col2:
    fig2 = px.box(df, x="no_show", y="age", title="Age vs No-show")
    st.plotly_chart(fig2, width='stretch')

st.header("Demographic Factors")

col3, col4 = st.columns(2)

with col3:
    fig3 = px.histogram(df, x='sms_received', color='no_show', barmode='group', title="SMS Received vs No-show")
    st.plotly_chart(fig3, width='stretch')

with col4:
    fig4 = px.histogram(df, x='gender', color='no_show', barmode='group', title="Gender vs No-show")
    st.plotly_chart(fig4, width='stretch')

st.header("Health Conditions")

col5, col6 = st.columns(2)

with col5:
    fig5 = px.histogram(df, x='hypertension', color='no_show', barmode='group', title="Hypertension vs No-show")
    st.plotly_chart(fig5, width='stretch')

with col6:
    fig7 = px.histogram(df, x='diabetes', color='no_show', barmode='group', title="Diabetes vs No-show")
    st.plotly_chart(fig7, width='stretch')

col7, col8 = st.columns(2)

with col7:
    fig8 = px.histogram(df, x='alcoholism', color='no_show', barmode='group', title="Alcoholism vs No-show")
    st.plotly_chart(fig8, width='stretch')

with col8:
    fig9 = px.histogram(df, x='handcap', color='no_show', barmode='group', title="Handicap vs No-show")
    st.plotly_chart(fig9, width='stretch')

st.header("Socioeconomic Factors")

fig10 = px.histogram(df, x='scholarship', color='no_show', barmode='group', title="Scholarship vs No-show")
st.plotly_chart(fig10, width='stretch')

st.header("Geographic Distribution")

fig11 = px.histogram(df, x='neighbourhood', color='no_show', barmode='group', title="Neighbourhood vs No-show")
st.plotly_chart(fig11, width='stretch')

st.header("Appointment Scheduling")

fig6 = px.histogram(df, x='waiting_days', nbins=30, title="Waiting Days Distribution")
st.plotly_chart(fig6, width='stretch')

