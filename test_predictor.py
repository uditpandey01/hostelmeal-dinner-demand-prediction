import pandas as pd
import pytest

from predictor import menu_similarity, predict_dinner, validate_data


def sample():
    return pd.DataFrame([
        {
            "date": "2026-10-01", "weekday": "Monday", "day_type": "Veg",
            "mess_dinner_menu": "rice dal roti", "canteen_dinner_menu": "noodles egg roll",
            "mess_attendance": 800, "canteen_visits": 120, "notes": "test",
        },
        {
            "date": "2026-10-08", "weekday": "Monday", "day_type": "Veg",
            "mess_dinner_menu": "rice dal roti", "canteen_dinner_menu": "noodles egg roll",
            "mess_attendance": 900, "canteen_visits": 140, "notes": "test",
        },
        {
            "date": "2026-10-09", "weekday": "Tuesday", "day_type": "Non-veg",
            "mess_dinner_menu": "chicken rice", "canteen_dinner_menu": "chicken roll",
            "mess_attendance": 1000, "canteen_visits": 180, "notes": "test",
        },
    ])


def test_identical_menus_score_one():
    assert menu_similarity("Rice, dal and roti", "rice dal roti") == 1.0


def test_prediction_returns_separate_measures():
    estimates, matches, warnings = predict_dinner(
        sample(), "Monday", "Veg", "rice dal roti", "noodles egg roll", k=2
    )
    assert estimates == {"mess_attendance": 850, "canteen_visits": 130}
    assert len(matches["mess"]) == 2
    assert len(matches["canteen"]) == 2
    assert warnings == []


def test_bad_negative_count_is_skipped():
    data = sample()
    data.loc[0, "mess_attendance"] = -1
    cleaned, warnings = validate_data(data)
    assert len(cleaned) == 2
    assert warnings
