import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Medical No Show Dashboard", layout="wide")
st.markdown("<h1 style='text-align: center; color: #12355B;'>🏥 Medical Appointment No-Show Dashboard</h1>",unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: gray;'>Interactive dashboard for analyzing patient attendance behavior</p>",unsafe_allow_html=True

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

total_appointments = len(df)
show_count = (df["no_show"] == 0).sum()
no_show_count = (df["no_show"] == 1).sum()
no_show_rate = round((no_show_count / total_appointments) * 100, 2)

st.header("📌 Key Metrics")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric("Total Appointments", total_appointments)
kpi2.metric("Show Count", show_count)
kpi3.metric("No-Show Count", no_show_count)
kpi4.metric("No-Show Rate", f"{no_show_rate}%")

# Graphs
st.header("No-Show Analysis")

col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(df,x="no_show",title="Show (0) vs No-show (1)",color="no_show",color_discrete_sequence=["#2A9D8F", "#E76F51"])
    st.plotly_chart(fig, width='stretch')

with col2:
    fig2 = px.box(df, x="no_show", y="age", title="Age vs No-show", color="no_show", color_discrete_sequence=["#2A9D8F", "#E76F51"] )
    st.plotly_chart(fig2, width='stretch')

st.header("Demographic Factors")

col3, col4 = st.columns(2)

with col3:
    fig3 = px.histogram(df, x='sms_received', color='no_show', barmode='group', title="SMS Received vs No-show", color_discrete_sequence=["#2A9D8F", "#E76F51"])
    st.plotly_chart(fig3, width='stretch')

with col4:
    fig4 = px.histogram(df, x='gender', color='no_show', barmode='group', title="Gender vs No-show", color_discrete_sequence=["#2A9D8F", "#E76F51"])
    st.plotly_chart(fig4, width='stretch')

st.header("Health Conditions")

col5, col6 = st.columns(2)

with col5:
    fig5 = px.histogram(df, x='hypertension', color='no_show', barmode='group', title="Hypertension vs No-show", color_discrete_sequence=["#2A9D8F", "#E76F51"])
    st.plotly_chart(fig5, width='stretch')

with col6:
    fig7 = px.histogram(df, x='diabetes', color='no_show', barmode='group', title="Diabetes vs No-show", color_discrete_sequence=["#2A9D8F", "#E76F51"])
    st.plotly_chart(fig7, width='stretch')

col7, col8 = st.columns(2)

with col7:
    fig8 = px.histogram(df, x='alcoholism', color='no_show', barmode='group', title="Alcoholism vs No-show", color_discrete_sequence=["#2A9D8F", "#E76F51"])
    st.plotly_chart(fig8, width='stretch')

with col8:
    fig9 = px.histogram(df, x='handcap', color='no_show', barmode='group', title="Handicap vs No-show", color_discrete_sequence=["#2A9D8F", "#E76F51"])
    st.plotly_chart(fig9, width='stretch')

st.header("Socioeconomic Factors")

fig10 = px.histogram(df, x='scholarship', color='no_show', barmode='group', title="Scholarship vs No-show", color_discrete_sequence=["#2A9D8F", "#E76F51"])
st.plotly_chart(fig10, width='stretch')

st.header("Geographic Distribution")

top_neighbourhoods = df['neighbourhood'].value_counts().head(10).index

filtered_df = df[df['neighbourhood'].isin(top_neighbourhoods)]

fig11 = px.histogram(filtered_df,x='neighbourhood',color='no_show',barmode='group',title="Top 10 Neighbourhoods vs No-show",color_discrete_sequence=["#2A9D8F", "#E76F51"])

st.plotly_chart(fig11, width='stretch')

st.header("Appointment Scheduling")

fig6 = px.histogram(df, x='waiting_days', nbins=30, title="Waiting Days Distribution")
st.plotly_chart(fig6, width='stretch')

st.markdown("---")

st.caption("Prepared by Nesreen | Data Analysis Mid Project")