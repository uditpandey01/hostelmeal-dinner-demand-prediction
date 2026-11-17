"""Explainable dinner-only menu similarity baseline."""
import pandas as pd

def menu_similarity(a, b):
    a = set(str(a).lower().replace(",", " ").split())
    b = set(str(b).lower().replace(",", " ").split())
    return len(a & b) / len(a | b) if a | b else 0.0

def predict_dinner(df, weekday, day_type, mess_menu, canteen_menu, k=5):
    required = {"weekday","day_type","mess_dinner_menu","canteen_dinner_menu",
                "mess_attendance","canteen_visits"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    estimates = {}
    for menu_col, target_col, menu, label in [
        ("mess_dinner_menu","mess_attendance",mess_menu,"mess_attendance"),
        ("canteen_dinner_menu","canteen_visits",canteen_menu,"canteen_visits")
    ]:
        pool = df.copy()
        pool["menu_similarity"] = pool[menu_col].apply(lambda x: menu_similarity(menu,x))
        pool["weekday_match"] = (pool.weekday == weekday).astype(int)
        pool["day_type_match"] = (pool.day_type == day_type).astype(int)
        pool["score"] = .65*pool.menu_similarity + .25*pool.weekday_match + .10*pool.day_type_match
        nearest = pool.sort_values("score",ascending=False).head(k)
        estimates[label] = round(float(nearest[target_col].mean()))
    return estimates
