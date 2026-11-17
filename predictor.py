"""Explainable dinner-only demand forecast for HostelMeal.

This is a simple nearest-neighbour baseline, not a trained machine-learning model.
It uses menu word overlap, weekday match, and veg/non-veg match.
"""
from __future__ import annotations

import re
from typing import Tuple

import pandas as pd

REQUIRED_COLUMNS = {
    "date", "weekday", "day_type", "mess_dinner_menu",
    "canteen_dinner_menu", "mess_attendance", "canteen_visits", "notes",
}
VALID_WEEKDAYS = {
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday",
}
VALID_DAY_TYPES = {"Veg", "Non-veg"}


def _tokens(value: object) -> set[str]:
    """Normalize a menu into simple word tokens."""
    return set(re.findall(r"[a-z0-9]+", str(value).lower())) - {"and", "with", "the", "a", "an"}


def menu_similarity(menu_a: object, menu_b: object) -> float:
    """Jaccard similarity between two menu descriptions (0 to 1)."""
    a, b = _tokens(menu_a), _tokens(menu_b)
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def validate_data(df: pd.DataFrame) -> Tuple[pd.DataFrame, list[str]]:
    """Return cleaned usable rows and human-readable data quality warnings."""
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required columns: {', '.join(sorted(missing))}")

    clean = df.copy()
    warnings: list[str] = []

    for col in ("mess_attendance", "canteen_visits"):
        clean[col] = pd.to_numeric(clean[col], errors="coerce")

    before = len(clean)
    clean = clean.dropna(subset=[
        "weekday", "day_type", "mess_dinner_menu", "canteen_dinner_menu",
        "mess_attendance", "canteen_visits",
    ])
    if len(clean) != before:
        warnings.append(f"Skipped {before - len(clean)} row(s) with missing or non-numeric required values.")

    clean["weekday"] = clean["weekday"].astype(str).str.strip().str.title()
    clean["day_type"] = clean["day_type"].astype(str).str.strip()
    invalid_weekday = ~clean["weekday"].isin(VALID_WEEKDAYS)
    invalid_type = ~clean["day_type"].isin(VALID_DAY_TYPES)
    invalid_count = (clean["mess_attendance"] < 0) | (clean["canteen_visits"] < 0)
    invalid = invalid_weekday | invalid_type | invalid_count
    if invalid.any():
        warnings.append(f"Skipped {int(invalid.sum())} row(s) with invalid weekday, day type, or negative counts.")
        clean = clean.loc[~invalid].copy()

    clean["mess_attendance"] = clean["mess_attendance"].round().astype(int)
    clean["canteen_visits"] = clean["canteen_visits"].round().astype(int)

    if clean.empty:
        raise ValueError("No usable rows remain. Check the CSV values and try again.")
    return clean, warnings


def _estimate(
    df: pd.DataFrame,
    menu_col: str,
    target_col: str,
    menu: str,
    weekday: str,
    day_type: str,
    k: int,
) -> tuple[int, pd.DataFrame]:
    ranked = df.copy()
    ranked["menu_similarity"] = ranked[menu_col].apply(
        lambda historical_menu: menu_similarity(menu, historical_menu)
    )
    ranked["weekday_match"] = (ranked["weekday"] == weekday).astype(int)
    ranked["day_type_match"] = (ranked["day_type"] == day_type).astype(int)
    # Weights sum to 1. Menu matters most; weekday and veg/non-veg add context.
    ranked["similarity_score"] = (
        0.65 * ranked["menu_similarity"]
        + 0.25 * ranked["weekday_match"]
        + 0.10 * ranked["day_type_match"]
    )
    nearest = ranked.sort_values(
        ["similarity_score", "date"], ascending=[False, False]
    ).head(max(1, min(int(k), len(ranked))))
    estimate = int(round(float(nearest[target_col].mean())))
    return estimate, nearest


def predict_dinner(
    df: pd.DataFrame,
    weekday: str,
    day_type: str,
    mess_menu: str,
    canteen_menu: str,
    k: int = 5,
) -> tuple[dict[str, int], dict[str, pd.DataFrame], list[str]]:
    """Predict main-mess attendance and separate canteen visits."""
    clean, warnings = validate_data(df)
    if weekday not in VALID_WEEKDAYS:
        raise ValueError("Choose a valid weekday.")
    if day_type not in VALID_DAY_TYPES:
        raise ValueError("Choose Veg or Non-veg.")
    if not mess_menu.strip() or not canteen_menu.strip():
        raise ValueError("Enter both dinner menus.")

    mess_value, mess_rows = _estimate(
        clean, "mess_dinner_menu", "mess_attendance",
        mess_menu, weekday, day_type, k,
    )
    canteen_value, canteen_rows = _estimate(
        clean, "canteen_dinner_menu", "canteen_visits",
        canteen_menu, weekday, day_type, k,
    )
    return (
        {"mess_attendance": mess_value, "canteen_visits": canteen_value},
        {"mess": mess_rows, "canteen": canteen_rows},
        warnings,
    )
