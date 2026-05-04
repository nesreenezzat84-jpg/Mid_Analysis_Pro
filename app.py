import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Medical No Show Dashboard", layout="wide")
st.title("Medical No Show Dashboard")

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "KaggleV2-May-2016.csv"

df = pd.read_csv(DATA_PATH)

df.columns = df.columns.str.lower().str.replace("-", "_")
df.rename(columns={"hipertension": "hypertension"}, inplace=True)

df["no_show"] = df["no_show"].map({"Yes": 1, "No": 0})

fig = px.histogram(df, x="no_show", title="Show vs No-show")
st.plotly_chart(fig, width='stretch')

fig2 = px.box(df, x="no_show", y="age", title="Age vs No-show")
st.plotly_chart(fig2, width='stretch')