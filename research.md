# Research notes — HostelMeal (dinner-only scope)

## Problem in five lines
1. The hostel has approximately 1,500 students (user-provided estimate).
2. The project focuses ONLY on dinner demand at the main mess and the separate night canteen.
3. The night canteen has its own menu and operates from main-mess dinner time until 3 AM.
4. User-reported dinner attendance varies by weekday: Tuesday 900, Thursday 950, Friday 1,200, Saturday 500 and Sunday 800; the counting location/method is not yet confirmed.
5. The project will investigate whether each location's dinner menu, weekday and contextual factors help explain dinner attendance and canteen visits.

## Person and place
- Tarun - Mess Supervisor
- 50 steps from our hostel. MEGA MESS


## Existing solutions
No existing solution, due to unpredictable and less accurate guess, surplus food goes to dustbin.



## Status
Working draft. Synthetic demo data is not research evidence or fieldwork.
# Research — HostelMeal (Dinner Demand Forecasting)

## 1. Problem in five lines

1. The hostel has approximately 1,500 students, according to the student's estimate.
2. The main mess and a separate night canteen both serve during dinner hours; the night canteen operates until 3:00 AM.
3. The two locations have different dinner menus, and the number of students choosing each location appears to vary by day and menu.
4. The student reported main/combined dinner attendance figures of Tuesday 900, Thursday 950, Friday 1,200, Saturday 500 and Sunday 800; the exact counting scope and source still need confirmation.
5. HostelMeal will investigate whether dinner menu, weekday, day type and relevant hostel context help estimate main-mess attendance and night-canteen demand.

## 2. Person and place

- **Intended user:** The real mess manager, kitchen supervisor or night-canteen operator who plans dinner preparation. The actual person must be selected and interviewed during fieldwork.
- **Person's name and role:** Tarun MESS SUPERVISOR
- **Place:** The student's own hostel main mess and its night canteen. Add the actual hostel/institution name and location after confirming what may be shared publicly.
- **Observation date and time:** 18-11-2026 MEGA MESS
- **Why this person:** They are directly involved in deciding or carrying out food preparation and can explain how expected attendance is currently estimated.

## 3. What is known so far (student-provided information)

- Approximate hostel population: 1,500.
- Scope selected for the project: dinner only.
- Main mess and night canteen have separate menus.
- Night canteen begins service around main-mess dinner time and continues until 3:00 AM.
- Student-reported dinner counts:
  - Tuesday: about 900
  - Thursday: about 950
  - Friday: about 1,200
  - Saturday: about 500
  - Sunday: about 800
- These five figures are preliminary observations, not yet verified fieldwork data. Before using them as training labels, confirm whether they count main-mess diners only, canteen customers only, or both; confirm how they were counted and the dates they refer to.
- A weekly menu photograph was supplied. The readable dinner items include different rice/roti, dal, vegetable, paneer/egg/chicken and dessert combinations on different days. Some text in the photograph is small, so the original menu should be checked with the staff rather than treating uncertain OCR/transcription as definitive.

## 4. Problem to investigate

A fixed attendance assumption based only on "veg day" or "non-veg day" is too simple. Menus change daily, and the two locations offer different choices. The project will test whether menu information and weekday patterns are associated with dinner attendance at each location.

The project should not assume that a student who does not eat in the mess necessarily goes to the night canteen. Some students may eat elsewhere, skip dinner, leave campus, or visit the canteen more than once. Therefore:
- Main-mess attendance should be recorded as a clearly defined meal count.
- Night-canteen activity should be recorded as visits/transactions unless a reliable method can count unique students.
- Counts should be recorded separately by location and by a clearly defined time window.
- If the canteen remains open until 3:00 AM, separate the dinner-time window from later-night visits instead of mixing all visits into one ambiguous number.

## 5. Two existing approaches / solutions to compare

These are candidate approaches found in food-service practice and literature. **They are not confirmed to be used by this hostel.** During the staff interview, ask which methods are actually used and replace or revise this section based on the answer.

### Existing approach 1 — Staff experience and recent-day estimates
A manager or kitchen team estimates the next dinner's attendance using memory, recent attendance and knowledge of the menu.

- **Why it may not fit this situation:** It can be difficult to consistently account for two different menus, weekday variation, late-night canteen visits and unusual days. The estimate may also be hard to audit after the meal.
- **What must be checked with the real user:** Does the manager currently rely on experience? What information do they look at? Which days are hardest to estimate? Do they keep any written record?

### Existing approach 2 — Manual count, token/register or transaction tally
A team may use meal tokens, a paper register, a headcount or canteen sales/transaction totals as a record of demand.

- **Why it may not fit this situation:** A single total may not distinguish the main mess from the night canteen, or dinner-time demand from visits after dinner. A transaction total may count repeat visits rather than unique students. A tally also describes what happened, but does not by itself forecast the next menu's demand.
- **What must be checked with the real user:** Is there a token/register/POS record? Does it record the time and location? Can it separate dinner from after-dinner visits? Are cancellations, staff meals or repeat transactions included?

## 6. Two external sources read

### Source 1
Gul Fatma Turker (2025), “Reducing Food Waste in Campus Dining: A Data-Driven Approach to Demand Prediction and Sustainability,” *Sustainability*, 17(2), 379. https://doi.org/10.3390/su17020379

Three-line note:
1. The paper studies campus dining demand using actual institutional data, including dining-hall entries, menu information, campus movement and cafeteria turnover.
2. It reports that menu composition and meal variety are useful factors to examine alongside attendance and other context when planning campus food demand.
3. This supports testing menu-aware dinner estimates in our hostel, but its dataset is much richer than the small dataset available here; its reported model accuracy must not be copied or assumed for HostelMeal.

### Source 2
Christopher Malefors et al. (2019), “Towards a Baseline for Food-Waste Quantification in the Hospitality Sector—Quantities and Data Processing Criteria,” *Sustainability*, 11(13), 3541. https://doi.org/10.3390/su11133541

Three-line note:
1. The study analyses food-waste measurements from hospitality kitchens and emphasizes consistent definitions and primary measurements.
2. It discusses measures such as waste per portion and waste as a percentage of food served, and explains that missing or inconsistent data can distort comparisons.
3. This informs our data-collection design: use consistent counting methods and, if the mess permits, record leftover/waste quantity separately from attendance. Attendance alone cannot prove that food waste was reduced.

## 7. Proposed project output

For a selected upcoming dinner, the prototype will show:
- Estimated main-mess dinner attendance.
- Estimated night-canteen dinner visits.
- The historical records most similar to the selected menus and weekday.
- A clear warning when the available comparable data is insufficient.

Food quantity recommendations are a later extension. They require portion/recipe information and actual prepared/leftover quantities; attendance counts alone are not enough to calculate kilograms of food.

## 8. Data needed from fieldwork

For each real observation, collect:
- Date and weekday.
- Main-mess dinner menu.
- Night-canteen menu.
- Main-mess attendance and how it was counted.
- Night-canteen visits, separated into dinner-time and post-dinner time slots.
- Approximate hostel occupancy or known absences, if available.
- Exam days, holidays, events, stockouts or unusual circumstances.
- Optional prepared quantity and leftover quantity, if staff can measure them.

Collect at least 20 real entries personally. Do not fill missing days with generated values. Keep synthetic development data in a separate file and label it clearly.

## 9. Fieldwork questions to validate the problem

1. How do you currently decide how much dinner to prepare?
2. Do you record the number of students eating in the main mess each day? How?
3. Do you have separate night-canteen sales or visitor counts?
4. Which menu items or combinations usually change dinner demand?
5. What happens on low-attendance days: leftover food, smaller batches, or something else?
6. What would be most useful: attendance estimate, food quantity estimate, or an alert that demand may be unusually high/low?

## 10. Status and honesty note

This file is a research draft prepared from the student's description, supplied menu image, and the two external sources listed above. It does not replace the required in-person interview or field observation. The real staff member's name, exact place/date, actual existing solutions, timestamped photos and at least 20 personally collected observations remain to be added after fieldwork. Do not submit invented details as facts.
