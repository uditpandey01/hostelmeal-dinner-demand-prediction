# HostelMeal — Dinner Demand Forecast

A dinner-only prototype for estimating main-mess attendance and separate night-canteen visits using the two menus and weekday.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Data
`data.csv` and `sample_data_synthetic.csv` currently contain 21 **synthetic sample rows** for implementation and testing. They are not real fieldwork and must be replaced with at least 20 personally collected observations before submission.

The CSV uses eight columns: `date`, `weekday`, `day_type`, `mess_dinner_menu`, `canteen_dinner_menu`, `mess_attendance`, `canteen_visits`, `notes`.

`canteen_visits` means visits/transactions, not necessarily unique students. Main-mess attendance and canteen visits must remain separate. Confirm the counting method and what time window is included.

## Prediction approach
The prototype uses a simple menu-word overlap and weekday/day-type similarity baseline. It is an initial explainable approach, not a validated model. Evaluate it on real held-out data before claiming accuracy.

## Limitations
- Synthetic sample values do not represent measured hostel attendance.
- Menu word overlap cannot understand taste, quality or student preference.
- Canteen visits may include repeat visits.
- Holidays, exams, hostel occupancy, events, stockouts and other factors may affect demand.
- Food quantity prediction requires additional portion/recipe and leftover data.
