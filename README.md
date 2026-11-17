# HostelMeal — Dinner Attendance & Demand Prediction

A simple menu-based prediction tool to help hostel mess staff estimate dinner attendance and night-canteen demand.

## 1. Problem Statement

In our hostel, approximately 1,500 students use the main mess and a separate night canteen.

Dinner attendance changes depending on the weekday and the food menu. When demand is estimated mainly through human judgement, the estimate can be inaccurate.

This can lead to excess food preparation, food wastage and financial loss.

HostelMeal aims to help mess staff make better dinner-planning decisions using historical menu and attendance data.

## 2. Field Research

- **Location:** Mega Mess
- **Visit date:** 18 November 2026
- **Person interviewed:** Tarun
- **Role:** Mess Supervisor

During the field visit, the supervisor highlighted three concerns:

1. Food is wasted.
2. Human-based estimates of demand can be inaccurate.
3. Inaccurate estimates can result in financial loss.

One surprising observation during the visit was that food wastage was higher than expected.

Fieldwork notes and photographs are included in the project repository.

## 3. Project Objectives

HostelMeal provides two separate dinner predictions:

- **Main mess:** Estimated dinner attendance.
- **Night canteen:** Estimated number of visits.

The project considers:
- Weekday
- Dinner type (Veg or Non-veg)
- Main-mess dinner menu
- Night-canteen dinner menu
- Historical attendance and visit counts

## 4. Dataset

The application reads data from `data.csv`.

The dataset contains eight columns:

| Column | Description |
|---|---|
| `date` | Observation date |
| `weekday` | Day of the week |
| `day_type` | Veg or Non-veg |
| `mess_dinner_menu` | Main-mess dinner menu |
| `canteen_dinner_menu` | Night-canteen dinner menu |
| `mess_attendance` | Recorded main-mess dinner attendance |
| `canteen_visits` | Recorded night-canteen visits |
| `notes` | Additional observations |

The dataset was collected through personal fieldwork and observations.

**Important:** Main-mess attendance and night-canteen visits are separate measures. Canteen visits should not be interpreted as unique students unless repeat visits have been identified and removed.

## 5. Technology Used

- Python
- Pandas
- Streamlit
- CSV

## 6. How the Prediction Works

HostelMeal uses a simple similarity-based prediction approach.

1. It compares the upcoming dinner menu with previously recorded menus.
2. It checks whether the weekday matches.
3. It checks whether the dinner type matches.
4. It ranks historical records using a similarity score.
5. It averages the target values from the closest matching records.

The scoring weights are:

| Factor | Weight |
|---|---:|
| Menu similarity | 65% |
| Weekday match | 25% |
| Veg/Non-veg match | 10% |

The application calculates main-mess attendance and night-canteen visits independently.

This is an explainable baseline prediction method, not a validated machine-learning model.

## 7. Installation and Setup

### Step 1: Clone the repository

```bash
git clone YOUR_PUBLIC_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder

```bash
cd hostelmeal_project
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 8. How to Use

1. Open the HostelMeal application.
2. Select the upcoming dinner weekday.
3. Select Veg or Non-veg.
4. Enter the main-mess dinner menu.
5. Enter the night-canteen dinner menu.
6. Select how many similar historical records to use.
7. Click **Predict dinner demand**.
8. View the separate predictions and matching historical records.

## 9. Sample Application Output

Add a screenshot of your working application here.

**Example format:**

- Main mess attendance: [Insert actual prediction]
- Night canteen visits: [Insert actual prediction]

These values should come directly from a run of the application using your real dataset. They should not be invented or presented as guaranteed attendance.

## 10. Limitations

- Prediction quality depends on the amount and quality of historical data.
- Similar menu descriptions do not always mean similar food popularity.
- Special events, holidays, weather and unexpected changes may affect attendance.
- The current approach is a basic similarity-based model.
- Canteen visits may include repeat visits by the same student.
- The application currently predicts dinner demand only.
- The project has not yet established a measured reduction in food wastage or financial loss.

## 11. Future Improvements

- Collect more historical dinner observations.
- Include special events and holidays.
- Improve menu popularity analysis.
- Compare predictions with actual attendance.
- Measure whether using predictions reduces food wastage.
- Improve the prediction algorithm as more real data becomes available.

## 12. Project Structure

```text
hostelmeal_project/
│
├── app.py
├── predictor.py
├── data.csv
├── test_predictor.py
├── requirements.txt
├── research.md
├── fieldwork.md
├── reflection.md
├── DATA_DICTIONARY.md
├── evidence/
└── ai-chats/
```

## 13. Demo Video

**3-minute application demonstration:** [Add your video link here]

## 14. Author

Developed as a B.Tech take-home assignment.

**Project:** HostelMeal — Menu-Based Dinner Attendance & Demand Prediction
