# database.py - saves and loads the bookings so they don't disappear
import json

FILE_NAME = "bookings.json"


def save_bookings(booked_slots):
    """Write the list of booked hours to bookings.json."""
    with open(FILE_NAME, "w") as file:
        json.dump(booked_slots, file)


def load_bookings():
    """Read the booked hours from bookings.json.

    Returns an empty list if the file doesn't exist yet (first run).
    """
    try:
        with open(FILE_NAME) as file:
            return json.load(file)
    except FileNotFoundError:
        return []
