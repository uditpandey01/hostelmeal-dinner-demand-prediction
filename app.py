import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="HostelMeal Dinner Forecast", page_icon="🍽️", layout="wide")
st.title("🍽️ HostelMeal — Dinner Demand Forecast")
st.caption("Dinner-only attendance planning for the main mess and separate night canteen")

st.warning("DEMO MODE: All rows in the bundled sample dataset are synthetic. Replace them with personally collected observations before submission.")

@st.cache_data
def load_data():
    return pd.read_csv(Path(__file__).parent / "sample_data_synthetic.csv")

df = load_data()
st.sidebar.header("Tomorrow's dinner")
weekday = st.sidebar.selectbox("Day", ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
day_type = st.sidebar.selectbox("Mess dinner type", ["Veg","Non-veg"])
mess_menu = st.sidebar.text_area("Main mess dinner menu", "rice, dal, seasonal vegetables, roti")
canteen_menu = st.sidebar.text_area("Night canteen dinner menu", "noodles, egg roll, fried rice")

def similarity(a, b):
    a = set(str(a).lower().replace(",", " ").split())
    b = set(str(b).lower().replace(",", " ").split())
    return len(a & b) / len(a | b) if a | b else 0.0

def estimate(data, menu_col, target_col, menu, weekday, day_type, k=5):
    pool = data.copy()
    pool["menu_similarity"] = pool[menu_col].apply(lambda x: similarity(menu, x))
    pool["weekday_match"] = (pool["weekday"] == weekday).astype(int)
    pool["day_type_match"] = (pool["day_type"] == day_type).astype(int)
    pool["score"] = 0.65*pool["menu_similarity"] + 0.25*pool["weekday_match"] + 0.10*pool["day_type_match"]
    nearest = pool.sort_values("score", ascending=False).head(k)
    return round(nearest[target_col].mean()), nearest

mess_est, mess_rows = estimate(df, "mess_dinner_menu", "mess_attendance", mess_menu, weekday, day_type)
canteen_est, canteen_rows = estimate(df, "canteen_dinner_menu", "canteen_visits", canteen_menu, weekday, day_type)

c1,c2,c3=st.columns(3)
c1.metric("Predicted main mess attendance", f"{mess_est:,}")
c2.metric("Predicted night canteen visits", f"{canteen_est:,}")
c3.metric("Hostel population reference", "≈1,500")

st.subheader("Comparable historical demo records")
left,right=st.columns(2)
with left:
    st.markdown("**Main mess**")
    st.dataframe(mess_rows[["date","weekday","mess_dinner_menu","mess_attendance","menu_similarity"]], use_container_width=True)
with right:
    st.markdown("**Night canteen**")
    st.dataframe(canteen_rows[["date","weekday","canteen_dinner_menu","canteen_visits","menu_similarity"]], use_container_width=True)

st.subheader("Dinner attendance pattern in demo data")
st.bar_chart(df.groupby("weekday")[["mess_attendance","canteen_visits"]].mean())

st.subheader("Limitations")
st.markdown("""
- Synthetic data is only for testing the interface and code.
- Menu matching uses simple word overlap; it does not understand taste or dish quality.
- Canteen visits are visits/transactions, not necessarily unique students.
- Main mess and canteen counts must be collected using consistent, documented methods.
- Five reported dinner figures are kept separately until their location/counting scope is confirmed.
- Do not claim prediction accuracy until evaluated against real held-out observations.
""")
