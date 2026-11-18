# Research notes — HostelMeal (dinner-only scope)

## 1. Problem in five lines

1. The hostel has approximately 1,500 students all assigned to have food from Mega Mess.
2. The mega mess and a separate night canteen both serve during dinner hours; the night canteen operates until 3:00 AM.
3. The two locations have different dinner menus, and the number of students choosing each location appears to vary by day and menu.
4. The mega mess  dinner attendance figures of Monday 1000, Tuesday 900, Wednesday 1100,Thursday 950, Friday 1,200, Saturday 500 and Sunday 800; 
5. HostelMeal will investigate whether dinner menu, weekday, day type and relevant hostel context help estimate main-mess attendance and night-canteen demand.

## 2. Person and place

- **Intended user:** The real mess manager, kitchen supervisor or night-canteen operator who plans dinner preparation.
- **Person's name and role:** Tarun MESS SUPERVISOR
- **Place:** Our own hostel main mess and its night canteen. Mega Mess and Hostel-K night canteen.
- **Observation date and time:** 17-11-2026 MEGA MESS
- **Why this person:** They are directly involved in deciding or carrying out food preparation and can explain how expected attendance is currently estimated.


## 4. Problem to investigate

A fixed attendance assumption based only on "veg day" or "non-veg day" is too simple. Menus change daily, and the two locations offer different choices. The project will test whether menu information and weekday patterns are associated with dinner attendance at each location.

The project should not assume that a student who does not eat in the mess necessarily goes to the night canteen. Some students may eat elsewhere, skip dinner, leave campus, or visit the canteen more than once. Therefore:
- Main-mess attendance should be recorded as a clearly defined meal count.
- Night-canteen activity should be recorded as visits/transactions unless a reliable method can count unique students.
- Counts should be recorded separately by location and by a clearly defined time window.
- If the canteen remains open until 3:00 AM, separate the dinner-time window from later-night visits instead of mixing all visits into one ambiguous number.

## 5. Two existing approaches / solutions to compare


### Existing approach 1 — Staff experience and recent-day estimates
A manager or kitchen team estimates the next dinner's attendance using memory, recent attendance and knowledge of the menu.

- **Why it may not fit this situation:** It can be difficult to consistently account for two different menus, weekday variation, late-night canteen visits and unusual days. The estimate may also be hard to audit after the meal.
- Some days are actually very difficult to judge when there is chicken in non - veg and paneer in veg.

### Existing approach 2 — Manual count, token/register or transaction tally
A team may use meal tokens, a paper register, a headcount or canteen sales/transaction totals as a record of demand.

- **Why it may not fit this situation:** A single total may not distinguish the main mess from the night canteen, or dinner-time demand from visits after dinner. A transaction total may count repeat visits rather than unique students. A tally also describes what happened, but does not by itself forecast the next menu's demand.
- This token approach is not feasable on daily basis doing this multiple times created kaos and made students to wait for much longer time creating inconveinience.

## 6. Two external sources read

### Source 1
Gul Fatma Turker (2025), “Reducing Food Waste in Campus Dining: A Data-Driven Approach to Demand Prediction and Sustainability,” *Sustainability*, 17(2), 379. https://doi.org/10.3390/su17020379

Three-line note:
1. The paper studies campus dining demand using actual institutional data, including dining-hall entries, menu information, campus movement and cafeteria turnover.
2. It reports that menu composition and meal variety are useful factors to examine alongside attendance and other context when planning campus food demand.
3. This supports testing menu-aware dinner estimates in our hostel, but its dataset is much richer than the small dataset available here;

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





