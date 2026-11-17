from pathlib import Path

import pandas as pd
import streamlit as st

from predictor import predict_dinner

st.set_page_config(page_title="HostelMeal Dinner Forecast", page_icon="🍽️", layout="wide")
st.title("🍽️ HostelMeal — Dinner Demand Forecast")
st.caption("Menu-based planning for main-mess dinner and the separate night canteen.")

DATA_PATH = Path(__file__).parent / "data.csv"

@st.cache_data
def load_data(path: str, modified: float) -> pd.DataFrame:
    return pd.read_csv(path)

try:
    df = load_data(str(DATA_PATH), DATA_PATH.stat().st_mtime)
except FileNotFoundError:
    st.error("data.csv was not found. Keep it in the same folder as app.py.")
    st.stop()
except Exception as exc:
    st.error(f"Could not read data.csv: {exc}")
    st.stop()

synthetic = (
    "notes" in df.columns
    and df["notes"].fillna("").astype(str).str.contains("SYNTHETIC SAMPLE ONLY", case=False).any()
)
if synthetic:
    st.warning(
        "DEMO MODE: data.csv currently contains synthetic sample rows. "
        "Use this only to test the app. Replace them with your own real observations before submission."
    )

st.sidebar.header("Upcoming dinner")
weekday = st.sidebar.selectbox(
    "Weekday",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
)
day_type = st.sidebar.selectbox("Dinner type", ["Veg", "Non-veg"])
mess_menu = st.sidebar.text_area(
    "Main mess dinner menu",
    "rice, dal, seasonal vegetables, roti",
)
canteen_menu = st.sidebar.text_area(
    "Night canteen dinner menu",
    "noodles, egg roll, fried rice",
)
k = st.sidebar.slider("Similar past records to use", min_value=1, max_value=10, value=5)

if st.sidebar.button("Predict dinner demand", type="primary"):
    try:
        estimates, matches, warnings = predict_dinner(
            df, weekday, day_type, mess_menu, canteen_menu, k
        )
        st.subheader("Estimated dinner demand")
        col1, col2 = st.columns(2)
        col1.metric("Main mess attendance", f'{estimates["mess_attendance"]:,} students')
        col2.metric("Night canteen activity", f'{estimates["canteen_visits"]:,} visits')

        st.caption(
            "These are estimates from the closest matching rows, not guaranteed counts. "
            "Canteen visits may include repeat visits and are not unique students unless deduplicated."
        )
        if warnings:
            st.warning("Data quality: " + " ".join(warnings))

        left, right = st.columns(2)
        with left:
            st.markdown("**Closest main-mess records**")
            st.dataframe(
                matches["mess"][[
                    "date", "weekday", "mess_dinner_menu",
                    "mess_attendance", "similarity_score",
                ]],
                use_container_width=True,
                hide_index=True,
            )
        with right:
            st.markdown("**Closest night-canteen records**")
            st.dataframe(
                matches["canteen"][[
                    "date", "weekday", "canteen_dinner_menu",
                    "canteen_visits", "similarity_score",
                ]],
                use_container_width=True,
                hide_index=True,
            )
    except ValueError as exc:
        st.error(str(exc))

st.divider()
st.subheader("Dataset overview")
st.write(f"Rows loaded: **{len(df)}**")
if "weekday" in df.columns:
    st.bar_chart(df.groupby("weekday")[["mess_attendance", "canteen_visits"]].mean())

st.subheader("How the estimate works")
st.markdown(
    """
    1. It compares the entered menu with each historical menu using word overlap.
    2. It adds points when the weekday and Veg/Non-veg type match.
    3. It averages the target counts from the top matching rows.

    **Scoring weights:** menu similarity 65%, weekday match 25%, dinner type match 10%.
    """
)
st.subheader("Limitations")
st.markdown(
    """
    - This is a transparent baseline, not a trained or accuracy-validated machine-learning model.
    - Similar words do not necessarily mean similar popularity, taste, or portion demand.
    - Predictions improve only when the CSV contains enough real, consistently measured observations.
    - Main-mess attendance and canteen visits are separate measures and must not be combined.
    - Canteen visits are not unique students unless the collection method deduplicates people.
    - The current dataset has no time-slot column, so it cannot separately forecast pre- and post-dinner canteen demand.
    """
)
