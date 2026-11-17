# HostelMeal — Dinner Demand Forecasting

A dinner-only prototype exploring whether menu and weekday information can help estimate attendance at the main hostel mess and demand at a separate night canteen.

## Scope
- Main mess dinner attendance.
- Separate night canteen dinner visits, including its operating period from mess dinner time until 3 AM. For reliable analysis, define a dinner window and distinguish post-dinner late-night visits.
- Separate menus for the two locations.
- Approximate hostel population: 1,500 (user-provided).

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Important data provenance
`sample_data_synthetic.csv` is synthetic and for development/testing only. It is not valid assignment fieldwork. The five user-reported figures are stored in `reported_observations_unverified.csv`; confirm whether they are main-mess counts or combined counts and how they were measured before including them in model training.

## Model
A transparent baseline ranks historical dinner records using menu word overlap, weekday match and veg/non-veg match, then averages the closest records. It separately estimates mess attendance and canteen visits. This is not a validated machine-learning model.

## Limitations
- Word overlap is not semantic food-preference understanding.
- Canteen visits may include repeat visits by the same student.
- Occupancy, exams, holidays, special events, price, service quality and stockouts are not yet modeled.
- Food quantity estimation requires recipe/portion and wastage data.
- Do not report accuracy until testing on real held-out observations.

## Assignment completion checklist
- [ ] First commit: research.md within first hour
- [ ] Two real sources read and annotated
- [ ] Two existing solutions researched for the actual staff member
- [ ] At least 20 genuine dinner observations in data.csv
- [ ] 20-minute field observation, two timestamped photos, interview
- [ ] Reflection written personally without AI
- [ ] At least five meaningful commits spread across the day
- [ ] AI chats exported to ai-chats/
- [ ] Three-minute screen recording linked here
