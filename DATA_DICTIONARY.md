# Data dictionary (8 columns)

| Column | Meaning |
|---|---|
| `date` | Date of the dinner observation |
| `weekday` | Day of the week |
| `day_type` | Veg or Non-veg classification of the main mess menu |
| `mess_dinner_menu` | Main mess dinner menu |
| `canteen_dinner_menu` | Separate night-canteen menu |
| `mess_attendance` | Main mess dinner attendance count |
| `canteen_visits` | Night-canteen visits/transactions; not necessarily unique students |
| `notes` | Context and data provenance |

**Important:** Current rows in `data.csv` are synthetic examples for implementation/testing only. Replace them with at least 20 personally collected real observations before assignment submission. Keep counts separate by location and use a consistent counting method. If you need to distinguish dinner-time from post-dinner visits until 3 AM later, add a time-slot column only after discussing the scope with the canteen operator.
