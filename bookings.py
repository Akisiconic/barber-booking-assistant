# bookings.py - handles booking, rescheduling and cancelling appointments
#
# These are the shop rules. Right now they're plain values; in the next step
# they move into the database so the barber can change them from the app.

OPEN_TIME = 9      # first slot starts at 9:00
CLOSE_TIME = 18    # shop closes at 18:00, so the last slot is 17:00
LUNCH_TIME = 12    # no bookings 12:00-13:00
CLOSED_DAYS = {"sunday"}


def is_closed_day(day):
    """True if the shop is closed all day (e.g. Sunday)."""
    return day.lower() in CLOSED_DAYS


def find_next_slot(booked_slots, after_hour=OPEN_TIME):
    """Return the first free hour from `after_hour` onwards, or None if the day is full.

    Skips lunch and any hour already in `booked_slots`.
    """
    for time_slot in range(max(after_hour, OPEN_TIME), CLOSE_TIME):
        if time_slot == LUNCH_TIME:
            continue
        if time_slot in booked_slots:
            continue
        return time_slot
    return None


def shop_status(day, hour):
    """Describe whether the shop is open at a given day and hour."""
    if is_closed_day(day):
        return "We are closed today"
    if hour >= CLOSE_TIME:
        return "Shop is closed"
    if hour == LUNCH_TIME:
        return "Barber is on lunch, back at 1"
    if hour >= OPEN_TIME:
        return "Shop is open"
    return "We are still closed right now!"


if __name__ == "__main__":
    booked = [9, 10, 11, 13]
    day = "monday"

    hour = int(input("What hour do you want to come in? (9-17): "))

    if shop_status(day, hour) != "Shop is open":
        print(shop_status(day, hour))
    elif hour in booked:
        print("Sorry, that slot is already taken.")
    else:
        print(f"{hour}:00 is available!")
