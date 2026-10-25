# Barber Booking Assistant

## The problem
I cut hair, and managing my clients is a constant headache: booking over text, last-minute reschedules, cancellations, and no-shows that waste slots another client could have taken. I'm building this to handle all of that through a simple chat.

## V1 features
**Barber:**
- Set services and prices
- Set working hours
- See today's bookings
- Mark a client as "not here"

**Client (by chat):**
- Book an open slot in plain language ("can I come in at 3 tomorrow?")
- Let the barber know they're running late
- Reschedule
- Cancel

**No-show handling:** when the barber marks a client as not here, the AI messages them asking for an ETA. If there's no reply in 10 minutes, it asks the barber whether to cancel. The slot is only freed after the barber confirms.

## Tech
Python, SQLite, Streamlit, LLM API

## Status
In progress