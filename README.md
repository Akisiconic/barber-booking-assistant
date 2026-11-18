# Barber Booking App

A terminal-based booking system for a barbershop, built in Python.
Customers can book, cancel, and reschedule hourly appointments,
and bookings are saved between sessions.

## Features
- Book an available time slot (checks shop hours, closed days, and lunch break)
- Suggests the next free slot if the chosen time is taken
- Cancel and reschedule bookings
- Input validation (handles non-numeric and out-of-hours input)
- Bookings saved to a JSON file so they persist after closing

## How to Run
1. Make sure Python 3 is installed
2. Clone the repo and go into the folder:
   ```
   git clone https://github.com/Akisiconic/barber-booking-assistant.git
   cd barber-booking-assistant
   ```
3. Run:
   ```
   python3 bookings.py
   ```

## Running the Tests
```
pip install pytest
python3 -m pytest
```

## Project Structure
- `bookings.py` – booking logic and menu
- `database.py` – saves and loads bookings (JSON)
- `tests/` – automated tests for the booking rules and saving/loading
- `app.py` – (planned) Flask web booking page
- `ai_assistant.py` – (planned) AI booking assistant

## What I Learned
- Writing reusable functions with return values
- Input validation with try/except
- Persisting data with JSON file handling

## Roadmap
- [ ] Move storage from JSON to SQLite
- [ ] Flask web pages for customers and a barber view
- [ ] AI assistant for booking through chat
