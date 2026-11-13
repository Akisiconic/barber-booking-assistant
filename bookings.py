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


def book_slot(booked_slots, hour):
    """Book `hour` by adding it to `booked_slots`.

    Returns True if it was booked, or False if that hour was already taken.
    """
    if hour in booked_slots:
        return False
    booked_slots.append(hour)
    return True


def cancel_booking(booked_slots, hour):
    """Cancel the booking at `hour` by removing it from `booked_slots`.

    Returns True if it was cancelled, or False if there was no booking at that hour.
    """
    if hour not in booked_slots:
        return False
    booked_slots.remove(hour)
    return True


def reschedule_booking(booked_slots, old_hour, new_hour):
    """Move a booking from `old_hour` to `new_hour`.

    Returns True if it moved, or False if there was no booking at `old_hour`
    or `new_hour` is already taken. Nothing changes when it returns False.
    """
    if old_hour not in booked_slots or new_hour in booked_slots:
        return False
    cancel_booking(booked_slots, old_hour)
    book_slot(booked_slots, new_hour)
    return True


def ask_hour(question):
    """Keep asking `question` until the user types a whole number, then return it."""
    while True:
        try:
            return int(input(question))
        except ValueError:
            print("Please type the hour as a number, like 14.")


if __name__ == "__main__":
    booked = [9, 10, 11]
    day = "monday"

    while True:
        print()
        print("1 = Book")
        print("2 = Cancel")
        print("3 = Reschedule")
        print("4 = View bookings")
        print("5 = Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            hour = ask_hour("What hour do you want to come in? (9-17): ")
            status = shop_status(day, hour)
            if status != "Shop is open":
                print(status)
            elif hour in booked:
                next_slot = find_next_slot(booked, hour)
                if next_slot is None:
                    print("Sorry, that's taken and there are no times left today.")
                else:
                    print(f"Sorry, that's taken. The next free time is {next_slot}:00")
            elif book_slot(booked, hour):
                print(f"You're booked in for {hour}:00!")
            else:
                print("Sorry, someone just took that slot.")

        elif choice == "2":
            hour = ask_hour("Which hour do you want to cancel? ")
            if cancel_booking(booked, hour):
                print(f"Your {hour}:00 booking is cancelled.")
            else:
                print(f"There's no booking at {hour}:00.")

        elif choice == "3":
            old_hour = ask_hour("Which hour is your booking now? ")
            new_hour = ask_hour("What hour do you want to move to? (9-17): ")
            status = shop_status(day, new_hour)
            if status != "Shop is open":
                print(status)
            elif reschedule_booking(booked, old_hour, new_hour):
                print(f"Moved your booking from {old_hour}:00 to {new_hour}:00.")
            else:
                print("Couldn't move it. Check you have a booking at that hour and the new time is free.")

        elif choice == "4":
            if booked:
                for hour in sorted(booked):
                    print(f"- {hour}:00")
            else:
                print("No bookings yet.")

        elif choice == "5":
            print("Bye!")
            break

        else:
            print("Please choose a number from 1 to 5.")
